FROM mcr.microsoft.com/devcontainers/python:3.12

# Install OpenSSH server
RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir -p /var/run/sshd && \
    ssh-keygen -A && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    echo 'root:pycharm' | chpasswd

EXPOSE 22 8000

CMD ["/usr/sbin/sshd", "-D"]