# File Timeline – HANDS-ON

Booting a Virtual Machine on a live system, you will acquire data and extract a file timeline to determine what simple action was done on the system.

## Starting the VM

Import the Alpine Linux virtual machine provided in Directory "file_timeline" ;

You should configure the VM to boot on the ISO image.

## Setup

Once the system has booted on the ISO image, log in as root (no password) and select the correct keyboard with the command "setup-keymap" (fr, fr) ; Setup the network interface (setup-interfaces ; default answers ; ifup eth0)

## Acquire the image

Using the same procedure as in previous exercice, «data acquisition », copy the root partition (/dev/sda3) on the host system. MD5 checksum should be 6e5b7c2d9ab4f6a169d0e58cc844e0ad

## Questions

1. Extract the list of files/MAC/timestamps with the fls command. Which command did you use ?

```bash
$ fls -r -m / part.raw > timeline.fls
```

2. Convert the fls output with the mactime command. Which command and options did you use ?

```bash
$ mactime -b timeline.fls > timeline.mactime
```

3. Using the mactime output, determine what action was done on the system. Which element in the mactime filesystem timeline demonstrate your hypothese ?

```
Beaucoup de choses ont été faites sur vsftpd. Un restart, un accès, etc... En checkant les logs de vsftpd, on constate que l'utilisateur à téléchargé un fichier.
```

The starting point of the analysis is 2016/06/21 21:26 local time

You can mount the image read-only to gather other information to support your analysis.