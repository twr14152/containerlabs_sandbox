#!/home/todd/Code_folder/containerlab/containerlabs_sandbox/myenv/bin/python

from netmiko import ConnectHandler 
import sys

devices = ["ceos1", "ceos2", "ceos3"]

q1 = input("Login into all devices?: (y/n)")
if q1 == "y":
    config_commands = input("Enter configs: ")
    show_commands = input("Enter show commands: ")
    for host in devices:
        device = {
        'device_type': 'arista_eos',
        'ip': host, 
        'username': 'admin',
        'password': 'admin',
        'secret' : 'admin',
        }
        print(f"connecting to: {host}" )
        #commands = input("Enter commands: ")
        cfg_cmds = config_commands.split(",")
        show_cmds = show_commands.split(",")
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        output = net_connect.send_config_set(cfg_cmds)
        print(output)
        for cmd in show_cmds:
            output = net_connect.send_command(cmd)
            print(output)
    end_script = input("Are you done (y/n): ")
    if end_script == "y":
        sys.exit(0)

q2 = input("Login into ceos1: (y/n)")
q3 = input("Login into ceos2: (y/n)")
q4 = input("Login into ceos3: (y/n)")



if len(q1) < 1: q1 == "n"
if len(q2) < 1: q2 == "n"
if len(q3) < 1: q3 == "n"
if len(q4) < 1: q4 == "n"

if q2 == "y":
    host = "ceos1"
    device = {
            'device_type': 'arista_eos',
            'ip': host,
            'username': 'admin',
            'password': 'admin',
            'secret' : 'admin',
            }
    print(f"connecting to: {host}" )
    config_commands = input("Enter configs: ")
    show_commands = input("Enter show commands: ")
    cfg_cmds = config_commands.split(",")
    show_cmds = show_commands.split(",")
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    output = net_connect.send_config_set(cfg_cmds)
    print(output)
    for cmd in show_cmds:
        output = net_connect.send_command(cmd)
        print(output)


if q3 == "y":
    host = "ceos2"
    device = {
            'device_type': 'arista_eos',
            'ip': host,
            'username': 'admin',
            'password': 'admin',
            'secret' : 'admin',
            }
    print(f"connecting to: {host}" )
    config_commands = input("Enter configs: ")
    show_commands = input("Enter show commands: ")
    cfg_cmds = config_commands.split(",")
    show_cmds = show_commands.split(",")
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    output = net_connect.send_config_set(cfg_cmds)
    print(output)
    for cmd in show_cmds:
        output = net_connect.send_command(cmd)
        print(output)

if q4 == "y":
    host = "ceos3"
    device = {
            'device_type': 'arista_eos',
            'ip': host,
            'username': 'admin',
            'password': 'admin',
            'secret' : 'admin',
            }
    print(f"connecting to: {host}" )
    config_commands = input("Enter configs: ")
    show_commands = input("Enter show commands: ")
    cfg_cmds = config_commands.split(",")
    show_cmds = show_commands.split(",")
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    output = net_connect.send_config_set(cfg_cmds)
    print(output)
    for cmd in show_cmds:
        output = net_connect.send_command(cmd)
        print(output)

