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
