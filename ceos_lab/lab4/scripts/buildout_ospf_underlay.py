#!/usr/bin/python3.12

import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

leaf1a_cfg = """
enable
configure
ip routing

interface loopback0
 description RtrID
 ip address 1.1.1.1/32

interface Loopback1
 description Lo1 for VTEP
 ip address 1.1.1.101/32


interface Eth49
  no switchport
  ip address 10.1.0.1/31


router ospf 1
 router-id 1.1.1.1
 network 1.1.1.1 0.0.0.0 area 0
 network 1.1.1.101 0.0.0.0 area 0
 network 10.1.0.0 0.0.0.1 area 0

"""




leaf1b_cfg = """
enable 
configure
ip routing

interface loopback0
 description RtrID
 ip address 1.1.1.2/32

interface Loopback1
 description Lo1 for VTEP
 ip address 1.1.1.102/32


interface Eth49
  no switchport
  ip address 10.1.0.3/31

router ospf 1
 router-id 1.1.1.2
 network 1.1.1.2 0.0.0.0 area 0
 network 1.1.1.102 0.0.0.0 area 0
 network 10.1.0.2 0.0.0.1 area 0

"""

leaf2_cfg = """
enable 
configure
ip routing

interface loopback0
 description RtrID
 ip address 1.1.1.3/32

interface Loopback1
 description Lo1 for VTEP
 ip address 1.1.1.103/32

 
interface Eth1
  no switchport
  ip address 10.1.0.5/31

interface Eth2
  no switchport
  ip address 10.1.0.7/31


router ospf 1
 router-id 1.1.1.3
 network 1.1.1.3 0.0.0.0 area 0
 network 1.1.1.103 0.0.0.0 area 0
 network 10.1.0.4 0.0.0.1 area 0
 network 10.1.0.6 0.0.0.1 area 0

"""

spine1_cfg = """
enable 
configure
ip routing

interface loopback0
  description RtrID
  ip address 100.100.100.1/32

interface Eth3
  no switchport
  ip address 10.1.0.0/31

interface Eth4
  no switchport
  ip address 10.1.0.4/31

router ospf 1
 router-id 100.100.100.1
 network 100.100.100.1 0.0.0.0 area 0
 network 10.1.0.0 0.0.0.1 area 0
 network 10.1.0.4 0.0.0.1 area 0


"""

spine2_cfg = """
enable 
configure
ip routing

interface loopback0
 description RtrID
 ip address 100.100.100.2/32
 
interface Eth3
  no switchport
  ip address 10.1.0.2/31

interface Eth4
  no switchport
  ip address 10.1.0.6/31

router ospf 1
 router-id 100.100.100.2
 network 100.100.100.2 0.0.0.0 area 0
 network 10.1.0.2 0.0.0.1 area 0
 network 10.1.0.6 0.0.0.1 area 0
 
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
