# cEOS (2)Spine/(3)Leaf lab

Testing
- ospf/bgp evpn - updated 12.14.2025
  - pings worked between h1 h2 and h3 (required flood list)
  - Can now see mac addresses from show bgp evpn mac
  - Changed Lo1 on leaf1b to match Lo1 on leaf1a (mlag switches) as it was causing DUPs to be sent to the h1 from pings from h3. Reason was because of the flood list on VTEP on leaf3 was sending to both leaf1b Lo1 at 1.1.1.102 and leaf lo1 at 1.1.1.101. Changing leaf1b Lo1 to 1.1.1.101 and removing .102 from flood list appears to have fixed the issue.
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

