#!/usr/bin/python3.12

import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


username = "admin"
password = "NokiaSrl1!"

def all_nodes():
    nodes = ["leaf1", "leaf2", "spine1", "spine2"]
    commands = input("Enter commands seperated by ',': ")
    cli_commands = commands.split(",")
    for node in nodes:
        url = f"https://{node}/jsonrpc"
        payload = {
                "jsonrpc": "2.0",
                "method": "cli",
                "params": {
                    "commands": cli_commands,
                    "output-format": "json" # "text" is bascially unreadable dont use....
                },
                "id":1
        }
        try:
            print(f"Connecting to {node}")
            response = requests.post(
                    url,
                    data=json.dumps(payload),
                    auth=(username, password),
                    headers={"Content-Type": "application/json"},
                    verify=False,
                    timeout=5
                    )
            print(response.status_code)
            print(json.dumps(response.json(), indent=2))
            #clean_response(response.json(), node)
        except requests.exceptions.RequestException as e:
            print("Error: ", e)

def node():
    node = input("Enter node: ")
    url = f"https://{node}/jsonrpc"
    
    commands = input("Enter commands seperated by ',': ")
    cli_commands = commands.split(",")

    payload = {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
                "commands": cli_commands,
                "output-format": "json" # "text" is bascially unreadable dont use....
                },
            "id":1
        }
    try:
        print(f"Connecting to {node}")
        response = requests.post(
                url,
                data=json.dumps(payload),
                auth=(username, password),
                headers={"Content-Type": "application/json"},
                verify=False,
                timeout=5
                )
        print(response.status_code)
        print(json.dumps(response.json(), indent=2))
    except requests.exceptions.RequestException as e:
        print("Error: ", e)


def clean_response(resp, node_name):
    # Extract the embedded JSON string
    text_blob = resp["result"][0]["text"]

    # Some devices prepend an empty {} before the real JSON
    # Split and keep the last JSON object
    json_str = text_blob.strip().split("}\n{", 1)

    if len(json_str) == 2:
        json_str = "{" + json_str[1]
    else:
        json_str = json_str[0]

    parsed = json.loads(json_str)

    print(f"\n===== {node_name} =====")
    print(json.dumps(parsed, indent=2))




def main():
    ans = input("Log in to all nodes (y/n): ")
    if ans == "y":
        all_nodes()
    else:
        node()



if __name__ == "__main__":
    main()


