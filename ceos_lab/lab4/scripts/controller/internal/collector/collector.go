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
