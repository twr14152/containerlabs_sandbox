Integrated Routing and Bridging (IRB)
- This was confusing to set up as the sr linux does not have vlan interfaces.
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

- You also need to add the interfaces to network-instance default that is mac-vrf
```
