#!/bin/bash

while true; do
mosquitto_pub -h localhost -t "test" -m '{"42":0,"43":200}'
sleep 1
mosquitto_pub -h localhost -t "test" -m '{"42":70,"43":150}'
sleep 1
mosquitto_pub -h localhost -t "test" -m '{"42":0,"43":200}'
sleep 1
mosquitto_pub -h localhost -t "test" -m '{"42":70,"43":150}'
sleep 1
mosquitto_pub -h localhost -t "test" -m '{"42":30,"43":180}'
sleep 1
mosquitto_pub -h localhost -t "test" -m '{"42":70,"43":0}'
sleep 1
mosquitto_pub -h localhost -t "test" -m '{"42":200,"43":0}'
sleep 1
mosquitto_pub -h localhost -t "test" -m '{"42":200,"43":255}'
sleep 1
mosquitto_pub -h localhost -t "test" -m '{"42":200,"43":0}'
sleep 1

done
