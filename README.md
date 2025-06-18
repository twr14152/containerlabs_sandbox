# containerlabs_sandbox
- This repo will store store some labs as I mess around with this tool.
- Apple silicon has required me to go down this path.
- So far just using cEOS and FRR for the routing and switching components
- With in couple of hours I've figured out how to use FRR in the way I was hoping to use cEOS.
- After some digging I found I was making too difficult to ssh into cEOS containerlab has that working out of the gates
- FRR is a much lighter performant image with my Mac M1.
- FRR/first_lab - basically just tested the routing and got ssh working
  - How to run multiple commands on frr router
    - docker exec <host> sh -c "vtysh -c '<>' -c '<>'"
    - docker exec clab-frr_lab-router1 sh -c "vtysh -c 'show version' -c 'show interface eth0' -c 'show ip route'"
- ceos_labs/lab1 - first functional arista lab on this platform
- ceos_labs/lab2 - More devices and eats more resources - if I reboot orbstack before running I have better success with it

