#!/usr/bin/python3.12

import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

leaf1a_cfg = """
enable
configure

interface Loopback1
 description Lo1 for VTEP
 ip address 1.1.1.101/32

interface Vxlan1
  vxlan source-interface Loopback1
  vxlan udp-port 4789
  vxlan vlan 20 vni 20020
  vxlan flood vtep 1.1.1.103

ip virtual-router mac-address 00:1c:73:00:00:99

interface Vlan20
   ip address 10.0.20.2/24
   ip virtual-router address 10.0.20.1

router bgp 65001
   router-id 1.1.1.1
   neighbor 100.100.100.1 remote-as 65000
   neighbor 100.100.100.1 update-source Loopback0
   neighbor 100.100.100.1 ebgp-multihop 5
   !
   vlan-aware-bundle VNI20
      rd 65000:20020
      route-target both 65000:20020
      redistribute learned
      vlan 20
   !
   address-family evpn
      neighbor 100.100.100.1 activate
   !
!


"""

leaf1b_cfg = """
enable 
configure

interface Loopback1
 description Lo1 for VTEP
 ip address 1.1.1.102/32

interface Vxlan1
  vxlan source-interface Loopback1
  vxlan udp-port 4789
  vxlan vlan 20 vni 20020
  vxlan flood vtep 1.1.1.103


ip virtual-router mac-address 00:1c:73:00:00:99

interface Vlan20
   ip address 10.0.20.3/24
   ip virtual-router address 10.0.20.1

router bgp 65001
   router-id 1.1.1.2
   neighbor 100.100.100.2 remote-as 65000
   neighbor 100.100.100.2 update-source Loopback0
   neighbor 100.100.100.2 ebgp-multihop 5
   !
   vlan-aware-bundle VNI20
      rd 65000:20020
      route-target both 65000:20020
      redistribute learned
      vlan 20
   !
   address-family evpn
      neighbor 100.100.100.2 activate
   !
!

"""

leaf2_cfg = """
enable 
configure

interface Loopback1
 description Lo1 for VTEP
  ip address 1.1.1.103/32

interface Vxlan1
  vxlan source-interface Loopback1
  vxlan udp-port 4789
  vxlan vlan 20 vni 20020
  vxlan flood vtep 1.1.1.101 

interface Vlan20
   ip address 10.0.20.4/24
   ip virtual-router address 10.0.20.1

ip virtual-router mac-address 00:1c:73:00:00:99

router bgp 65002
   router-id 1.1.1.3
   neighbor 100.100.100.1 remote-as 65000
   neighbor 100.100.100.1 update-source Loopback0
   neighbor 100.100.100.1 ebgp-multihop 5
   neighbor 100.100.100.2 remote-as 65000
   neighbor 100.100.100.2 update-source Loopback0
   neighbor 100.100.100.2 ebgp-multihop 5
   !
   vlan-aware-bundle VNI20
      rd 65000:20020
      route-target both 65000:20020
      redistribute learned
      vlan 20
   !
   address-family evpn
      neighbor 100.100.100.1 activate
      neighbor 100.100.100.2 activate
   !
!



"""

spine1_cfg = """
enable 
configure

router bgp 65000
   router-id 100.100.100.1
   neighbor 1.1.1.1 remote-as 65001
   neighbor 1.1.1.1 update-source Loopback0
   neighbor 1.1.1.1 ebgp-multihop 5
   neighbor 1.1.1.1 route-reflector-client
   neighbor 1.1.1.3 remote-as 65002
   neighbor 1.1.1.3 update-source Loopback0
   neighbor 1.1.1.3 ebgp-multihop 5
   neighbor 1.1.1.3 route-reflector-client
   !
   vlan-aware-bundle VNI20
      rd 65000:20020
      route-target both 65000:20020
      vlan 20
   !
   address-family evpn
      neighbor 1.1.1.1 activate
      neighbor 1.1.1.3 activate
   !

"""

spine2_cfg = """
enable 
configure

router bgp 65000
   router-id 100.100.100.2
   neighbor 1.1.1.2 remote-as 65001
   neighbor 1.1.1.2 update-source Loopback0
   neighbor 1.1.1.2 ebgp-multihop 5
   neighbor 1.1.1.2 route-reflector-client
   neighbor 1.1.1.3 remote-as 65002
   neighbor 1.1.1.3 update-source Loopback0
   neighbor 1.1.1.3 ebgp-multihop 5
   neighbor 1.1.1.3 route-reflector-client
   !
   vlan-aware-bundle VNI20
      rd 65000:20020
      route-target both 65000:20020
      vlan 20
   !
   address-family evpn
      neighbor 1.1.1.2 activate
      neighbor 1.1.1.3 activate
   !
!



"""

def config(host, cmds):
    url = f"https://{host}/command-api"
    print(f"Connected to {host}..")
    headers = {'Content-Type': 'application/json'}
    payload = {
            "jsonrpc": "2.0",
            "method": "runCmds",
            "params": {
                "version": 1,
                "cmds": cmds,
                "format": "json"
                },
            "id": "1"
            }
    response = requests.post(url, data=json.dumps(payload), auth=('admin', 'admin'), verify=False)
    print(json.dumps(response.json(), indent=2))        
    print(f"Closing connection to {host}...\n\n")


def to_list(cfg_string):
    return [line.strip() for line in cfg_string.splitlines() if line.strip()]


def main():
    #convert string to list
    leaf1a_cfg_list= to_list(leaf1a_cfg)
    leaf1b_cfg_list = to_list(leaf1b_cfg)
    leaf2_cfg_list = to_list(leaf2_cfg)
    spine1_cfg_list = to_list(spine1_cfg)
    spine2_cfg_list = to_list(spine2_cfg)
    
    config("leaf1a", leaf1a_cfg_list)
    config("leaf1b", leaf1b_cfg_list)
    config("leaf2", leaf2_cfg_list)
    config("spine1", spine1_cfg_list)
    config("spine2", spine2_cfg_list)
    print("End of script...")

if __name__ == "__main__":
    main()

