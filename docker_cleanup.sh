#!/bin/bash -e 

docker rm $(docker ps -aq)
docker images | grep none | awk '{print "docker rmi " $3;}' | sh
docker volume ls -qf dangling=true | xargs -r docker volume rm