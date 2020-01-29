# Dockerfile
FROM debian

# install necessary tools
RUN apt-get update
RUN apt-get install -qq -y git python3 python3-dev python3-pip
RUN apt-get install -qq -y postgresql-11 postgresql-client-11 postgresql-contrib-11 libpq-dev

# pull git repository
RUN git clone https://github.com/ThibaultLatrille/MonPotager
WORKDIR MonPotager

# install python packages
RUN pip3 install -r requirements.txt

# env variables database
USER postgres
RUN /etc/init.d/postgresql start && psql --command "CREATE USER root WITH SUPERUSER;" && createdb -O root root

USER root
RUN /etc/init.d/postgresql start && psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'password';" && createdb -O docker monpotager
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/11/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/11/main/postgresql.conf
EXPOSE 5432
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
# CMD ["/usr/lib/postgresql/11/bin/postgres", "-D", "/var/lib/postgresql/11/main", "-c", "config_file=/etc/postgresql/11/main/postgresql.conf"]

# RUN createuser docker
# RUN createdb monpotager
ENV APP_SETTINGS="config.DevelopmentConfig"
ENV DATABASE_URL="postgresql://docker:password@localhost/monpotager"
ENV SEED_PATH="/seed_path_reset_all_db"
ENV SECRET_KEY_BASE="af686cd78d5d56cd7af6"
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0"
