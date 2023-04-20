FROM registry.gitlab.com/alta3/planetexpress/ubuntu-base:22.04

# build with:  sudo docker build --tag ssh-ps .
# run with:    sudo docker run -d ssh-ps

ARG user=student
ARG pass=alta3

# create user, set password, make passwordless sudoer
RUN useradd --create-home --shell /bin/bash ${user}                                   && \
    install --directory --owner=${user} --group=${user} /home/${user}/.ssh            && \
    echo "${user}:${pass}" | chpasswd                                                 && \
    echo "export LC_ALL=C" >> /home/${user}/.bashrc                                   && \
    echo "${user}       ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers                      && \
    mkdir -p /var/run/sshd                                                            && \
    echo "${user}       ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
