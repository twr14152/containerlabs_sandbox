#!/bin/sh
set -e

# --- Install required packages if not already installed ---
if ! apk info | grep -q "^openssh\$"; then
  apk update
  apk add --no-cache openssh openssh-server sudo shadow
fi

# --- Create admin user if not exists ---
if ! id admin >/dev/null 2>&1; then
  adduser -D -h /home/admin -s /bin/sh admin
  echo 'admin:admin' | chpasswd
  echo 'admin ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
fi

# --- Ensure admin is in frrvty group ---
if ! getent group frrvty >/dev/null 2>&1; then
  addgroup -g 102 frrvty
fi

if ! id -nG admin | grep -qw frrvty; then
  adduser admin frrvty
fi

# --- Prepare SSH environment ---
mkdir -p /run/sshd

# --- Update sshd_config safely ---
grep -q '^PermitRootLogin yes' /etc/ssh/sshd_config || echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
grep -q '^PasswordAuthentication yes' /etc/ssh/sshd_config || echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
grep -q '^ListenAddress 0.0.0.0' /etc/ssh/sshd_config || echo 'ListenAddress 0.0.0.0' >> /etc/ssh/sshd_config

# --- Generate host keys if not exist ---
if [ ! -f /etc/ssh/ssh_host_rsa_key ]; then
  ssh-keygen -A
fi

# --- Kill existing sshd instances to avoid duplicates ---
pkill sshd || true

# --- Start sshd daemon ---
/usr/sbin/sshd

echo "SSH server is up and running."
