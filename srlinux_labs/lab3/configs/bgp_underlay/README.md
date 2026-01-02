BGP Underlay notes

- started advertising loopback0 as the router id in BGP ended up changing this on Leaf1/2 as the system0.0 would be used for this and for vxlan source IP.
- I tried having them both use the same address to no avail. So i removed Lo0. As stated the router-id would now come from that IP. Until I read otherwise.
- Policy routing needed tweaked. The examples provided in reading and videos get a little confusing. In that they say you should tweak default behavior for import and export policy routing if you are just starting
- Custom policy routing from reading has you define default behavior and if its reject its location will matter in your group that your applying routing policy it if you have other routes your trying to advertise as well.
-  enabling multipath was straight forward
