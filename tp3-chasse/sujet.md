# Chasse en terre inconnue

Dans bien des situations il arrive de travailler dans un environnement non documenté, et donc très opaque.
Vous allez devoir trouver un fichier caché sur une infrastructure émulée.

## Mise en place de l'infrastructure

Ecrivez un fichier `Containerfile` en partant de l'image **ubuntu:14.04** et en installant les paquets suivants: `python python-scapy telnet tcpdump tmux vim dsniff nmap`.
Vous pouvez ensuite ajouter les fichiers `ChasseEnTerreInconnue.py` et `conf.py` (depuis moodle).

Vous pouvez tester votre configuration en lançant un conteneur à partir de cette image avec les options `--privileged --device /dev/net/tun`, en exécutant le script `ChasseEnTerreInconnue.py`, vous devriez lire **La chasse est lancée**.
L'interface `tap0` sera la seule interface don vous aurez besoin.

Nous vous proposons l'utilisation de tmux afin de lancer plusieurs terminaux sur la même session.
L'ensemble du jeu de piste est faisable en ligne de commande, vous aurez besoin de la commande `macof` (cf https://www.monkey.org/~dugsong/dsniff/)

## Conclusions

Dans un petit rapport, vous expliquerez de façon chronologique les évènements et actions qui vous ont conduites au fichier caché.
