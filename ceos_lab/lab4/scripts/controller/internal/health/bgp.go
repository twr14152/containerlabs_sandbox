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

