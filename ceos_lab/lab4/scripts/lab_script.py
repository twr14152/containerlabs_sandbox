#!/home/todd/Code_folder/containerlab/containerlabs_sandbox/myenv/bin/python

from netmiko import ConnectHandler 
import sys

devices = ["leaf1a", "leaf1b", "leaf2", "spine1", "spine2"]

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

q2 = input("Login into leaf1a: (y/n)")
q3 = input("Login into leaf1b: (y/n)")
q4 = input("Login into leafb: (y/n)")
q5 = input("Login into spine1: (y/n)")
q6 = input("Login into spine2: (y/n)")


if len(q2) < 1: q2 == "n"
if len(q3) < 1: q3 == "n"
if len(q4) < 1: q4 == "n"
if len(q5) < 1: q5 == "n"
if len(q6) < 1: q6 == "n"

if q2 == "y":
    host = "leaf1a"
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
    host = "leaf1b"
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
    host = "leaf2"
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

if q5 == "y":
    host = "spine1"
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

if q6 == "y":
    host = "spine2"
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




