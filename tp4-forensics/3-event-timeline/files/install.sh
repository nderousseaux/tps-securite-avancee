#!/bin/bash

# Deps installable as packages
apt install -y libdatetime-perl libnet-pcap-perl libarchive-any-perl libxml-libxml-perl libdbi-perl libhtml-scrubber-perl libimage-exiftool-perl libgtk2-perl libglib-perl libcarp-assert-perl libdbd-sqlite3-perl libdigest-crc-perl libversion-perl libdate-manip-perl perl-modules cpanminus
# Rest of the deps through CPAN
cpanm Data::Hexify File::Mork Mac::PropertyList NetPacket::Ethernet NetPacket::IP NetPacket::TCP NetPacket::UDP Parse::Win32Registry DateTime::Format::Strptime

# Source
wget https://launchpad.net/~sift/+archive/ubuntu/stable/+sourcefiles/log2timeline-perl/0.663-1ubuntu1/log2timeline-perl_0.663.orig.tar.gz
tar xf log2timeline-perl_0.663.orig.tar.gz
cd log2timeline
sed -i '/CMI-CreateHive/s/[{}]/\\&/g' lib/Log2t/input/ntuser.pm lib/Log2t/input/sam.pm
perl Makefile.PL
make
make install
ln -s /usr/local/bin/log2timeline_legacy /usr/local/bin/log2timeline
