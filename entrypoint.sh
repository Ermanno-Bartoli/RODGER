#!/bin/bash

# First fix the nameserver on the container
echo nameserver $DNS_IP > /etc/resolv.conf

# Fix the gateway
ip route del default
ip route add default via $GATEWAY_IP

# run pfm server
# pfm > /proc/1/fd/1 2>&1 &

# setup sshd
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# useradd -m -s /bin/bash $USER
# usermod -aG sudo $USER
echo "root:${PASS}" | chpasswd

# run ssh server
service ssh start

sleep infinity;
