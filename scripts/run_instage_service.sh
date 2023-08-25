#!/bin/bash

docker run -d --privileged -e REDIS_HOST='192.168.1.126' -e REDIS_PORT=6379 instage-service:latest

#docker run -d --name mqtt_broker -p 1883:1883 -v ./mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
