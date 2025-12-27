Integrated Routing and Bridging (IRB)
- This was confusing to set up as the sr linux does not have vlan interfaces.
- irb interface needs to be created
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
