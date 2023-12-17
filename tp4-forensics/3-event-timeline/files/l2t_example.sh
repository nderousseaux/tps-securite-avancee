#!/bin/sh
#    log2timeline [OPTIONS] [-f FORMAT] [-z TIMEZONE] [-o OUTPUT MODULE] [-w BODYFILE] LOG_FILE/LOG_DIR [--] [FORMAT FILE OPTIONS]
rm -f l2t-utc.out
log2timeline -r -z Europe/Paris -Z UTC -e /var/log/messages -o mactime -w l2t-utc.out /mnt
