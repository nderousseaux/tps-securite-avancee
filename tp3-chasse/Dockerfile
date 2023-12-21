# Ecrivez un fichier `Containerfile` en partant de l'image **ubuntu:14.04** et en installant les paquets suivants: `python python-scapy telnet tcpdump tmux vim dsniff nmap`.
# Vous pouvez ensuite ajouter les fichiers `ChasseEnTerreInconnue.py` et `conf.py` (depuis moodle).

FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python python-scapy telnet tcpdump tmux vim dsniff nmap

WORKDIR /root

COPY ChasseEnTerreInconnue.py ChasseEnTerreInconnue.py
COPY conf.py conf.py
COPY pytransform pytransform


# Always up
CMD ["tail", "-f", "/dev/null"]


# Docker build
# docker build -t tp3-secu .


# Docker run
# docker run --privileged --device /dev/net/tun tp3-secu
