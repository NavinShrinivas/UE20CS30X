FROM debian:buster-slim
RUN \ 
apt upgrade -y && \
apt -y update && \
apt install -y sudo vim neovim neofetch 
RUN useradd -rm -d /home/containeruser -s /bin/bash  -G sudo containeruser
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN echo 'root:root' | chpasswd
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN echo 'containeruser:root' | chpasswd
USER containeruser
WORKDIR /home/containeruser
