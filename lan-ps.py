#!/usr/env/python

import sys
from scapy.all import send, ICMP, IP 

send(IP(dst="172.16.8.1")/ICMP())