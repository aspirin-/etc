# etc

small scripts and miscellany 

## domain-ip-enumerator.sh 

accepts single argument: domain (e.g. google.com)  
pulls / for that domain, finds all domains listed, and gets IPv4 addresses
for those domains. If multiple domains reside at the same IP, there will be
duplicates in the output.

## lan-ps.sh

loads local networks from ifconfig and sends out a pingsweep
