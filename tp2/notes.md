# Notes - TP2

## Exercice 1

1. `tcpdump arp` :  Afficher toutes les trames en rapport avec le protocole réseau ARP. (Résolution d'adresse MAC vers IP)
2. `tcpdump icmp` : Afficher toutes les trames en rapport avec le protocole réseau ICMP. (Typiquement les pings)
3. `tcpdump ip` : Afficher toutes les trames du protocole réseau IP  (l'essentiel des trames applicatives)
4. `tcpdump ’ether host 00:10:20:41:5A:F0’` : Affiche toutes les trames qui ont comme source ou destination l'adresse MAC spécifiée.
5. `tcpdump ’ip src 192.168.56.1’` : Affiche toutes les trames IP qui ont comme source l'adresse IP spécifée.
6. `tcpdump ’ip dst 192.168.56.200’` : Affiche toutes les trames IP qui ont comme destination l'adresse IP spécifée.
7. `tcpdump ’tcp port 22’` : Affiche toutes les trames TCP qui sont envoyées ou reçues sur le port 22. (Typiquement les connections SSH).
8. `tcpdump ’udp port domain or tcp port http’` : Affiche toutes les trames UDP envoyées ou reçues sur le port DNS (53), et toutes les trames TCP envoyées ou reçues sur le port HTTP (80).

## Exercice 2 

### Question 1

> Afficher les paquets d’un ping (requête et réponse) en visant précisément les éléments de protocole impliqués (c’est-à-dire les octets et les valeurs correspondants).

Le filtre correspondant est `tcpdump 'icmp[0] == 0x08 or icmp[0] == 0x00'`.

### Question 2

> Isoler les datagrammes UDP dont le port destination est compris entre 33434 et 33534 ainsi que les trames ICMP *port unreachable* et *ttl expired*. Comment peut-on tester simplement si le filtre fonctionne ? A quoi correspond ce trafic ?

Le filtre correspondant est `tcpdump '(udp[2:2] >= 0x829a && udp[2:2] <= 0x82fe) || icmp[0] == 0x0b' ||  icmp[0] == 0x03'`.

Ce trafic correspond à la réponse de routeurs qui ne peuvent pas atteindre leur destination. Un manière simple de générer le trafic est de faire un traceroute vers un routeur suffisemment éloigné.

### Question 3

> Voir les connexions HTTP initiées vers 193.0.6.139 (connexion = uniquement le premier paquet TCP)(indice : utiliser les offset et les masques)

Le filtre correspondant est `sudo tcpdump 'tcp[13:2]&0x2 == 0x00 && tcp port http && ip src 193.0.6.139'`.

### Question 4

> Afficher toutes les trames Ethernet issues d’une interface réseau dont l’O.U.I. (Organizationally Unique Identifier) est donné AB:CD:EF et à destination de l’adresse de diffusion

Le filtre correspondant est `sudo tcpdump 'ether dst ff:ff:ff:ff:ff:ff && ether[0:2] == 0xabcd && ether[2:1] == 0xef'`.

## Exercice 3

> Quelle est l’adresse IP de l’attaquant ?

L'addresse IP de l'attaquant est `192.168.0.9`.

> Quelle est l’adresse IP de destination?

L'addresse IP de destination est `192.168.0.99`.

> Plusieurs méthodes de scan différentes ont été utilisées. Quelles sont-elles ? Expliquer comment chacune d’elle fonctionne.

L'attaque commence par un ping, sans doute pour tester si la cible est accessible ou pas. 

Ensuite il tente sur tout les ports d'initier une connection (SYN, resize de fenêtre, puis fermeture). En analysant la réponse il est capable de savoir si le port est ouvert ou non. 

Ensuite il tente des choses similaire en faisant retransmettre son message depuis une autre IP. L'idée est de savoir si il existe une relation de confiance entre deux machines.

> Quel outil de scan a été utilisé ? Comment avez-vous fait pour le déterminer ?

Je pense que c'est Nmap. Cette technique d'envoyer des flags SYN+ACK est similaire à celle de mes expérimentations locales.

> Quel est le but du scan de port ?

Cela permet de savoir quels sont les services qui tournent sur la machine, et possiblement leur version. Cela pourra permettre d'envisager une attaque sur les vulnérabilités connues du service.

> Quels sont les ports qui sont ouverts sur la destination ?

Les ports ouverts semblent être 22, 53, 80, 111, 443, 32768.

> Quel système d’exploitation a été utilise ?

Cela semble être un linux. Le délais des 6 retransmissions sont de 4, 6, 12, 24 et 48 après un SYN/ACK sur un port ouverts. Ce qui est caractéristique d'un OS linux.

## Exercice 4

> Comment détecter qu’un scan est en cours sur une machine ?

Pour détecter qu'un scan est en cours sur une machine, on va utiliser une technique par seuil de détection. On va stocker les demande de connections entrantes sans aboutissement, et si ce nombre est trop élevé provenant de la même IP en un temps trop court, on déclanchera une alerte.

> Quelle structure de données utiliser?

La structure de données pertinante est une hashmap. Cela permettra de stocker, pour chaque IP, toutes les demandes de connection. 

> Proposer un algorithme avec un seuil de détection.

```
list_connection_non_abouties = {}
for connection in connections:
	if connection is connection_aboutie:
		continue
	connection[connection.ip].append(connection)
	
for conn_ip in list_connection_non_abouties:
	if len(conn_ip) > seuil * temps_ecoule:
		print(Scan supposé !)
```

> Implémenter cet algorithme dans le langage de votre choix.

```python
from collections import defaultdict 
import sys

import scapy.all as scapy

# Limite de connexions non abouties par secondes avant de considérer qu'il s'agit d'un scan
LIMIT = 5

# Fonction qui renvoie la liste de toutes le connections non abouties
def get_unfinished_connections(packets):
	return [packet for packet in packets if packet.haslayer(scapy.TCP) and packet['TCP'].flags & 0x04]

# Fonction qui renvoie le dictionnaire des ips qui ont envoyé des paquets TCP
def packet_to_ip_list(packets):
	ips = defaultdict(int)
	for packet in packets:
		ip = packet['IP'].src
		ips[ip] += 1

	return ips

if __name__	== "__main__":

	if len(sys.argv) != 2:
		print("Usage : python3 scan-detect.py <pcap_file>")
		exit(1)

	# On ouvre le fichier pcap
	packets = scapy.rdpcap(sys.argv[1])

	# On calcule le temps écoulé entre le premier et le dernier paquet
	time_elapsed = packets[-1].time - packets[0].time

	# On filtre pour garder uniquement les connexions TCP non abouties
	packets = get_unfinished_connections(packets)

	# On fait la liste des ips qui ont tentées des connexions TCP non abouties
	ips = packet_to_ip_list(packets)

	# On regarde si le nombre de connexions non abouties est supérieur à la limite
	ips_scan = [ip for ip in ips if ips[ip] > LIMIT * time_elapsed]

	# On affiche les ips qui ont fait un scan
	for ip in ips_scan:
		print("Scan possible from " + ip + " !")

```

> Votre programme doit pouvoir lire un fichier pcap. Tester le fichier pcap du point précédent sur votre programme.
