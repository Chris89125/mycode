#!/bin/bash


echo -e "Cleaning up Containers..."
sudo docker stop john paul george stuart pete ringo &> /dev/null
sudo docker rm john paul george stuart pete ringo &> /dev/null
sudo docker network rm ansible-net &> /dev/null
rm /tmp/labrunning &> /dev/null

sudo docker stop indy &> /dev/null
sudo docker rm indy &> /dev/null
sudo docker network rm ansible-net &> /dev/null
rm /tmp/labrunning &> /dev/null

sudo docker stop bender fry zoidberg farnsworth indy &> /dev/null
sudo docker rm bender fry zoidberg farnsworth indy &> /dev/null
sudo docker network rm ansible-net &> /dev/null
rm /tmp/labrunning &> /dev/null
echo -e "Containers Cleared!\n"

echo -e "Assembling Planet Express team...\n"

### Set ARGS
SSH_PUB_KEY="$(cat ~/.ssh/id_rsa.pub)" 
DOCKERFILE=$HOME/planet-express/dockerfiles/2204/staff
CENT_DOCKERFILE=$HOME/planet-express/dockerfiles/centos

### Create networks
sudo docker network create --opt com.docker.network.driver.mtu=1450 --subnet 10.10.2.0/24 ansible-net

### Build docker images
sudo docker build -q --build-arg user=bender      --build-arg $SSH_PUB_KEY  --tag bender:22.04          $DOCKERFILE
sudo docker build -q --build-arg user=fry         --build-arg $SSH_PUB_KEY  --tag fry:22.04             $DOCKERFILE
sudo docker build -q --build-arg user=zoidberg    --build-arg $SSH_PUB_KEY  --tag zoidberg:22.04        $DOCKERFILE
sudo docker build -q --build-arg user=farnsworth                            --tag farnsworth:centos8    $CENT_DOCKERFILE

### Launch containers and connect networks
sudo docker run -d  --name bender      -h bender     --ip 10.10.2.3 --network ansible-net bender
sudo docker run -d  --name fry         -h fry        --ip 10.10.2.4 --network ansible-net fry
sudo docker run -d  --name zoidberg    -h zoidberg   --ip 10.10.2.5 --network ansible-net zoidberg
sudo docker run -d  --name farnsworth  -h farnsworth --ip 10.10.2.6 --network ansible-net farnsworth

printf "
             ______ 
             |___ /  
               |_ \            .
              ___) |          ==
             |____/           ===
       /"""""""""""""""""\___/ ===
      {       Complete!       /  ===-
       \______ O           __/
         \    \         __/
          \____\_______/

"


