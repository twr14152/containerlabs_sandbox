#!/bin/sh
#

#gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure get \
#  --path "/system/config/hostname" \
#  --encoding json_ietf

#gnmic -a clab-lab3-ceos2:6030 -u admin -p admin --insecure get \
#  --path "/system/config/hostname" \
#  --encoding json_ietf

#gnmic -a clab-lab3-ceos3:6030 -u admin -p admin --insecure get \
#  --path "/system/config/hostname" \
#  --encoding json_ietf

#gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure subscribe \
#  --path "/interfaces/interface[name=Ethernet1]/state/counters" \
#  --encoding json_ietf \
#  --mode stream \
#  --stream-mode sample \
#  --sample-interval 5s

#not working
#gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure path \
#  --model openconfig-interfaces

#list capabilities
#gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure capabilities

#list all interfaces
#gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure get \
#  --path "/interfaces/interface" \
#  --encoding json_ietf

#save the capabilities to a different file
#gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure capabilities > ceos1_capabilities.json

#putting it all together to gather streaming data from interface Ethernet1
#gnmic subscribe \
# -a clab-lab3-ceos1:6030 -u admin -p admin --insecure \
# --path "/interfaces/interface[name=Ethernet1]/state/counters" \
# --mode stream \
# --stream-mode sample \
# --sample-interval 5s \
# --encoding json_ietf

#Check all bgp  status
#gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure get \
#  --path "/network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors" \
#  --encoding json_ietf

#check bgp neighbor status
#gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure get \
#  --path "/network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=10.0.0.2]/state" \
#  --encoding json_ietf


#query for ospf neighbors | not working
#gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure get \
#  --path "/network-instances/network-instance[name=default]/protocols/protocol[identifier=OSPF][name=OSPF]/ospfv2/neighbors" \
#  --encoding json_ietf

#troubleshooting step to get ospf data
#gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure get \
#  --path "/network-instances/network-instance[name=default]/protocols/protocol[identifier=OSPF][name=OSPF]/ospfv2" \
#  --encoding json_ietf

#shits not working
#gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure get \
#  --path "/network-instances/network-instance[name=default]/protocols/protocol[identifier=OSPF][name=OSPF]/ospfv2" \
#  --encoding json_ietf 

#This didn't work either
gnmic -a clab-lab3-ceos1:6030 -u admin -p admin --insecure cli -f enable_bfd.cli
gnmic -a clab-lab3-ceos2:6030 -u admin -p admin --insecure cli -f enable_bfd.cli

