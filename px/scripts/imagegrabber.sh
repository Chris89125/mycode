#!/bin/bash

mkdir -p ~/.config/dockerfiles/ansible/

wget https://static.alta3.com/projects/ansible/modules/ssh-bender.tar.gz -O ~/.config/dockerfiles/ansible/ssh-bender.tar.gz
wget https://static.alta3.com/projects/ansible/modules/ssh-farnsworth.tar.gz -O ~/.config/dockerfiles/ansible/ssh-farnsworth.tar.gz
wget https://static.alta3.com/projects/ansible/modules/ssh-fry.tar.gz -O ~/.config/dockerfiles/ansible/ssh-fry.tar.gz
wget https://static.alta3.com/projects/ansible/modules/ssh-zoidberg.tar.gz -O ~/.config/dockerfiles/ansible/ssh-zoidberg.tar.gz

cd ~/.config/dockerfiles/ansible
gunzip ssh-bender.tar.gz
gunzip ssh-fry.tar.gz
gunzip ssh-farnsworth.tar.gz
gunzip ssh-zoidberg.tar.gz
