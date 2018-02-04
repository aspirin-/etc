# fish 

## Docker

    function docker_cleanup
        docker rm (docker ps -aq) 2>/dev/null; or echo "Containers already clean."
        docker rmi (docker images | grep none | awk '{print $3}') 2>/dev/null; or echo "Images already clean."
    end
