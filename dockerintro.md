# Installation
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

```
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
$ sudo apt update
$ apt-cache policy docker-ce
$ sudo apt install docker-ce
$ sudo systemctl status docker
```

# Executing Dcoker Commands Without sudo

```
$ sudo usermod -aG docker ${USER}
$ su - ${USER}
$ id -nG
$ sudo usermod -aG docker username
```

# Using the Docker Command

```
$ docker [option] [command] [arguments]
```

### Search for images, ubuntu example
```
$ docker search ubuntu
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

### To view the latest container you created
```
$ docker ps -l
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