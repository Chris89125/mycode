FROM centos:latest 

# build with:  sudo docker build 
# run with:    sudo docker run -d 

ARG user=farnsworth
ARG pass=alta3

RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-*                                            && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*

RUN yum -y update                                                                                             && \
    yum install -y epel-release                                                                               && \
    yum install -y jq curl sudo vim openssh-server man less python39 git                                      && \
    mkdir -p /var/run/sshd                                                                                    && \
    echo "AllowAgentForwarding yes" >> /etc/ssh/sshd_config

# create user, set password, make passwordless sudoer, add authorized key
RUN useradd --create-home --shell /bin/bash ${user}                                                           && \
    install --directory --owner=${user} --group=${user} /home/${user}/.ssh                                    && \
    echo "${user}:${pass}" | chpasswd                                                                         && \
    echo "export LC_ALL=C" >> /home/${user}/.bashrc                                                           && \
    echo "${user}       ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN rm /var/run/nologin
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' 

# allow root ssh with password and set password
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config                    && \
    echo "root:${pass}" | chpasswd

EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]
