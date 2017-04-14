#!/bin/bash -e 

sudo docker rm (sudo docker ps -aq)
sudo docker images | grep none | awk '{print "sudo docker rmi " $3;}' | sh
sudo docker volume ls -qf dangling=true | xargs -r sudo docker volume rm