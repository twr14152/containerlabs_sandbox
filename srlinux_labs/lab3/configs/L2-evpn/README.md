layer2 evpn

<img width="1482" height="743" alt="image" src="https://github.com/user-attachments/assets/559a7024-eb2a-415a-99ab-9a9fb8044a41" />

- Stretching Vlan10 192.168.101.0/24 between leaf1 and leaf2
- Interface irb10  using 192.168.101.1 address on both leaf1 and leaf2
- ebgp between leaf and spines for ip connectivity (underlay)
- evpn set up network-instance bridging-network (overlay)
- Connecting leaf1 hosts client10-12 and leaf2 host client20
