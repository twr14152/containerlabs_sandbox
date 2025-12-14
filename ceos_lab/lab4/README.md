# cEOS (2)Spine/(3)Leaf lab

Testing
- ospf/bgp evpn - updated 12.14.2025
  - pings worked between h1 h2 and h3 (required flood list)
  - Can now see mac addresses from show bgp evpn mac
  - Had to keep flood lists on int vxlan1 in order for pings to continue to work
  - configs: /scripts/conf_bkup/ospf_bgp_evpn_12.14.2025

- Ospf only solution using vxlan 
  - Easiest of the solutions to implement
  - Meant for smaller environments
  - Could ping between 3 different hosts off each leaf switch
  - Requires vxlan flood list to remote VTEPs (Leafs)
  - configs: /scripts/conf_bkup/ospf_only_underlay_build_12.13.2025

- bgp/bgp evpn
  - pings worked between hosts
  - unable to see any mac addresses using show bgp evpn mac ??
  -  configs: /scripts/conf_bkup/bgp_underlay_evpn_12.13.2025

