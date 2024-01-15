# Docker

```bash
service docker status
```
```bash
service docker start
```
```bash
docker version
```
```bash
docker info
```

## Containers
```bash
docker container ls
```
```bash
docker container ls -a
```

## Run container
```bash
docker container run ubuntu
```
```bash
docker container run nginx
```


### Execute command inside the container
```bash
docker container run ubuntu sleep 5
```


### Start, Stop, and Restart container
```bash
docker container start CONTAINER_ID
```
```bash
docker container stop CONTAINER_ID
```
```bash
docker container restart CONTAINER_ID
```

### Container in background
`d`: detach
`i`: interactive
`t`: tty
```bash
docker container run -d ubuntu sleep
```
```bash
docker container run -it ubuntu bash
```

### Exit from the container without stopping
- Ctrl + P -> Q


### Remove container
```bash
docker container rm CONTAINER_ID CONTAINER_ID
```

### Info about the container
```bash
docker container inspect CONTAINER_ID
```
```bash
docker container logs CONTAINER_ID
```
```bash
docker container top CONTAINER_ID
```

### Resource usage
```bash
docker container stats
```


### Execute Command
```bash
docker container exec -it CONTAINER_ID /bin/bash
```

### Other
```bash
docker container attach CONTAINER_ID
```
```bash
docker container kill CONTAINER_ID
```
```bash
docker container stop CONTAINER_ID
```
```bash
docker container wait CONTAINER_ID
```
```bash
docker container pause CONTAINER_ID
```
```bash
docker container unpause CONTAINER_ID
```
Remove containers not running
```bash
docker container prune -f
```

File changes in the container respect to the image
```bash
docker container diff CONTAINER_ID
```

Copying files into a container
```bash
docker container cp test/ CONTAINER_ID:/tmp/
```

Port Forwarding or Port Mapping
```bash
docker container run -d -p 3600:80 --name test1 nginx
```

Priviledged container
```bash
docker container run --privileged IMAGE_NAME
```

### Export and Import
```bash
docker container export CONTAINER_ID > my_ubuntu.tar
```
```bash
docker image import my_ubuntu.tar NEW_NAME
```
```bash
docker container run -it NEW_NAME /bin/bash
```


## Docker Image
```bash
docker image ls
```
Pull image with tag
```bash
docker pull ubuntu:14.04
```
```bash
docker image rm ubuntu
```
```bash
docker image rm -f ubuntu
```
```bash
docker image inspect ubuntu
```

## Docker volume
```bash
docker volume create myvol
```
```bash
docker volume rm vol1 vol2
```
```bash
docker volume prune
```
Bind mount
```bash
docker container run -it -v $(pwd):/tmp/test ubuntu bash
```

## Docker Networking
```bash
docker network ls
```
```bash
docker network inspect bridge
```
Create new network (all the custom-created networks are DNS enabled)
```bash
docker network create -d bridge mynetwork
```
```bash
docker network rm mynetwork
```
```bash
docker network prune
```

Attach to new network
```bash
docker container run -it --network mynetwork ubuntu bash
```

Host Network
```bash
docker container run -itd --network=host ubuntu bash
```
None Network
```bash
docker container run -itd --network=none ubuntu bash
```

### Connect and Disconnect
Connecting and disconnecting to multiple networks.
```bash
docker container run -it --network bridge ubuntu bash
```
Now connect the container to the test network
```bash
docker network connect mynetwork
```
Now disconnect the test network
```bash
docker network disconnect mynetwork
```

## Dockerfile
```bash
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y tree
RUN touch /tmp/hello1.txt
RUN touch /tmp/hello2.txt
RUN echo "hello world!" > /tmp/hello3.txt
```
```bash
FROM ubuntu:20.04
LABEL name="Suvam Basak"
LABEL email="20mcmb08@uohyd.ac.in"
ENV NAME Basak
ENV PASSWORD passwd
WORKDIR /tmp
RUN pwd>/tmp/pwd.txt
```
```bash
FROM python:3.9-slim-buster
WORKDIR /usr/src/app
COPY ./fetch.py .
CMD [ "python3", "./fetch.py" ]
```

### Push to Docker hub
Building image from Dockerfile
```bash
docker image build -t pyimg:1 .
```
Change the image name (username/image_name:tag)
```bash
docker tag pyimg:1 suvambasak/pyimg:1
```
Push
```bash
docker login
```
```bash
docker push suvambasak/pyimg:1
```

### Multi Architecture Build with Buildx
Building image for multiple CPU architectures
```bash
docker buildx ls
```
Create a new builder
```bash
docker buildx create --name crossbuild
```
Use that builder
```bash
docker buildx use crossbuild
```
```bash
docker buildx inspect --bootstrap
```
Build the image and push it to the registry
```bash
docker buildx build --platform linux/arm64,linux/amd64,linux/arm/v7,linux arm/v6 -t suvambasak/pyimg:1 --push .
```

## Docker Compose
Make a new file name: `docker-compose.yaml`
```YAML
version: "3.8"
services:
    webserver:
        image: nginx
        ports:
            - "8080:80"
```
```bash
docker-compose up -d
```
```bash
curl localhost:8080
```
```bash
docker-compose down
```
## Running two containers (Gonna use the previous container unless it is changed)
```YAML
version: "3.8"
services:
    webserver_1:
        image: nginx
        ports:
            - "8080:80"
    webserver_2:
        image: nginx
        ports:
            - "8081:80"
```

```bash
docker-compose up -d
curl localhost:8080
curl localhost:8081
docker-compose down
```
# Docker Swarm

## Setup
Manager node
```bash
docker swarm init
```
```bash
docker swarm init --advertise-addr 172.27.28.217
```
Get the joining token later
```bash
docker swarm join-token worker
```
```bash
docker swarm join-token manager
```
Add worker nodes
```bash
 docker swarm join --token SWMTKN-1-0jyybxslust2j468pg3r8f0lst0qwtpy8xjn2uwkvxg6qmfz95-4sufwllpjcbzn184scnd1dc0n 172.27.28.217:2377
```
Only on the manager node
```bash
docker node ls
```

Worker node leave (Now the info will show swarm inactive. But Manager is still not aware that the worker left)
```bash
docker swarm leave
```
Manager node remove worker nodes
```bash
docker node rm worker2
```
```bash
docker node rm -f worker1
```
Promote and Demote
```bash
docker node promote worker1 worker2
```
```bash
docker node demote worker1 worker2
```

### Node Availability
```bash
docker node ls
```
- Active: Node is ready to take a job from the manager
- Pause: All tasks running will be kept running but not ready to take a new job
- Drain: If need to shift all running containers to other nodes

```bash
docker node update --availability=pause worker2
```
```bash
docker node update --availability=drain worker2
```

## Docker services
Only works on the Manager node
```bash
docker container ls
```
```bash
docker service ls
```
Creating service
```bash
docker service create -d alpine ping 8.8.8.8
```
```bash
docker service inspect SERVICE_ID
```
```bash
docker service logs SERVICE_ID
```
Creating service with multiple replicas
```bash
docker service create -d --replicas 4 apline ping 127.0.0.1
```
Scalling
```bash
docker service scale SERVICE_ID=10 SERVICE_ID=3
```
Port mapping 
```bash
docker service create -d -p 8090:80 nginx
```

Create one container for each node in the cluster
```bash
docker service create --mode=global alpine ping 8.8.8.8
```

Create containers only for managers
```bash
docker service create --replicas=3 --constraint=”node.role==manager” alpine ping 8.8.8.8
```
Create containers only on the worker node.
```bash
docker service create --replicas=3 --constraint=”node.role==worker” alpine ping 8.8.8.8
```
Adding labels
```bash
docker node update --label-add=”sdd=true” worker1
```
```bash
docker service create --replicas=3 --constraint=”node.labels.ssd==true” alpine ping 8.8.8.8
```

## Swarm Networking
```bash
docker network create -d overlay test_nw
```
```bash
docker service create -d --replicas 3 --network test_nw IMAGE_NAME
```

## Docker Stack

```bash
docker stack deploy --compose-file docker-compose.yaml MYNAME
```