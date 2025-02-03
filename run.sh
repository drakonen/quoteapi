#!/usr/bin/env sh
docker run \
    --publish 8000:8000 \
    $(docker build -q .)