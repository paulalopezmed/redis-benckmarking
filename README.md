# Redis Benchmarking

## Introduction


## Get started

### Command to run redis image with Docker

Redis image https://hub.docker.com/r/clue/redis-benchmark

```bash
sudo docker run --name some-redis -d redis
```
 
### Command to control Docker-compose

``` bash 
sudo docker ps --all
sudo docker-compose up --detach
sudo docker-compose down
```

### Running the python client localy
``` bash 
python redis-client.py
```

### Running the python client localy using containers
We will generate the client application image using the [official Docker image for python](https://hub.docker.com/_/python).

``` bash 
sudo docker-compose up --detach
```
#### Install dependencies for Python client
``` bash 
pip install -r requirements.txt
```
#### Manual build and run (without Docker-compose)

``` bash 
sudo docker build -t redis-client .
sudo docker run --network host redis-client
```


## Documentation used

https://github.com/clue/docker-redis-benchmark


https://github.com/joeferner/redis-commander

