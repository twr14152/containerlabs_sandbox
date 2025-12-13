#!/home/todd/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/lab_env/bin/python3.12

from netmiko import ConnectHandler 

devices = ["clab-lab3-ceos1", "clab-lab3-ceos2", "clab-lab3-ceos3"]

q1 = input("Login into all devices?: (y/n)")
q2 = input("Login into clab-lab3-ceos1: (y/n)")
q3 = input("Login into clab-lab3-ceos2: (y/n)")
q4 = input("Login into clab-lab3-ceos3: (y/n)")

if len(q1) < 1: q1 == "n"
if len(q2) < 1: q2 == "n"
if len(q3) < 1: q3 == "n"
if len(q4) < 1: q4 == "n"

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

elif q2 == "y":
    host = "clab-lab3-ceos1"
    device = {
            'device_type': 'arista_eos',
            'ip': host,
            'username': 'admin',
            'password': 'admin',
            'secret' : 'admin',
            }
    print(f"connecting to: {host}" )
#   commands = input("Enter commands: ")
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


elif q3 == "y":
    host = "clab-lab3-ceos2"
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

elif q4 == "y":
    host = "clab-lab3-ceos3"
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

