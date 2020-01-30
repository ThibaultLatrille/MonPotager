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

# PostgreSQL database creation
USER postgres
RUN /etc/init.d/postgresql start && psql --command "CREATE USER monpotager_user WITH CREATEDB PASSWORD 'password';" && psql --command "CREATE DATABASE monpotager_db OWNER monpotager_user;"
USER root

# env variables database
ENV APP_SETTINGS="config.DevelopmentConfig"
ENV DATABASE_URL="postgresql://monpotager_user:password@localhost/monpotager_db"
ENV SEED_PATH="/seed_path_reset_all_db"
ENV SECRET_KEY_BASE="af686cd78d5d56cd7af6"
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0"
