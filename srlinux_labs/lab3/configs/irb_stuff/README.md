Integrated Routing and Bridging (IRB)
- This was confusing to set up as the sr linux does not have vlan interfaces.
- Need to use irb and connect it to both the Layer 2 mac-vrf and Layer 3  ip-vrf network-instances or default network-instance
- irb interface needs to be created
  ```
   "result": [
    {
      "name": "irb10",
      "admin-state": "enable",
      "subinterface": [
        {
          "index": 0,
          "admin-state": "enable",
          "ipv4": {
            "admin-state": "enable",
            "address": [
              {
                "ip-prefix": "192.168.101.1/24"
              }
            ]
          }
        }
      ]
    }
  ],
  ```
- host ports participating need interface vlan tagging set to false , and to be type bridged
    ```
    "name": "ethernet-1/11",
    "admin-state": "enable",
      "vlan-tagging": false,
      "subinterface": [
        {
          "index": 0,
          "type": "bridged",
          "admin-state": "enable"
    ```

- You also need to add the interfaces to network-instance that is mac-vrf (bridging part of the IRB interface)
```
  Connecting to leaf1
200
{
  "result": [
    {
      "name": "bridging_netwk",
      "type": "mac-vrf",
      "admin-state": "enable",
      "interface": [
        {
          "name": "ethernet-1/10.0"
        },
        {
          "name": "ethernet-1/11.0"
        },
        {
          "name": "ethernet-1/12.0"
        },
        {
          "name": "irb10.0"
        }
      ],
      "bridge-table": {
        "mac-learning": {
          "admin-state": "enable"
        }
      }
    }
  ],
  "id": 1,
  "jsonrpc": "2.0"
}
```
- Lastly you need to associate the routing portion to the IRB to network-instance default
```
   Connecting to leaf1
200
{
  "result": [
    {
      "name": "default",
      "type": "default",
      "admin-state": "enable",
      "interface": [
        {
          "name": "ethernet-1/1.0"
        },
        {
          "name": "ethernet-1/2.0"
        },
        {
          "name": "irb10.0"
        },
        {
          "name": "lo0.0"
        }
      ],
      "protocols": {
        "bgp": {
          "admin-state": "enable",
          "autonomous-system": 65001,
          "router-id": "1.1.1.1",
          "ebgp-default-policy": {
            "import-reject-all": false,
            "export-reject-all": false
          },
          "afi-safi": [
            {
              "afi-safi-name": "ipv4-unicast",
              "admin-state": "enable"
            }
          ],
          "group": [
            {
              "group-name": "spine",
              "peer-as": 64999,
              "export-policy": [
                "advertise-local"
              ]
            }
          ],
          "neighbor": [
            {
              "peer-address": "10.1.1.0",
              "peer-group": "spine"
            },
            {
              "peer-address": "10.2.1.0",
              "peer-group": "spine"
            }
          ]
        }
      }
    }
  ],
  "id": 1,
  "jsonrpc": "2.0"
}
```
