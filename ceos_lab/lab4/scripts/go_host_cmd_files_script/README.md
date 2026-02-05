### How to use the script

```
todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab4/scripts/go_host_cmd_files_script$ ./run_cmds hostfile.txt admin admin
hosts: [leaf1a leaf1b leaf2 spine1 spine2]
leaf1a.cfg
[enable configure interface loopback69  description leaf1a   show interfaces loopback 69]
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {},
    {},
    {},
    {},
    {},
    {
      "interfaces": {
        "Loopback69": {
          "name": "Loopback69",
          "forwardingModel": "routed",
          "lineProtocolStatus": "up",
          "interfaceStatus": "connected",
          "hardware": "loopback",
          "interfaceAddress": [],
          "description": "leaf1a",
          "bandwidth": 0,
          "mtu": 65535,
          "l3MtuConfigured": false,
          "l2Mru": 0,
          "lastStatusChangeTimestamp": 1769908292.0489764
        }
      }
    }
  ]
}
leaf1b.cfg
[enable configure interface loopback69  description leaf1b   show interfaces loopback 69 ]
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {},
    {},
    {},
    {},
    {},
    {
      "interfaces": {
        "Loopback69": {
          "name": "Loopback69",
          "forwardingModel": "routed",
          "lineProtocolStatus": "up",
          "interfaceStatus": "connected",
          "hardware": "loopback",
          "interfaceAddress": [],
          "description": "leaf1b",
          "bandwidth": 0,
          "mtu": 65535,
          "l3MtuConfigured": false,
          "l2Mru": 0,
          "lastStatusChangeTimestamp": 1769908293.0955617
        }
      }
    },
    {}
  ]
}
leaf2.cfg
[enable configure interface loopback69  description leaf2  show interfaces loopback 69 ]
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {},
    {},
    {},
    {},
    {
      "interfaces": {
        "Loopback69": {
          "name": "Loopback69",
          "forwardingModel": "routed",
          "lineProtocolStatus": "up",
          "interfaceStatus": "connected",
          "hardware": "loopback",
          "interfaceAddress": [],
          "description": "leaf2",
          "bandwidth": 0,
          "mtu": 65535,
          "l3MtuConfigured": false,
          "l2Mru": 0,
          "lastStatusChangeTimestamp": 1769908293.8168898
        }
      }
    },
    {}
  ]
}
spine1.cfg
[  enable configure interface loopback69  description spine1  show interfaces loopback 69]
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {
      "interfaces": {
        "Loopback69": {
          "name": "Loopback69",
          "forwardingModel": "routed",
          "lineProtocolStatus": "up",
          "interfaceStatus": "connected",
          "hardware": "loopback",
          "interfaceAddress": [],
          "description": "spine1",
          "bandwidth": 0,
          "mtu": 65535,
          "l3MtuConfigured": false,
          "l2Mru": 0,
          "lastStatusChangeTimestamp": 1769908294.4603617
        }
      }
    }
  ]
}
spine2.cfg
[enable configure interface loopback69  description spine2   show interfaces loopback 69  ]
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {},
    {},
    {},
    {},
    {},
    {
      "interfaces": {
        "Loopback69": {
          "name": "Loopback69",
          "forwardingModel": "routed",
          "lineProtocolStatus": "up",
          "interfaceStatus": "connected",
          "hardware": "loopback",
          "interfaceAddress": [],
          "description": "spine2",
          "bandwidth": 0,
          "mtu": 65535,
          "l3MtuConfigured": false,
          "l2Mru": 0,
          "lastStatusChangeTimestamp": 1769908294.7915113
        }
      }
    },
    {},
    {}
  ]
}
todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab4/scripts/go_host_cmd_files_script$ 
```
