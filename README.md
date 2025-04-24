# networkLookups

For when you need to lookup up multiple Names or IPs of hosts using either as a base, mainly for when manually running `ping` or `dig` would not suffice.

## Requirements

* `python3`
* `socket`
* `subprocess`

## Usage

Using these scripts is super easy:

- **To get hostnames from a list of IP addresses**:
    - Add your list of IPs in the `ips.txt` file
    - Run the `getHosts.py` script
- **To get IP addresses from a list of hostnames**:
    - Add your list of IPs in the `hosts.txt` file
    - Run the `getIPs.py` script
- **To get Site24x7 Poller IPs for allow listing**:
    - Edit the `pollers.txt` file as needed
    - Run the `getPollers.py` script
    - You can get a list of their endpoints [here](https://support.site24x7.com/portal/en/kb/articles/domain-configurations-for-location-server-ips)
