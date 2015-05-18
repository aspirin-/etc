#!/usr/env/python
#
# Note: root is required to send ICMP packets
#
# Dependencies: 
#   netifaces (pip install netifaces) 

import sys
from netifaces import interfaces, ifaddresses, AF_INET
from scapy.all import send, ICMP, IP 

send(IP(dst="172.16.8.1")/ICMP())
