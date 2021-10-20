#!/bin/bash
set -e
set -x

# Build

CAL_VER=$(TZ=America/New_York date '+%Y-%m-%d')
echo 'Docker Build Python'
# build all
docker build -t mikeryan56/bpm:7.16-$CAL_VER -f dockerfile .
docker tag mikeryan56/bpm:7.16-$CAL_VER mikeryan56/bpm:latest
#build rest only
docker build -t mikeryan56/bpm:7.16-rest-$CAL_VER -f dockerfile-rest .
#build rest & swagger
docker build -t mikeryan56/bpm:7.16-rest-swagger-$CAL_VER -f dockerfile-rest-swagger .

# docker push
docker push mikeryan56/bpm:7.16-$CAL_VER
docker push mikeryan56/bpm:7.16-rest-$CAL_VER
docker push mikeryan56/bpm:7.16-rest-swagger-$CAL_VER
docker push mikeryan56/bpm:latest

# docker run mikeryan56/bpm:7.16-$CAL_VER