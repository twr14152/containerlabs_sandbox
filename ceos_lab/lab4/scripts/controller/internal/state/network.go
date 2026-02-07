package state

import (
    "time"

    "controller/internal/normalize"
    "controller/internal/health"
)

type NetworkState struct {
    Timestamp time.Time

    Interfaces map[string][]normalize.InterfaceCounters
    BGP        map[string]health.NodeBGPHealth
}
