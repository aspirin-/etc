#!/usr/env/python
#
# Note: root is required to send ICMP packets
#
# Dependencies: 
#   netifaces (pip install netifaces) 

import sys
from netifaces import interfaces, ifaddresses, AF_INET
from scapy.all import send, ICMP, IP 

def get_base_addresses(): 
    base_addresses = []
    for iface in interfaces(): 
        inet_info = {}
        if AF_INET in ifaddresses(iface):
            inet_info = ifaddresses(iface)[AF_INET][0]
        if 'broadcast' in inet_info:
            base_addresses.append(inet_info['addr'])
    return base_addresses


base_addresses = get_base_addresses()
print base_addresses

try: 
    send(IP(dst="172.16.8.1")/ICMP())
except Exception, the_exception: 
    print the_exception
