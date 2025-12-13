# cEOS (2)Spine/(3)Leaf lab

Testing
- ospf only underlay with vxlan vtep/flood domain
  - worked
  - Could ping between 3 different hosts off each leaf switch
  - Believe it worked because ospf and vxlan flood domains were configured
- ospf/bgp evpn
  - pings worked
  - unable to see any mac addresses from show bgp evpn mac ??
- bgp/bgp evpn
  - pings worked between hosts
  - unable to see any mac addresses using show bgp evpn mac ??

