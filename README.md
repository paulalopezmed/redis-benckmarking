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
### Benchmark executation in Google Cloud Platform

Build SUT and Client in order. Obtain the result with the process is finiched. Execute the finish file when the benchmark is finished


#### Build and run of Redis (in Google Cloud Platform)

``` bash 
chmod +x startRedis.sh
./startRedis.sh
```

#### Build and run of Client (in Google Cloud Platform)

``` bash 
chmod +x startClient.sh
./startClient.sh
```
#### Retrieve the CSV output file of the benchmark

``` bash 
chmod +x getResults.sh
./getResults.sh
```

#### Delete instance of Redis (in Google Cloud Platform)

``` bash 
chmod +x finishRedis.sh
./finishClient.sh
```

#### Delete instance of Client (in Google Cloud Platform)

``` bash 
chmod +x finishClient.sh
./finishClient.sh
```

## Documentation used

https://github.com/clue/docker-redis-benchmark


https://github.com/joeferner/redis-commander

