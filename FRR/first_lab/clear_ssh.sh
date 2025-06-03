cat clear_ssh.sh 
#!/bin/sh
#
ssh-keygen -f "/home/toddriemenschneider/.ssh/known_hosts" -R "172.20.20.2"
ssh-keygen -f "/home/toddriemenschneider/.ssh/known_hosts" -R "172.20.20.3"
ssh-keygen -f "/home/toddriemenschneider/.ssh/known_hosts" -R "172.20.20.4"
ssh-keygen -f "/home/toddriemenschneider/.ssh/known_hosts" -R "172.20.20.5"
