# Détail de l'attaque

> ***<u>Consignes :</u>*** 4 parties à la présentation : 
>
> 1. Task specification
> 2. Analysis description
> 3. Conclusions
> 4. Free discussion
>
> Le présentation doit être compréhensible, neutre et répetable.

## Contexte

Un client maintient à serveur FTP à Paris. Sur un système Alpine Linux

Le 10 Juin, le client veux télécharger des fichiers, et constate qu'il y a des photos étranges dans `/home/jean/photos`.  Il c'est immédiatement loggé en tant que root et à coupé le serveur à 14h23.

##  Déroulé de l'attaque

### Etape 1 : Intrusion via brute force ssh

À `12:26`, une addresse ip interne au réseau (`192.168.1.5`) tente des connections ssh sur notre serveur via le port `41702`. Il va essayer avec les utilisateurs `admin`, `service`et `root`. Au bout de seulement quelques essais, il va réussir à trouver le mot de passe root.

### Etape 2 : Sécurisation de l'accès

Ensuite, l'attaquant sécurise ses accès en inscrivant sa clé publique dans les clés autorisées des utilisateurs `root`, `MeowKitty` (qu'il aura crée) et `jean`.

### Etape 3 : Ajout de documents via FTP

L'attaquant va modifier le fichier `vsftpd.conf` afin de pouvoir uploader n'importe quel fichier sans autorisation.

Une fois fait, il va mettre 7 photos dans le répertoire photos de jean : 

- `/home/jean/photos/freedom_for_cat.jpg`
- `/home/jean/photos/hack-me.jpg`
- `/home/jean/photos/hacker_meow_in_action.png`
- `/home/jean/photos/hackykitty.jpg`
- `/home/jean/photos/kittylogger.jpg`
- `/home/jean/photos/meow_wins.jpg`
- `/home/jean/photos/we_will-we_will-hack_you!.jpg`

### Etape 4 : Modification du système

À `12:29` il va lancer un script, stocké dans `/lib/apk/db/scripts.tar`. Ce script va modifier le chemin de certains binaire critique : `/usr/bin/passwd` ou `/usr/bin/su`. Il va les faires pointer vers une toolbox embarquée `busybox` sans doute une version modifié. C'est surement un rootkit. 