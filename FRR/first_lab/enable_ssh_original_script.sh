#!/bin/sh
set -e

# Install required packages
apk update
apk add --no-cache openssh openssh-server sudo shadow

# Create admin user and configure sudo
adduser -D -h /home/admin -s /bin/sh admin
echo 'admin:admin' | chpasswd
echo 'admin ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Create group and add user
addgroup -g 102 frrvty
adduser admin frrvty

# Prepare SSH environment
mkdir -p /run/sshd

# Configure sshd
echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
echo 'ListenAddress 0.0.0.0' >> /etc/ssh/sshd_config

# Generate SSH host keys
ssh-keygen -A

# Start SSH daemon
/usr/sbin/sshd

echo "SSH server started. Login with admin/admin"
