Coté receveur : `nc -l -p <port> > file.iso`
Coté sender : `dd if=<partition> | nc <ip-receveur> <port>


50892c253a482afacecd9a31342e220c5c27d5a55ad73ab597a537064496fd0c  file.iso

monter une image iso
mkdir /media/part
sudo mount -o loop,ro,noatime,noauto file.iso /media/part