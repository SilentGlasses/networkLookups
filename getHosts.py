#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket

def get_hostnames_from_file(file_path):
    hostnames = {}
    try:
        with open(file_path, 'r') as file:
            ip_list = file.read().splitlines()

        for ip in ip_list:
            try:
                hostname, _, _ = socket.gethostbyaddr(ip)
                hostnames[ip] = hostname
            except socket.herror:
                hostnames[ip] = "Hostname not found"
    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return hostnames

if __name__ == "__main__":
    file_path = "ips.txt"

    hostnames = get_hostnames_from_file(file_path)

    if hostnames:
        print("IP Address\tHostname")
        for ip, hostname in hostnames.items():
            print(f"{ip}\t{hostname}")
