#!/usr/env/python
# Note: root is required to send ICMP packets

import sys
from scapy.all import send, ICMP, IP 

send(IP(dst="172.16.8.1")/ICMP())