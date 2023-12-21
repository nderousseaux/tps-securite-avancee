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
	


