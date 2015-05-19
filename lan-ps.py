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


def begin_sequence(base_address): 
    numbers = '1234567890'
    stub = base_address.rstrip(numbers)
    for number in range(254):
        new_ipaddr = stub + str(number + 1)
        result = do_ping(new_ipaddr)
        announce_if_alive(result)


def do_ping(input_address):
    timeout = 0.1
    number_to_send = 1
    ping_result = ping.quiet_ping(input_address, timeout, number_to_send)
    if ping_result[0] == 0: # percent dropped
        return input_address
    else: 
        return None


def announce_if_alive(ping_result):
    if ping_result: 
        print ping_result + " is up"


if __name__ == "__main__": 
    try:
        for address in get_base_addresses(): 
            begin_sequence(address)
    except Exception, the_exception: 
        print the_exception
