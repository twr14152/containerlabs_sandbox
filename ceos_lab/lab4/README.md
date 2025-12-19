# cEOS (2)Spine/(3)Leaf lab

Testing
- ospf/bgp evpn - updated 12.14.2025
  - pings worked between h1 h2 and h3 (required flood list)
  - Can now see mac addresses from show bgp evpn mac
  - Flood lists are required for the evpn to function properly in the lab. The mac learning works in evpn software on ceos the fowarding does not. Thats where the flood lists come in. 
  - Had to keep flood lists on int vxlan1 in order for pings to continue to work
  - configs: scripts/conf_bkup/ospf_bgp_evpn_12.14.2025

- Static vxlan solution  
  - Easiest of the solutions to implement
  - Meant for smaller environments
  - Could ping between 3 different hosts off each leaf switch
  - Requires Headend Replication flood list to remote VTEPs (Leafs)
  - configs: scripts/conf_bkup/ospf_only_underlay_build_12.13.2025

- bgp/bgp evpn
  - scripts to build
    - buildout_bgp_underlay.py
    - buildout_bgp_overlay.py
    - The mlag configs were build prior to setting this up but would also be necessary for this to work
    - Flood lists are required for the evpn to function properly in the lab. The mac learning works in evpn software on ceos the fowarding does not. Thats where the flood lists come in. 
  -  configs: scripts/conf_bkup/bgp_bgp_evpn.12.16.2025

