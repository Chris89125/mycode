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
DOCKERFILE=$HOME/px/dockerfiles/2204/staff

### Create networks
sudo docker network create --opt com.docker.network.driver.mtu=1450 --subnet 10.10.2.0/24 ansible-net

### Build docker images
sudo docker build -q --build-arg user=bender      --tag bender:22.04          $DOCKERFILE
sudo docker build -q --build-arg user=fry         --tag fry:22.04             $DOCKERFILE
sudo docker build -q --build-arg user=zoidberg    --tag zoidberg:22.04        $DOCKERFILE
sudo docker build -q --build-arg user=indy        --tag indy:22.04            $DOCKERFILE

### Launch containers and connect networks
sudo docker run -d  --name indy        -h indy       --ip 10.10.2.2 --network ansible-net indy:22.04
sudo docker run -d  --name bender      -h bender     --ip 10.10.2.3 --network ansible-net bender:22.04
sudo docker run -d  --name fry         -h fry        --ip 10.10.2.4 --network ansible-net fry:22.04
sudo docker run -d  --name zoidberg    -h zoidberg   --ip 10.10.2.5 --network ansible-net zoidberg:22.04
sudo docker run -d  --name farnsworth  -h farnsworth --ip 10.10.2.6 --network ansible-net registry.gitlab.com/alta3/planetexpress/centos/farnsworth:8

sudo apt install sshpass -y

echo -e ".ansible.cfg Updated (/home/student/.ansible.cfg)"
curl https://static.alta3.com/projects/ansible/deploy/ansiblecfg --create-dirs -o ~/.ansible.cfg

echo -e "Inventory File Updated (/home/student/mycode/inv/dev/hosts)"
curl https://static.alta3.com/projects/ansible/deploy/hosts --create-dirs -o ~/mycode/inv/dev/hosts

echo -e "Nethosts Inventory File Updated (/home/student/mycode/inv/dev/nethosts)"
curl https://static.alta3.com/projects/ansible/deploy/nethosts --create-dirs -o ~/mycode/inv/dev/nethosts

ansible-playbook ~/px/scripts/px-access.yml -i ~/mycode/inv/dev/hosts
