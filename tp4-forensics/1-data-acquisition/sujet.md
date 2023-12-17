
# Data Acquisition – HANDS-ON

You will acquire data from a virtual machine. This VM, running Alpine Linux, has a small virtual disk (less than 1 Gb) ; you will acquire the root file system of this disk.

## Starting the VM

Import the Alpine Linux virtual machine provided in directory "Data Acquisition" located on the Desktop; **DO NOT START THE VM YET !**

Before starting it, add the Alpine Linux ISO as a virtual CD.

The system will boot automatically on the ISO image. Booting on an separate media is mandatory to avoid pertubation from acquiring data on a live system.

## Setup

Once the system has booted on the ISO image, log in as root (no password). 

The default keyboard layout is « US ». If you are confortable with, keep it. If not, select the keyboard layout with the command *setup-keymap* and choose (fr, fr) if you want the layout to match the keyboard.

Configure the network by doing **setup-interfaces** (all default choices : eth0, dhcp, no) and activate the interface with *ifup eth0*

## Identify disk and partitions

List the disks with the command "fdisk -l" and identify the root partition (the largest one)

## Acquire the disk image of the root partition :

- start receiving process (nc) on the host,

- start acquisition process (dd… | nc...) on the guest

## Checksum generation & verification

- Calculate the checksum of your image

- give access to image & checksum to your neighbour
- copy the image of your neighbour and verify its checksum : it should be the same

## Mount the image read-only and explore the image (don't forget to use the « -o loop,ro,noatime,noauto » of mount)