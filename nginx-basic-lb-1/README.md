# NGINX Basic Load Balancing 1

* Load balance several containers by exposing container ports (nginx.conf references container IP's and mapped ports).
* Flask-based app.

# Quick Start

## Install Docker Engine (`docker-ce`, etc.)

Start here, find your distro, and follow the directions:

https://docs.docker.com/engine/install/

## Install Docker Compose (`docker-compose`)

Start here, find your distro, and follow the directions:

https://docs.docker.com/compose/install/

## Quick list of commands for `nginx-basic-lb-1`
Run these after installing Docker Engine and Docker Compose
```
cd ~
git clone https://github.com/tabernarious/nginx-demo.git
cd ~/nginx-demo/nginx-basic-lb-1
sudo docker-compose down
sudo docker-compose build
sudo docker-compose up -d
sudo docker-compose ps
```

Hit the load balancer from the Docker Host's CLI (try several times)
```
curl http://localhost:8081/
```

Hit the load balancer from a browser (locally or externally):

http://localhost:8081/ (if you're running Docker locally)

http://DOCKER-HOST-IP:8081/ (if you're running Docker on a separate host/server)

# Full Walkthrough

See main README.md