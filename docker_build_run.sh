#!/usr/bin/env bash
IMAGE_NAME=monpotager
TAG=beta
REPO=thibaultlatrille/${IMAGE_NAME}:${TAG}

echo "Building ${REPO}"
mkdir -p ./docker
docker build -t ${REPO} -f Dockerfile ./docker

echo "Running ${REPO}"
docker run -i -t -p 8000:8000 -v $(pwd):/MonPotager ${REPO} /bin/bash -c "/etc/init.d/postgresql start && python3 manage.py db upgrade && python3 -c 'import app; app.reset_db()' && gunicorn app:app"
