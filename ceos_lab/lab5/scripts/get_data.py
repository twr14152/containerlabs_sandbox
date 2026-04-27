#!/home/toddriemenschneider/github_repos/containerlabs_sandbox/myenv/bin/python

from jsonrpclib import Server
import ssl
import json

import sqlite3
import datetime


ssl._create_default_https_context = ssl._create_unverified_context


hosts = ["ceos1", "ceos2", "ceos3"]

commands = "show hostname, show ip interface brief, show version" 
cmds = [c.strip() for c in commands.split(",")]

def get_data(hosts):
    
    conn = sqlite3.connect("/home/toddriemenschneider/github_repos/containerlabs_sandbox/ceos_lab/lab5/netwk.db")
    cursor = conn.cursor()


    for host in hosts:
        switch = Server(f"https://admin:admin@{host}/command-api")
        response = switch.runCmds( 1, cmds )
        print(json.dumps(response, indent=2))
        hostname = response[0]["hostname"]
        mgmt_ip = response[1]["interfaces"]["Management0"]["interfaceAddress"]["ipAddr"]["address"]
        os_version = response[2]["internalVersion"]
        #print(type(response))
        print(f"The data that was captured for host is {hostname}")
        print(f"The management ip is {mgmt_ip}")
        print(f"The os version is {os_version}")


        try:
            last_seen = datetime.datetime.now().isoformat()
            cursor.execute("""INSERT INTO devices (hostname, mgmt_ip, os_version, last_seen)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(hostname) DO UPDATE SET
            mgmt_ip=excluded.mgmt_ip,
            os_version=excluded.os_version,
                           last_seen=excluded.last_seen""",
                           (hostname, mgmt_ip, os_version, last_seen))
            #cursor.execute("INSERT INTO devices (hostname, mgmt_ip, os_version) VALUES (?, ?, ?)",(hostname, mgmt_ip, os_version))
            conn.commit()
            print(f"Device {hostname} inserted successfully.")
            print(f"Mgmt_IP {mgmt_ip} inserted successfully.")
            print(f"OS Version {os_version} inserted successfully.")
        except Exception as e:
            print(f"Error adding device: {e}")


def main():
    get_data(hosts)


if __name__ == "__main__":
    main()
