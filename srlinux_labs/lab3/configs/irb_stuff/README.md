Integrated Routing and Bridging (IRB)
- This was confusing to set up as the sr linux does not have vlan interfaces.
- Need to use irb and connect it to both the Layer 2 mac-vrf and Layer 3  ip-vrf network-instances 
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

- You also need to add the interfaces to network-instance default that is mac-vrf (bridging part of the IRB interface)
```
    {
      "name": "default",
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
```
- Lastly you need to associate the routing portion to the IRB so you create a new network-instance and associate ip-vrf
```
    {
      "name": "L3default",
      "type": "ip-vrf",
      "admin-state": "enable",
      "interface": [
        {
          "name": "irb10.0"
        }
      ]
    }

```
