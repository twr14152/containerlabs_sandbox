How to backup configs used in lab
```
todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts$ ./lab_script.py | tee bkup/config_file.txt
Login into all devices?: (y/n)y
Login into clab-lab3-ceos1: (y/n)
Login into clab-lab3-ceos2: (y/n)
Login into clab-lab3-ceos3: (y/n)
Enter configs: 
Enter show commands: show run , wr mem
connecting to: clab-lab3-ceos1
configure terminal
ceos1(config)#
ceos1(config)#end
ceos1#
! Command: show running-config
! device: ceos1 (cEOSLab, EOS-4.34.2F-43232954.4342F.1 (engineering build))
!
no aaa root
!
username admin privilege 15 role network-admin secret sha512 $6$dfnPlRK7dM5.gtV3$2buw6CucLcHz.LDPiJdP1H9cof6BShC6Om3nE02nE7VL/EWcwj3iXT7gM/TJLzFZWXviX5svPiUkzaTspnHcj.
!
management api http-commands
   protocol https ssl profile self-signed-certs
   no shutdown
!
no service interface inactive port-id allocation disabled
!
transceiver qsfp default-mode 4x10G
!
service routing protocols model multi-agent
!
hostname ceos1
!
spanning-tree mode mstp
!
system l1
   unsupported speed action error
   unsupported error-correction action error
!
management api gnmi
   transport grpc default
!
management api netconf
   transport ssh default
!
management api restconf
   transport https default
      ssl profile self-signed-certs
!
management security
   ssl profile self-signed-certs
      certificate self-signed.crt key self-signed.key
!
interface Ethernet1
   description to ceos2
   no switchport
   ip address 10.0.0.1/24
!
interface Ethernet2
   description to ceos3
   no switchport
   ip address 10.0.1.1/24
!
interface Ethernet3
!
interface Loopback0
   description testing restconf
   ip address 1.1.1.1/32
!
interface Management0
   ip address 172.20.20.5/24
   ipv6 address 3fff:172:20:20::5/64
!
ip access-list MGMT-ACL
   10 permit icmp any any
   20 permit ip any any tracked
   30 permit udp any any eq bfd ttl eq 255
   40 permit udp any any eq bfd-echo ttl eq 254
   50 permit udp any any eq multihop-bfd micro-bfd sbfd
   60 permit udp any eq sbfd any eq sbfd-initiator
   70 permit ospf any any
   80 permit tcp any any eq ssh telnet www snmp bgp https msdp ldp netconf-ssh gnmi
   90 permit udp any any eq bootps bootpc ntp snmp ptp-event ptp-general rip ldp
   100 permit tcp any any eq mlag ttl eq 255
   110 permit udp any any eq mlag ttl eq 255
   120 permit vrrp any any
   130 permit ahp any any
   140 permit pim any any
   150 permit igmp any any
   160 permit tcp any any range 5900 5910
   170 permit tcp any any range 50000 50100
   180 permit udp any any range 51000 51100
   190 permit tcp any any eq 3333
   200 permit tcp any any eq nat ttl eq 255
   210 permit tcp any eq bgp any
   220 permit rsvp any any
   230 permit tcp any any eq 9340
   240 permit tcp any any eq 9559
   250 permit udp any any eq 8503
   260 permit udp any any eq lsp-ping
   270 permit udp any eq lsp-ping any range 51900 51999
   280 permit tcp any any eq 6020
!
ip routing
!
system control-plane
   ip access-group MGMT-ACL in
!
ip route 0.0.0.0/0 172.20.20.1
!
ipv6 route ::/0 3fff:172:20:20::1
!
router bgp 1
   distance bgp 20 200 200
   neighbor 10.0.0.2 remote-as 2
   neighbor 10.0.0.2 description ceos2
   neighbor 10.0.0.2 timers 1 4
   network 1.1.1.1/32
   redistribute connected
!
router multicast
   ipv4
      software-forwarding kernel
   !
   ipv6
      software-forwarding kernel
!
router ospf 1
   network 0.0.0.0/0 area 0.0.0.0
   network 10.0.0.0/8 area 0.0.0.0
   max-lsa 12000
!
end
Copy completed successfully.
connecting to: clab-lab3-ceos2
configure terminal
ceos2(config)#
ceos2(config)#end
ceos2#
! Command: show running-config
! device: ceos2 (cEOSLab, EOS-4.34.2F-43232954.4342F.1 (engineering build))
!
no aaa root
!
username admin privilege 15 role network-admin secret sha512 $6$OZ7Mor044Vt7RJ2J$x4S1h/AxW/z.wvQFkFsJhdaGmhEub/ASVuptL6CNJ28zW5xERgq2rzUl8JlVrORsQrkOgzrDfYgBVk6amTMN10
!
management api http-commands
   protocol https ssl profile self-signed-certs
   no shutdown
!
no service interface inactive port-id allocation disabled
!
transceiver qsfp default-mode 4x10G
!
service routing protocols model multi-agent
!
hostname ceos2
!
spanning-tree mode mstp
!
system l1
   unsupported speed action error
   unsupported error-correction action error
!
management api gnmi
   transport grpc default
!
management api netconf
   transport ssh default
!
management api restconf
   transport https default
      ssl profile self-signed-certs
!
management security
   ssl profile self-signed-certs
      certificate self-signed.crt key self-signed.key
!
interface Ethernet1
   description to ceos1
   no switchport
   ip address 10.0.0.2/24
!
interface Ethernet2
   description to ceos3
   no switchport
   ip address 10.0.2.2/24
!
interface Ethernet3
!
interface Loopback0
   description testing restconf
   ip address 2.2.2.2/32
!
interface Management0
   ip address 172.20.20.7/24
   ipv6 address 3fff:172:20:20::7/64
!
ip access-list MGMT-ACL
   10 permit icmp any any
   20 permit ip any any tracked
   30 permit udp any any eq bfd ttl eq 255
   40 permit udp any any eq bfd-echo ttl eq 254
   50 permit udp any any eq multihop-bfd micro-bfd sbfd
   60 permit udp any eq sbfd any eq sbfd-initiator
   70 permit ospf any any
   80 permit tcp any any eq ssh telnet www snmp bgp https msdp ldp netconf-ssh gnmi
   90 permit udp any any eq bootps bootpc ntp snmp ptp-event ptp-general rip ldp
   100 permit tcp any any eq mlag ttl eq 255
   110 permit udp any any eq mlag ttl eq 255
   120 permit vrrp any any
   130 permit ahp any any
   140 permit pim any any
   150 permit igmp any any
   160 permit tcp any any range 5900 5910
   170 permit tcp any any range 50000 50100
   180 permit udp any any range 51000 51100
   190 permit tcp any any eq 3333
   200 permit tcp any any eq nat ttl eq 255
   210 permit tcp any eq bgp any
   220 permit rsvp any any
   230 permit tcp any any eq 9340
   240 permit tcp any any eq 9559
   250 permit udp any any eq 8503
   260 permit udp any any eq lsp-ping
   270 permit udp any eq lsp-ping any range 51900 51999
   280 permit tcp any any eq 6020
!
ip routing
!
system control-plane
   ip access-group MGMT-ACL in
!
ip route 0.0.0.0/0 172.20.20.1
!
ipv6 route ::/0 3fff:172:20:20::1
!
router bgp 2
   distance bgp 20 200 200
   neighbor 10.0.0.1 remote-as 1
   neighbor 10.0.0.1 description ceos1
   neighbor 10.0.0.1 timers 1 4
   network 2.2.2.2/32
   redistribute connected
!
router multicast
   ipv4
      software-forwarding kernel
   !
   ipv6
      software-forwarding kernel
!
router ospf 1
   network 0.0.0.0/0 area 0.0.0.0
   network 10.0.0.0/8 area 0.0.0.0
   max-lsa 12000
!
end
Copy completed successfully.
connecting to: clab-lab3-ceos3
configure terminal
ceos3(config)#
ceos3(config)#end
ceos3#
! Command: show running-config
! device: ceos3 (cEOSLab, EOS-4.34.2F-43232954.4342F.1 (engineering build))
!
no aaa root
!
username admin privilege 15 role network-admin secret sha512 $6$wbQ1lctzznhGevNS$A.BkmfJjIY6UAFMhlSozbdTnlcgAsd8UlKR2lM5QaitOVsGjlb0tU5GZJelRiZL54v.BFxmhvgk1R1Y5L86nd0
!
management api http-commands
   protocol https ssl profile self-signed-certs
   no shutdown
!
no service interface inactive port-id allocation disabled
!
transceiver qsfp default-mode 4x10G
!
service routing protocols model multi-agent
!
hostname ceos3
!
spanning-tree mode mstp
!
system l1
   unsupported speed action error
   unsupported error-correction action error
!
management api gnmi
   transport grpc default
!
management api netconf
   transport ssh default
!
management api restconf
   transport https default
      ssl profile self-signed-certs
!
management security
   ssl profile self-signed-certs
      certificate self-signed.crt key self-signed.key
!
interface Ethernet1
   description to ceos1
   no switchport
   ip address 10.0.1.3/24
!
interface Ethernet2
   description to ceos2
   no switchport
   ip address 10.0.2.3/24
!
interface Ethernet3
!
interface Loopback0
   description testing restconf
   ip address 3.3.3.3/32
!
interface Management0
   ip address 172.20.20.8/24
   ipv6 address 3fff:172:20:20::8/64
!
ip access-list MGMT-ACL
   10 permit icmp any any
   20 permit ip any any tracked
   30 permit udp any any eq bfd ttl eq 255
   40 permit udp any any eq bfd-echo ttl eq 254
   50 permit udp any any eq multihop-bfd micro-bfd sbfd
   60 permit udp any eq sbfd any eq sbfd-initiator
   70 permit ospf any any
   80 permit tcp any any eq ssh telnet www snmp bgp https msdp ldp netconf-ssh gnmi
   90 permit udp any any eq bootps bootpc ntp snmp ptp-event ptp-general rip ldp
   100 permit tcp any any eq mlag ttl eq 255
   110 permit udp any any eq mlag ttl eq 255
   120 permit vrrp any any
   130 permit ahp any any
   140 permit pim any any
   150 permit igmp any any
   160 permit tcp any any range 5900 5910
   170 permit tcp any any range 50000 50100
   180 permit udp any any range 51000 51100
   190 permit tcp any any eq 3333
   200 permit tcp any any eq nat ttl eq 255
   210 permit tcp any eq bgp any
   220 permit rsvp any any
   230 permit tcp any any eq 9340
   240 permit tcp any any eq 9559
   250 permit udp any any eq 8503
   260 permit udp any any eq lsp-ping
   270 permit udp any eq lsp-ping any range 51900 51999
   280 permit tcp any any eq 6020
!
ip routing
!
system control-plane
   ip access-group MGMT-ACL in
!
ip route 0.0.0.0/0 172.20.20.1
!
ipv6 route ::/0 3fff:172:20:20::1
!
router multicast
   ipv4
      software-forwarding kernel
   !
   ipv6
      software-forwarding kernel
!
router ospf 1
   network 0.0.0.0/0 area 0.0.0.0
   network 10.0.0.0/8 area 0.0.0.0
   max-lsa 12000
!
end
Copy completed successfully.
todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts$ 
end
Copy completed successfully.
todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts$ 
```
