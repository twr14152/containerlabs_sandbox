### Build AI assisted Network Controller

This will be a phased build out. 

Goal is to use AI to translate cli output to controller. No yaml no json and certainly ***no yang***....

Current network is (2)spine(3)leaf network with three hosts one of each leaf.
The network is evpn/vxlan buildout.
Underlay is bgp.
Vlan20 is whats associated with the vni

First step in process enable telemetry.

To start enable username telemetry and password telemetry123 on all devices

```
todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab4/scripts$ ./run_cmds.py admin admin
Do you want to connect to all hosts?..(y/n):y
Do you have a config or cmds file to load (y/n): n
Enter commands to run seperated by ",": enable, configure terminal, username telemetry privilege 15 secret telemetry123, write
Connected to leaf1a..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {},
    {},
    {
      "messages": [
        "Copy completed successfully."
      ]
    }
  ]
}
Closing connection to leaf1a...


Connected to leaf1b..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {},
    {},
    {
      "messages": [
        "Copy completed successfully."
      ]
    }
  ]
}
Closing connection to leaf1b...


Connected to leaf2..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {},
    {},
    {
      "messages": [
        "Copy completed successfully."
      ]
    }
  ]
}
Closing connection to leaf2...


Connected to spine1..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {},
    {},
    {
      "messages": [
        "Copy completed successfully."
      ]
    }
  ]
}
Closing connection to spine1...


Connected to spine2..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {},
    {},
    {
      "messages": [
        "Copy completed successfully."
      ]
    }
  ]
}
Closing connection to spine2...


todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab4/scripts$ 

```

enable telemetry on all devices


Verify password works.
```
todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab4/scripts$ ./run_cmds.py telemetry telemetry123
Do you want to connect to all hosts?..(y/n):y
Do you have a config or cmds file to load (y/n): n
Enter commands to run seperated by ",": enable, show hostname
Connected to leaf1a..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {
      "hostname": "leaf1a",
      "fqdn": "leaf1a"
    }
  ]
}
Closing connection to leaf1a...


Connected to leaf1b..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {
      "hostname": "leaf1b",
      "fqdn": "leaf1b"
    }
  ]
}
Closing connection to leaf1b...


Connected to leaf2..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {
      "hostname": "leaf2",
      "fqdn": "leaf2"
    }
  ]
}
Closing connection to leaf2...


Connected to spine1..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {
      "hostname": "spine1",
      "fqdn": "spine1"
    }
  ]
}
Closing connection to spine1...


Connected to spine2..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {
      "hostname": "spine2",
      "fqdn": "spine2"
    }
  ]
}
Closing connection to spine2...
```


The commands we want to capture are as follows:

- Basic Node Health
show version
show uptime

- Interface status
show interfaces counters
show interfaces status

- Control Plane
show ip bgp summary
show bgp evpn summary

- Vxlan/evpn health
show vxlan vtep
show vxlan address-table


Directory structure for project
```
├── cmd
│   └── controller
│       ├── controller
│       └── main.go
├── go.mod
├── internal
│   ├── collector
│   │   └── collector.go
│   ├── inventory
│   │   └── nodes.go
│   ├── normalize
│   │   └── interfaces.go
│   └── transport
│       └── eapi
│           └── client.go
└── README.md

9 directories, 8 files
```
-------------------------------------------------------
cmd/contoller/main.go
```
package main

import (
	"fmt"
	"log"

	"controller/internal/collector"
	"controller/internal/inventory"
)

func main() {
	nodes := inventory.Nodes

	totalNodes := len(nodes)
	nodesWithErrors := 0

	for _, node := range nodes {
		fmt.Printf("\n%s (%s)\n", node.Name, node.MgmtIP)
		stats, err := collector.CollectInterfaceStats(node.MgmtIP)
		if err != nil {
			log.Printf("%s - failed to collect data: %v\n", node.Name, err)
			continue
		}

		nodeHasErrors := false

		for _, intf := range stats {
			if intf.RxErr > 0 || intf.TxErr > 0 {
				fmt.Printf("%s rxErr=%d txErr=%d\n", intf.Name, intf.RxErr, intf.TxErr)
				nodeHasErrors = true
			} else {
				fmt.Printf("  %s rxErr=%d txErr=%d\n",
					intf.Name, intf.RxErr, intf.TxErr)
			}
		}

		if nodeHasErrors {
			nodesWithErrors++
		}
	}

	fmt.Println("\nSummary")
	fmt.Println("-------")
	fmt.Printf("Nodes checked: %d\n", totalNodes)
	fmt.Printf("Nodes with errors: %d\n", nodesWithErrors)
}
```

------------------------------------------------------------

internal/collector/collector.go
```
package collector

import (
    "encoding/json"
    "time"

    "controller/internal/inventory"
    "controller/internal/transport/eapi"
)

type RawSample struct {
    Node      string
    Command   string
    Payload   json.RawMessage
    Timestamp time.Time
}

type InterfaceStats struct {
    Name  string
    RxErr int
    TxErr int
}


// CollectInterfaceStats connects to the device and returns the interface stats.
// Replace this stub with your actual eAPI call.
func CollectInterfaceStats(host string) ([]InterfaceStats, error) {
    // TODO: replace with real eAPI logic
    return []InterfaceStats{
        {Name: "Ethernet10", RxErr: 0, TxErr: 0},
        {Name: "Ethernet47", RxErr: 0, TxErr: 0},
    }, nil
}


func CollectInterfaceCounters(node inventory.Node) ([]RawSample, error) {
    client := eapi.New(node.MgmtIP, node.Username, node.Password)

    results, err := client.RunCmds([]string{
        "show interfaces counters",
    })
    if err != nil {
        return nil, err
    }

    return []RawSample{
        {
            Node:      node.Name,
            Command:   "show interfaces counters",
            Payload:   results[0],
            Timestamp: time.Now(),
        },
    }, nil
}
```

------------------------------------------------------------------------------

internal/inventory/nodes.go
```
package inventory

type Node struct {
	Name		string
	MgmtIP 		string
	Username	string
	Password	string
}

var Nodes = []Node{
	{
		Name: 		"leaf1a",
		MgmtIP: 	"10.0.0.4",
		Username: 	"telemetry",
		Password: 	"telemetry123",
	},
	{
		Name: 		"leaf1b",
		MgmtIP: 	"10.0.0.5",
		Username: 	"telemetry",
		Password: 	"telemetry123",
	},
	{
		Name: 		"leaf2",
		MgmtIP: 	"10.0.0.6",
		Username: 	"telemetry",
		Password: 	"telemetry123",
	},
	{
		Name: 		"spine1",
		MgmtIP: 	"10.0.0.2",
		Username: 	"telemetry",
		Password: 	"telemetry123",
	},
	{
		Name: 		"spine2",
		MgmtIP: 	"10.0.0.3",
		Username: 	"telemetry",
		Password: 	"telemetry123",
	},



}
```

--------------------------------------------------------------

internal/normalize/interfaces.go
```
package normalize

import (
    "encoding/json"
    "time"
)

type InterfaceCounters struct {
    Node       string
    Interface  string
    RxErrors   uint64
    TxErrors   uint64
    Timestamp  time.Time
}

func ParseInterfaceCounters(
    node string,
    payload json.RawMessage,
    ts time.Time,
) ([]InterfaceCounters, error) {

    var parsed struct {
        Interfaces map[string]struct {
            InErrors  uint64 `json:"inErrors"`
            OutErrors uint64 `json:"outErrors"`
        } `json:"interfaces"`
    }

    if err := json.Unmarshal(payload, &parsed); err != nil {
        return nil, err
    }

    counters := []InterfaceCounters{}
    for name, data := range parsed.Interfaces {
        counters = append(counters, InterfaceCounters{
            Node:      node,
            Interface: name,
            RxErrors:  data.InErrors,
            TxErrors:  data.OutErrors,
            Timestamp: ts,
        })
    }

    return counters, nil
}
```
-----------------------------------------------------------------------------
internal/transport/eapi/client.go
```
package eapi

import (
    "bytes"
    "encoding/json"
    "net/http"
    "crypto/tls"
)

type Client struct {
    Addr     string
    Username string
    Password string
}

func New(addr, user, pass string) *Client {
    return &Client{
        Addr:     addr,
        Username: user,
        Password: pass,
    }
}

func (c *Client) RunCmds(cmds []string) ([]json.RawMessage, error) {
    payload := map[string]interface{}{
        "jsonrpc": "2.0",
        "method":  "runCmds",
        "params": map[string]interface{}{
            "version": 1,
            "cmds":    cmds,
        },
        "id": 1,
    }

    body, _ := json.Marshal(payload)

    req, _ := http.NewRequest(
        "POST",
        "https://"+c.Addr+"/command-api",
        bytes.NewBuffer(body),
    )
    req.SetBasicAuth(c.Username, c.Password)
    req.Header.Set("Content-Type", "application/json")
    tr := &http.Transport{
	    TLSClientConfig: &tls.Config{
		    InsecureSkipVerify: true,
	    },
    }
    client := &http.Client{
	    Transport: tr,
    }

    resp, err := client.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()

    var result struct {
        Result []json.RawMessage `json:"result"`
    }

    err = json.NewDecoder(resp.Body).Decode(&result)
    return result.Result, err
}
```

-------------------------------------------------------


Running controller


```
todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab4/scripts/controller$ ./cmd/controller/controller 

leaf1a (10.0.0.4)
  Ethernet10 rxErr=0 txErr=0
  Ethernet47 rxErr=0 txErr=0

leaf1b (10.0.0.5)
  Ethernet10 rxErr=0 txErr=0
  Ethernet47 rxErr=0 txErr=0

leaf2 (10.0.0.6)
  Ethernet10 rxErr=0 txErr=0
  Ethernet47 rxErr=0 txErr=0

spine1 (10.0.0.2)
  Ethernet10 rxErr=0 txErr=0
  Ethernet47 rxErr=0 txErr=0

spine2 (10.0.0.3)
  Ethernet10 rxErr=0 txErr=0
  Ethernet47 rxErr=0 txErr=0

Summary
-------
Nodes checked: 5
Nodes with errors: 0
```


----------------------------------------------
Update - Added bgp to status change, 'show ip bgp summary', as well as the health to internal directory structure.
- Required updates to:
	- cmd/controller/main.go
	- interneral/collector/collector.go
	- normalize/bgp.go
	- health/bgp.go <-- new folder and file

```
$ tree
.
├── cmd
│   └── controller
│       ├── controller
│       ├── main.go
│       └── version_1_main.go <-- depricated main.go
├── go.mod
├── internal
│   ├── collector
│   │   └── collector.go
│   ├── health
│   │   └── bgp.go
│   ├── inventory
│   │   └── nodes.go
│   ├── normalize
│   │   ├── bgp.go
│   │   └── interfaces.go
│   └── transport
│       └── eapi
│           └── client.go
└── README.md

10 directories, 11 files

```
cmd/controller/main.go

main.go
```
package main

import (
	"fmt"
	"log"

	"controller/internal/collector"
	"controller/internal/inventory"
	"controller/internal/normalize"
	"controller/internal/health"
)

func main() {
	nodes := inventory.Nodes
	totalNodes := len(nodes)
	nodesWithIntfErrors := 0

	fmt.Printf("Nodes checked: %d\n", totalNodes)

	for _, node := range nodes {
		fmt.Printf("\n%s (%s)\n", node.Name, node.MgmtIP)

		// -------------------------------
		// Collect interface stats
		// -------------------------------
		ifStats, err := collector.CollectInterfaceStats(node.MgmtIP)
		if err != nil {
			log.Printf("%s - failed to collect interface stats: %v\n", node.Name, err)
			continue
		}

		nodeHasIntfErrors := false
		for _, intf := range ifStats {
			if intf.RxErr > 0 || intf.TxErr > 0 {
				fmt.Printf("  %s rxErr=%d txErr=%d <-- ERROR\n", intf.Name, intf.RxErr, intf.TxErr)
				nodeHasIntfErrors = true
			} else {
				fmt.Printf("  %s rxErr=%d txErr=%d\n", intf.Name, intf.RxErr, intf.TxErr)
			}
		}
		if nodeHasIntfErrors {
			nodesWithIntfErrors++
		}

		// -------------------------------
		// Collect BGP summary
		// -------------------------------
		rawSamples, err := collector.CollectInterfaceCounters(node)
		if err != nil {
			log.Printf("%s - failed to collect BGP summary: %v\n", node.Name, err)
			continue
		}

		for _, sample := range rawSamples {
			if sample.Command != "show ip bgp summary" {
				continue
			}

			peers, err := normalize.ParseBGPSummary(sample.Node, sample.Payload, sample.Timestamp)
			if err != nil {
				log.Printf("%s - failed to parse BGP summary: %v\n", node.Name, err)
				continue
			}

			// Print BGP peers
			for _, p := range peers {
				fmt.Printf(
					"  BGP neighbor=%s vrf=%s state=%s prefixes=%d uptime=%ds\n",
					p.Neighbor,
					p.VRF,
					p.State,
					p.PrefixesRx,
					p.UptimeSec,
				)
			}

			// Evaluate BGP health
			nodeHealth := health.EvaluateBGPPeers(peers)
			fmt.Printf(
				"  --> BGP health: %s (%d/%d peers established)\n",
				nodeHealth.Status,
				nodeHealth.Established,
				nodeHealth.TotalPeers,
			)
		}
	}

	// -------------------------------
	// Print summary
	// -------------------------------
	fmt.Println("\nSummary")
	fmt.Println("-------")
	fmt.Printf("Nodes checked: %d\n", totalNodes)
	fmt.Printf("Nodes with interface errors: %d\n", nodesWithIntfErrors)
}

```
internal/collector/collector.go

collector.go
```
package collector

import (
	"encoding/json"
	"time"

	"controller/internal/inventory"
	"controller/internal/transport/eapi"
)

type RawSample struct {
	Node      string
	Command   string
	Payload   json.RawMessage
	Timestamp time.Time
}

type InterfaceStats struct {
	Name  string
	RxErr int
	TxErr int
}

// CollectInterfaceStats connects to the device and returns the interface stats.
// Replace this stub with your actual eAPI call.
func CollectInterfaceStats(host string) ([]InterfaceStats, error) {
	// TODO: replace with real eAPI logic
	return []InterfaceStats{
		{Name: "Ethernet10", RxErr: 0, TxErr: 0},
		{Name: "Ethernet47", RxErr: 0, TxErr: 0},
	}, nil
}

func CollectInterfaceCounters(node inventory.Node) ([]RawSample, error) {
	client := eapi.New(node.MgmtIP, node.Username, node.Password)

	results, err := client.RunCmds([]string{
		"show interfaces counters", "show ip bgp summary",
	})
	if err != nil {
		return nil, err
	}
	samples := []RawSample{
		{
			Node:      node.Name,
			Command:   "show interfaces counters",
			Payload:   results[0],
			Timestamp: time.Now(),
		},
		{
			Node:      node.Name,
			Command:   "show ip bgp summary",
			Payload:   results[1],
			Timestamp: time.Now(),
		},
	}

	return samples, nil

}
```
internal/health/bgp.go
bgp.go
```
package health

import (
	"controller/internal/normalize"
)

type NodeBGPHealth struct {
	Node        string
	TotalPeers  int
	Established int
	Down        int
	Status      string // "OK", "WARNING", "CRITICAL"
}

// EvaluateBGPPeers checks the BGP peers and returns a summary
func EvaluateBGPPeers(peers []normalize.BGPPeer) NodeBGPHealth {
	health := NodeBGPHealth{
		TotalPeers: len(peers),
		Node:       "",
	}

	for _, p := range peers {
		health.Node = p.Node
		if p.State == "Established" {
			health.Established++
		} else {
			health.Down++
		}
	}

	// Simple health logic:
	switch {
	case health.Established == health.TotalPeers:
		health.Status = "OK"
	case health.Established > 0:
		health.Status = "WARNING"
	default:
		health.Status = "CRITICAL"
	}

	return health
}


```

internal/normalize/bgp.go
bgp.go
```
package normalize

import (
	"encoding/json"
	"time"
)

type BGPPeer struct {
	Node        string
	VRF         string
	Neighbor    string // IP or DNS name
	ASN         string
	State       string
	PrefixesRx  int
	UptimeSec   int
	Timestamp   time.Time
}

func ParseBGPSummary(
	node string,
	payload json.RawMessage,
	ts time.Time,
) ([]BGPPeer, error) {

	var parsed struct {
		VRFs map[string]struct {
			Peers map[string]struct {
				ASN             string `json:"asn"`
				PeerState       string `json:"peerState"`
				PrefixesRx      int    `json:"prefixReceived"`
				UpDownTime      float64    `json:"upDownTime"`
			} `json:"peers"`
		} `json:"vrfs"`
	}

	if err := json.Unmarshal(payload, &parsed); err != nil {
		return nil, err
	}

	peers := []BGPPeer{}

	for vrf, vrfData := range parsed.VRFs {
		for neighbor, data := range vrfData.Peers {
			peers = append(peers, BGPPeer{
				Node:       node,
				VRF:        vrf,
				Neighbor:   neighbor, // IP or DNS, we don't care
				ASN:        data.ASN,
				State:      data.PeerState,
				PrefixesRx: data.PrefixesRx,
				UptimeSec:  int(data.UpDownTime),
				Timestamp:  ts,
			})
		}
	}

	return peers, nil
}

```




