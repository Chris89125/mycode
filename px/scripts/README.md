dockerfiles for simple lab containers


1. Find the docker file you want, and build a new image (with a tag). 

`sudo docker build -q --build-arg user=bender     --tag ssh-bender     $HOME/.config/dockerfiles/ansible/ssh-ks`

2. Once that is done, save the image. 

`sudo docker save ssh-bender:latest | gzip > ssh-bender.tar.gz`

3. Push the image up to the correct location (might have to go through some hoops here since we did this on the student machine)

`scp ~/ssh-bender.tar.gz website:/var/www/html/static.alta3.com//projects/ansible/modules/`

4. Update the pexpress-setup.sh script for testing the new name and image, or test this manually as such. (You can use an extra student machine).

`sudo docker network create --opt com.docker.network.driver.mtu=1450 --subnet 10.10.2.0/24 ansible-net`

`sudo docker build -q --build-arg user=bender     --tag ssh-bender     $HOME/.config/dockerfiles/ansible/ssh-ks`    #(using the right ssh- file)  

FILE_PATH=$HOME/.config/dockerfiles/ansible  

`sudo docker image load -i $FILE_PATH/ssh-bender.tar`

`sudo docker run -d  --name bender      -h bender    ` --ip 10.10.2.3 --network ansible-net ssh-bender`
