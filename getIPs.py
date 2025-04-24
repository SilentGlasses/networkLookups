#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket

def get_ips_from_file(file_path):
    ips = {}
    try:
        with open(file_path, 'r') as file:
            hostname_list = file.read().splitlines()

        for hostname in hostname_list:
            try:
                ip = socket.gethostbyname(hostname)
                ips[hostname] = ip
            except socket.gaierror:
                ips[hostname] = "IP address not found"
    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return ips

if __name__ == "__main__":
    file_path = "hosts.txt"

    ips = get_ips_from_file(file_path)

    if ips:
        print("Hostname\tIP Address")
        for hostname, ip in ips.items():
            print(f"{hostname}\t{ip}")
