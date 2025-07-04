#!/bin/bash
# Assign underlay IP
ip addr add 192.168.0.1/24 dev eth1
ip link set eth1 up

# Create bridge
ip link add br0 type bridge
ip link set br0 up

# Add host interface to bridge
ip link set eth2 up
ip link set eth2 master br0

# Create VXLAN
ip link add vxlan100 type vxlan id 100 dstport 4789 dev eth1 remote 192.168.0.2
ip link set vxlan100 up
ip link set vxlan100 master br0

# Add IP to bridge (GW for hosts)
ip addr add 10.0.0.1/24 dev br0
