### Script output

```
$ ./ssh_file 

--- Connecting to leaf1a:22 ---
[Waiting for prompt: >]
[PROMPT FOUND]
[Waiting for prompt: #]
[PROMPT FOUND]
[Waiting for prompt: #]
[PROMPT FOUND]
Sending commands from: file_leaf1a:22.cfg
[SENDING] enable
[OUTPUT]
enable
leaf1a#
[SENDING] show vxlan vni
[OUTPUT]
show vxlan vni
VNI to VLAN Mapping for Vxlan1
VNI   VLAN Source Interface  802.1Q Tag
----- ---- ------ ---------- ----------
20020 20   static Ethernet1  untagged  
                  Ethernet10 untagged  
                  Vxlan1     20        

VNI to dynamic VLAN Mapping for Vxlan1
VNI     VLAN      VRF      Source      
------- --------- -------- ----------- 

leaf1a#
[SENDING] show vxlan vtep
[OUTPUT]
show vxlan vtep
Remote VTEPS for Vxlan1:

VTEP            Tunnel Type(s)
--------------- --------------
1.1.1.103       flood         

Total number of remote VTEPS:  1
leaf1a#
[SENDING] show bgp evpn summary 
[OUTPUT]
show bgp evpn summary 
BGP summary information for VRF default
Router identifier 1.1.1.1, local AS number 65001
Neighbor Status Codes: m - Under maintenance
  Neighbor      V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc PfxAdv
  100.100.100.1 4 65000           7894      8018    0    0    4d14h Estab   1      1      1
leaf1a#

--- Connecting to leaf1b:22 ---
[Waiting for prompt: >]
[PROMPT FOUND]
[Waiting for prompt: #]
[PROMPT FOUND]
[Waiting for prompt: #]
[PROMPT FOUND]
Sending commands from: file_leaf1b:22.cfg
[SENDING] enable
[OUTPUT]
enable
leaf1b#
[SENDING] show vxlan vni
[OUTPUT]
show vxlan vni
VNI to VLAN Mapping for Vxlan1
VNI   VLAN Source Interface  802.1Q Tag
----- ---- ------ ---------- ----------
20020 20   static Ethernet10 untagged  
                  Vxlan1     20        

VNI to dynamic VLAN Mapping for Vxlan1
VNI     VLAN      VRF      Source      
------- --------- -------- ----------- 

leaf1b#
[SENDING] show vxlan vtep
[OUTPUT]
show vxlan vtep
Remote VTEPS for Vxlan1:

VTEP            Tunnel Type(s)
--------------- --------------
1.1.1.103       flood         

Total number of remote VTEPS:  1
leaf1b#
[SENDING] show bgp evpn summary 
[OUTPUT]
show bgp evpn summary 
BGP summary information for VRF default
Router identifier 1.1.1.2, local AS number 65001
Neighbor Status Codes: m - Under maintenance
  Neighbor      V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc PfxAdv
  100.100.100.2 4 65000           7912      8028    0    0    4d14h Estab   1      1      1
leaf1b#

--- Connecting to leaf2:22 ---
[Waiting for prompt: >]
[PROMPT FOUND]
[Waiting for prompt: #]
[PROMPT FOUND]
[Waiting for prompt: #]
[PROMPT FOUND]
Sending commands from: file_leaf2:22.cfg
[SENDING] enable
[OUTPUT]
enable
leaf2#
[SENDING] show vxlan vni
[OUTPUT]
show vxlan vni
VNI to VLAN Mapping for Vxlan1
VNI   VLAN Source Interface  802.1Q Tag
----- ---- ------ ---------- ----------
20020 20   static Ethernet10 untagged  
                  Vxlan1     20        

VNI to dynamic VLAN Mapping for Vxlan1
VNI     VLAN      VRF      Source      
------- --------- -------- ----------- 

leaf2#
[SENDING] show vxlan vtep
[OUTPUT]
show vxlan vtep
Remote VTEPS for Vxlan1:

VTEP            Tunnel Type(s)
--------------- --------------
1.1.1.101       flood         

Total number of remote VTEPS:  1
leaf2#
[SENDING] show bgp evpn summary 
[OUTPUT]
show bgp evpn summary 
BGP summary information for VRF default
Router identifier 1.1.1.3, local AS number 65002
Neighbor Status Codes: m - Under maintenance
  Neighbor      V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc PfxAdv
  100.100.100.1 4 65000           8009      8088    0    0    4d14h Estab   1      1      2
  100.100.100.2 4 65000           8010      8112    0    0    4d14h Estab   1      1      1
leaf2#

--- Connecting to spine1:22 ---
[Waiting for prompt: >]
[PROMPT FOUND]
[Waiting for prompt: #]
[PROMPT FOUND]
[Waiting for prompt: #]
[PROMPT FOUND]
Sending commands from: file_spine1:22.cfg
[SENDING] enable
[OUTPUT]
enable
spine1#
[SENDING] show ip bgp summ
[OUTPUT]
show ip bgp summ
BGP summary information for VRF default
Router identifier 100.100.100.1, local AS number 65000
Neighbor Status Codes: m - Under maintenance
  Neighbor V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc PfxAdv
  1.1.1.1  4 65001           8018      7894    0    0    4d14h Estab   2      2      5
  1.1.1.3  4 65002           8088      8009    0    0    4d14h Estab   2      2      5
  10.1.0.1 4 65001           7796      7798    0    0    4d14h Estab   2      2      3
  10.1.0.5 4 65002           7794      7789    0    0    4d14h Estab   2      2      3
spine1#
[SENDING] show bgp evpn summ
[OUTPUT]
show bgp evpn summ
BGP summary information for VRF default
Router identifier 100.100.100.1, local AS number 65000
Neighbor Status Codes: m - Under maintenance
  Neighbor V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc PfxAdv
  1.1.1.1  4 65001           8018      7894    0    0    4d14h Estab   1      1      1
  1.1.1.3  4 65002           8088      8009    0    0    4d14h Estab   1      1      1
spine1#
[SENDING] show ip route
[OUTPUT]
show ip route

VRF: default
Source Codes:
       C - connected, S - static, K - kernel,
       O - OSPF, O IA - OSPF inter area, O E1 - OSPF external type 1,
       O E2 - OSPF external type 2, O N1 - OSPF NSSA external type 1,
       O N2 - OSPF NSSA external type2, O3 - OSPFv3,
       O3 IA - OSPFv3 inter area, O3 E1 - OSPFv3 external type 1,
       O3 E2 - OSPFv3 external type 2,
       O3 N1 - OSPFv3 NSSA external type 1,
       O3 N2 - OSPFv3 NSSA external type2, B - Other BGP Routes,
       B I - iBGP, B E - eBGP, R - RIP, I L1 - IS-IS level 1,
       I L2 - IS-IS level 2, A B - BGP Aggregate,
       A O - OSPF Summary, NG - Nexthop Group Static Route,
       V - VXLAN Control Service, M - Martian,
       DH - DHCP client installed default route,
       DP - Dynamic Policy Route, L - VRF Leaked,
       G  - gRIBI, RC - Route Cache Route,
       CL - CBF Leaked Route

Gateway of last resort:
 S        0.0.0.0/0 [1/0]
           via 10.0.0.1, Management0

 B E      1.1.1.1/32 [200/0]
           via 10.1.0.1, Ethernet3
 B E      1.1.1.3/32 [200/0]
           via 10.1.0.5, Ethernet4
 B E      1.1.1.101/32 [200/0]
           via 10.1.0.1, Ethernet3
 B E      1.1.1.103/32 [200/0]
           via 10.1.0.5, Ethernet4
 C        10.0.0.0/24
           directly connected, Management0
 C        10.1.0.0/31
           directly connected, Ethernet3
 C        10.1.0.4/31
           directly connected, Ethernet4
 C        100.100.100.1/32
           directly connected, Loopback0

spine1#

--- Connecting to spine2:22 ---
[Waiting for prompt: >]
[PROMPT FOUND]
[Waiting for prompt: #]
[PROMPT FOUND]
[Waiting for prompt: #]
[PROMPT FOUND]
Sending commands from: file_spine2:22.cfg
[SENDING] enable
[OUTPUT]
enable
spine2#
[SENDING] show ip bgp summ
[OUTPUT]
show ip bgp summ
BGP summary information for VRF default
Router identifier 100.100.100.2, local AS number 65000
Neighbor Status Codes: m - Under maintenance
  Neighbor V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc PfxAdv
  1.1.1.2  4 65001           8028      7912    0    0    4d14h Estab   2      2      5
  1.1.1.3  4 65002           8112      8010    0    0    4d14h Estab   2      2      5
  10.1.0.3 4 65001           7792      7805    0    0    4d14h Estab   2      2      3
  10.1.0.7 4 65002           7793      7801    0    0    4d14h Estab   2      2      3
spine2#
[SENDING] show bgp evpn summ
[OUTPUT]
show bgp evpn summ
BGP summary information for VRF default
Router identifier 100.100.100.2, local AS number 65000
Neighbor Status Codes: m - Under maintenance
  Neighbor V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc PfxAdv
  1.1.1.2  4 65001           8028      7912    0    0    4d14h Estab   1      1      1
  1.1.1.3  4 65002           8112      8010    0    0    4d14h Estab   1      1      1
spine2#
[SENDING] show ip route
[OUTPUT]
show ip route

VRF: default
Source Codes:
       C - connected, S - static, K - kernel,
       O - OSPF, O IA - OSPF inter area, O E1 - OSPF external type 1,
       O E2 - OSPF external type 2, O N1 - OSPF NSSA external type 1,
       O N2 - OSPF NSSA external type2, O3 - OSPFv3,
       O3 IA - OSPFv3 inter area, O3 E1 - OSPFv3 external type 1,
       O3 E2 - OSPFv3 external type 2,
       O3 N1 - OSPFv3 NSSA external type 1,
       O3 N2 - OSPFv3 NSSA external type2, B - Other BGP Routes,
       B I - iBGP, B E - eBGP, R - RIP, I L1 - IS-IS level 1,
       I L2 - IS-IS level 2, A B - BGP Aggregate,
       A O - OSPF Summary, NG - Nexthop Group Static Route,
       V - VXLAN Control Service, M - Martian,
       DH - DHCP client installed default route,
       DP - Dynamic Policy Route, L - VRF Leaked,
       G  - gRIBI, RC - Route Cache Route,
       CL - CBF Leaked Route

Gateway of last resort:
 S        0.0.0.0/0 [1/0]
           via 10.0.0.1, Management0

 B E      1.1.1.2/32 [200/0]
           via 10.1.0.3, Ethernet3
 B E      1.1.1.3/32 [200/0]
           via 10.1.0.7, Ethernet4
 B E      1.1.1.101/32 [200/0]
           via 10.1.0.3, Ethernet3
 B E      1.1.1.103/32 [200/0]
           via 10.1.0.7, Ethernet4
 C        10.0.0.0/24
           directly connected, Management0
 C        10.1.0.2/31
           directly connected, Ethernet3
 C        10.1.0.6/31
           directly connected, Ethernet4
 C        100.100.100.2/32
           directly connected, Loopback0

spine2#

--- Connecting to  ---
2026/02/05 03:36:19 Failed to dial : dial tcp: missing address
$ 
