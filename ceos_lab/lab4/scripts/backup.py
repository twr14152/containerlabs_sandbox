#!/home/todd/Code_folder/containerlab/containerlabs_sandbox/myenv/bin/python

from jsonrpclib import Server
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

hosts = ["leaf1a", "leaf1b", "leaf2", "spine1", "spine2"]

cmds = ["enable", "copy running-config startup-config"]

for host in hosts:
    print(f"Connecting to host {host}...")
    switch = Server(f"https://admin:admin@{host}/command-api")
    response = switch.runCmds( 1, cmds )
    print(json.dumps(response, indent=2))
    print(f"Disconnecting from  host {host}...")

