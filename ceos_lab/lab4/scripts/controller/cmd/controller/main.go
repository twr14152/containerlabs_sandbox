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
		rawSamples, err := collector.CollectOperationalState(node)
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

