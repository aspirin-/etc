#!/usr/env/python
#
# Note: root is required to send ICMP packets
#
# Dependencies: 
#   netifaces (pip install netifaces) 
#   ping (pip install ping)

import sys
from netifaces import interfaces, ifaddresses, AF_INET
import ping 

def get_base_addresses(): 
    base_addresses = []
    for iface in interfaces(): 
    # netifaces.interfaces() returns a list of the system's network interfaces
        inet_info = {}
        if AF_INET in ifaddresses(iface):
            inet_info = ifaddresses(iface)[AF_INET][0]
            # ifaddresses(i...INET] is a single-entry list, containing a 
            # dictionary. If the interface is not being used, the dict will 
            # be empty. 
            # When ifaddresses(i...INET][0] is not empty, it contains  
            # broadcast, netmask, addr
        if 'broadcast' in inet_info:
            base_addresses.append(inet_info['addr'])
            # loopback does not have a 'broadcast' entry, so this appears to 
            # be an acceptable way to include only non-lo interfaces. 
    return base_addresses


# Next: Define sequencing
# input is list of base addresses; from each base address, strip last octet; 
# for each address in [first-three-octets].0/24, icmp_echo()


# Next: Define icmp echo function
def do_ping(input_address):
    timeout = 0.2
    number_to_send = 1
    ping_result = ping.quiet_ping(input_address, timeout, number_to_send)
    if ping_result[0] == 0: # percent dropped
        return input_address
    else: 
        return None


def announce_if_alive(ping_result):
    if ping_result: 
        print ping_result + " is up"


base_addresses = get_base_addresses()
print base_addresses

try: 
    destin = "192.168.1.8"
    trial = do_ping(destin)
    announce_if_alive(trial)
except Exception, the_exception: 
    print the_exception
