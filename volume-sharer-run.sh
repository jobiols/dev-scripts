#!/usr/bin/env bash

sudo docker run --name volume-sharer \
           --rm \
           -d \
           -v /var/lib/docker/volumes:/docker_volumes \
           -p 139:139 \
           -p 445:445 \
           -v /var/run/docker.sock:/var/run/docker.sock \
           --net=host \
           gdiepen/volume-sharer