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
