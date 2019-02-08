#!/usr/bin/env bash
sudo docker run \
        --name some-nginx \
        -v /some/content:/usr/share/nginx/html:ro \
        -d \
        nginx