#!/bin/bash

docker build -f ./Dockerfile.txt -t myflask .

docker run -d -p 5000:5000 --name myflask myflask