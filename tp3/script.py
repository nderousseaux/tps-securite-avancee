# Use scapy for port knocking

from scapy.all import *

# Define the target IP
target = "10.5.0.6"

# Define the ports to knock
ports = [951, 951, 4826, 443, 100, 21]

# Send the SYN packet
for port in ports:
		send(IP(dst=target)/TCP(dport=port, flags="S"))
		print("Sent SYN packet to port " + str(port))

