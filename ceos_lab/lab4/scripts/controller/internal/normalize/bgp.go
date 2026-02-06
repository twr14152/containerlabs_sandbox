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

