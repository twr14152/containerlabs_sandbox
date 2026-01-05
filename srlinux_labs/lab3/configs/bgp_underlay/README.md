BGP Underlay notes

- started advertising loopback0 as the router id in BGP ended up changing this on Leaf1 and leaf2 as the system0.0 would be used for this and for vxlan source IP.
- I tried having them both use the same address to no avail. So i removed Lo0. As stated the router-id would now come from system0.0 IP. Until I read otherwise.
- Policy routing needed tweaked. The examples provided in reading and videos get a little confusing. In that they say you should tweak default behavior for import and export policy routing if you are just starting
- Custom policy routing from reading has you define default behavior and if its default action is to reject non matching routes, then its location in your policy can matter. That's is to say if you have multiple policies being applied to export routes. In my case leaf1 router has a default action of rejecting routes that aren't the network associated with the irb interface. That policy was listed prior to the one advertising my RID in bgp. So my system0.0 interface was being black holed. So I need to add the RID policy prior to the policy advertising my irb network to get it advertised to the network. Only on leaf1.
-  enabling multipath was straight forward
