#!/bin/bash

docker run -d --name redis-dmx -p 6379:6379 redis
docker exec -it redis-dmx redis-cli
