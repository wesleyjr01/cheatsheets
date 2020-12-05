# Docker Cheatsheet

### Dockerfile Reference:
https://docs.docker.com/engine/reference/builder/

## Installation
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04


## Executing Docker Commands Without sudo

```
$ sudo usermod -aG docker ${USER}
$ su - ${USER}
$ id -nG
$ sudo usermod -aG docker username
```

### download ubuntu image into your cmputer
```
$ docker pull ubuntu
```

### Check downloaded images
```
$ docker images
```

### To view active containers
```
$ docker ps
```

### To view all containers — active and inactive
```
$ docker ps -a
```

### Build a image from Dockerfile in current folder
```
$ docker build .
```

### Build a image from Dockerfile in current folder and use --tag to give it a name
```
$ docker build . --tag myimage:1.0
```

### Run the image your built with iteractive mode
```
$ docker run -t myimage:1.0
```

### Check which docker images you have
```
$ docker images
```


### To start a stopped container, use docker start
```
$ docker start <ID>
```

### To stop a running container, use docker stop, followed by the container ID or name
```
$ docker stop sharp_volhard
```

### Remove a container
```
$ docker rm festive_williams
```

# Docker Directives

### COPY
* The COPY instruction copies new files or directories from <src> and adds them to the filesystem of the container at the path <dest>.
```Dockerfile
COPY requirements.txt /code/
```
	
### VOLUME
* The VOLUME instruction creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers. The value can be a JSON array, VOLUME ["/var/log/"], or a plain string with multiple arguments, such as VOLUME /var/log or VOLUME /var/log /var/db. For more information/examples and mounting instructions via the Docker client, refer to [Share Directories via Volumes documentation](https://docs.docker.com/storage/volumes/).

### USER
```
USER <user>[:<group>]
```
The USER instruction sets the user name (or UID) and optionally the user group (or GID) to use when running the image and for any RUN, CMD and ENTRYPOINT instructions that follow it in the Dockerfile.

### WORKDIR
```
WORKDIR /path/to/workdir
```
The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile. If the WORKDIR doesn’t exist, it will be created even if it’s not used in any subsequent Dockerfile instruction.

The WORKDIR instruction can be used multiple times in a Dockerfile. If a relative path is provided, it will be relative to the path of the previous WORKDIR instruction. 

# Docker Compose

### Rename images   
* `$ docker tag <old_name> <new_name>`

### Docker volumes / Persist Data:   
* The docker-compose.yml file lets you define your application infrastructure as individual services. The services can be connected to each other and each can have a volume attached to it for persistent storage. Volumes are stored in a part of the host filesystem managed by Docker (`/var/lib/docker/volumes/` on Linux).
* Docker data volumes are mounted in:
	* `/var/lib/docker/volumes/<volume-name>/_data`
* Check which volumes you have on disk:
	* `$ docker volume ls -q`
* Inspect a specific volume:
	* `$ docker volumes <volume_name>`
	
### Delete and Start a Clean Docker Instance:   
* https://docs.tibco.com/pub/mash-local/4.1.1/doc/html/docker/GUID-BD850566-5B79-4915-987E-430FC38DAAE4.html
* `docker-compose down`
* `docker rm -f $(docker ps -a -q)`
* `docker volume rm $(docker volume ls -q)`
* `docker-compose up -d`

### Build Docker-Compose
* `$ docker-compose build -d`

### Up Docker Compose
* `$ docker-compose up`
* To ensure to rebuild image: `$ docker-compose up --force-recreate`

### Run a container in interactive mode
* `$ docker run -it <IMAGE_ID> /bin/bash`
