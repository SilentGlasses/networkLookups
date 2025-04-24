#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess

def dig_domains_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print("  site24x7_ips = [")
            for line in file:
                domain = line.strip()
                try:
                    result = subprocess.run(["dig", "+noall", "+short", domain], capture_output=True, text=True, check=True)
                    ip_addresses = result.stdout.strip().split('\n')

                    for ip in ip_addresses:
                        print(f"    \"{ip}\"")
                except subprocess.CalledProcessError:
                    print(f"Unable to resolve the domain: {domain}")
            print("  ]")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    file_path = "pollers.txt"  # Replace with the path to your text file
    dig_domains_from_file(file_path)
