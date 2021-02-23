# NGINX Demos

## References
These sites helped me get going:
* https://towardsdatascience.com/sample-load-balancing-solution-with-docker-and-nginx-cf1ffc60e644
* https://runnable.com/docker/python/docker-compose-with-flask-apps

# Quick Start

## Install Docker Engine (`docker-ce`, etc.)

Start here, find your distro, and follow the directions:

https://docs.docker.com/engine/install/

## Install Docker Compose (`docker-compose`)

Start here, find your distro, and follow the directions:

https://docs.docker.com/compose/install/

## Quick list of commands for `nginx-basic-lb-4`
NOTE: See individual README.md files for respective "quick start" command lists.

Run these after installing Docker Engine and Docker Compose
```
cd ~
git clone https://github.com/tabernarious/nginx-demo.git
cd ~/nginx-demo/nginx-basic-lb-4
sudo docker-compose down
sudo docker-compose build
sudo docker-compose up -d
sudo docker-compose ps
```

Hit the load balancer from the Docker Host's CLI (try several times)
```
curl http://localhost:8084/
```

Hit the load balancer from a browser (locally or externally):

http://localhost:8084/ (if you're running Docker locally)

http://DOCKER-HOST-IP:8084/ (if you're running Docker on a separate host/server)

# Full Walkthrough

## Pick a directory to build In
This will position you in your home directory:
```
cd ~
```

## Clone this GitHub repo
This will create a directory `nginx-demo` in the working directory:
```
git clone https://github.com/tabernarious/nginx-demo.git
```

## Move into the demo directory (e.g. `nginx-basic-lb-4`)
```
cd ~/nginx-demo/nginx-basic-lb-4/
```

## Build containers
```
sudo docker-compose build
```

## Run containers in the background
This must be run from `~/nginx-demo/nginx-basic-lb-4/`
```
sudo docker-compose up -d
```

This can be run from any directory:
```
sudo docker-compose -f ~/nginx-demo/nginx-basic-lb-4/docker-compose.yml up -d
```

## List containers for this docker-compose context
This must be run from `~/nginx-demo/nginx-basic-lb-4/`
```
sudo docker-compose ps
```

This can be run from any directory:
```
sudo docker-compose -f ~/nginx-demo/nginx-basic-lb-4/docker-compose.yml ps
```

## List all docker containers (in all contexts)
```
sudo docker ps -a
```

## Inspect each container
This output is very verbose:
```
sudo docker inspect nginx-basic-lb-4_app1_1
sudo docker inspect nginx-basic-lb-4_app2_1
sudo docker inspect nginx-basic-lb-4_app3_1
sudo docker inspect nginx-basic-lb-4_redis_1
```

TIP: Piping the output to `jq` can make the json output much easier to read. Just don't forget the "`.`" at the end:
```
sudo docker inspect nginx-basic-lb-4_app1_1 | jq .
```

## List and inspect all container networks
```
sudo docker network ls
```
```
NETWORK ID     NAME                       DRIVER    SCOPE
8f73f7f2d089   bridge                     bridge    local
0135f77b58a1   host                       host      local
45355cca6cb9   nginx-basic-lb-4_default   bridge    local
b588a90dd4cd   none                       null      local
```
```
sudo docker network inspect nginx-basic-lb-4_default
```

## Attach to process running in container for troubleshooting
```
sudo docker container attach nginx-basic-lb-4_app1_1
```

## Open a `bash` shell on the running container
```
sudo docker exec -it nginx-basic-lb-4_app1_1 /bin/bash
```
