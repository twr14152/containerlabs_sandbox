#!/usr/bin/python3.12

import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ans = input("Do you want to connect to all hosts?..(y/n):")

if ans == 'y':
    hosts = ["leaf1a", "leaf1b", "leaf2", "spine1", "spine2"]
    ans = input("Do you have a config or cmds file to load (y/n): ")
    if ans == 'y':
        cfg_file = input("Enter file name (eg..'hostname.cmds' or 'hostname-description.cfg'): ")
        with open(cfg_file) as f:
            cmds = f.read().splitlines()
        for host in hosts:
            url = f"https://{host}/command-api"
            print(f"Connected to {host}..")
            headers = {'Content-Type': 'application/json'}
            payload = {
                    "jsonrpc": "2.0",
                    "method": "runCmds",
                    "params": {
                        "version": 1,
                        "cmds": cmds,
                        "format": "json"
                        },
                    "id": "1"
                    }
            response = requests.post(url, data=json.dumps(payload), auth=('admin', 'admin'), verify=False)
            print(json.dumps(response.json(), indent=2))
            print(f"Closing connection to {host}...\n\n")

    else:
        commands = input('Enter commands to run seperated by ",": ')
        cmds = commands.split(",")

        for host in hosts:
            url = f"https://{host}/command-api"
            print(f"Connected to {host}..")
            headers = {'Content-Type': 'application/json'}
            payload = {
                    "jsonrpc": "2.0",
                    "method": "runCmds",
                    "params": {
                        "version": 1,
                        "cmds": cmds,
                        "format": "json"
                        },
                    "id": "1"
                    }
            response = requests.post(url, data=json.dumps(payload), auth=('admin', 'admin'), verify=False)
            print(json.dumps(response.json(), indent=2))
            print(f"Closing connection to {host}...\n\n")




else:
    host_list = input("Enter host or hostnames separated by ',': ")
    hosts = [i.strip() for i in host_list.split(",")] #splits into a list and removes white space

    ans = input("Do you have a config or cmds file to load (y/n): ")
    if ans == 'y':
        for host in hosts:
            cfg_file = input("Enter file name (eg..'hostname.cmds' or 'hostname-description.cfg'): ")
            with open(cfg_file) as f:
                cmds = f.read().splitlines()
            url = f"https://{host}/command-api"
            print(f"Connected to {host}..")
            headers = {'Content-Type': 'application/json'}
            payload = {
                    "jsonrpc": "2.0",
                    "method": "runCmds",
                    "params": {
                        "version": 1,
                        "cmds": cmds,
                        "format": "json"
                        },
                    "id": "1"
                    }
            response = requests.post(url, data=json.dumps(payload), auth=('admin', 'admin'), verify=False)
            print(json.dumps(response.json(), indent=2))
            print(f"Closing connection to {host}...\n\n")

