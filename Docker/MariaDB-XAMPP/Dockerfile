FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    sudo \
    software-properties-common \
    mariadb-server \
    net-tools \
    && apt-get clean

RUN wget https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run \
    && chmod +x xampp-linux-x64-8.2.12-0-installer.run \
    && ./xampp-linux-x64-8.2.12-0-installer.run --mode unattended

EXPOSE 80 3306

CMD ["bash", "-c", "/opt/lampp/lampp start && tail -f /dev/null"]

