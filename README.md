# etc

small scripts and miscellany 

## domain-ip-enumerator.sh 

accepts single argument: domain (e.g. google.com)  
pulls / for that domain, finds all domains listed, and gets IPv4 addresses
for those domains. If multiple domains reside at the same IP, there will be
duplicates in the output.

## lan-ps.sh

loads local networks from ifconfig and sends out a pingsweep

## pagepicker-bf.js

Written while working on the hack.darkn3ss.com game (lvl 7). 

pagepicker.php takes a 'nextPageUrl' (3-digit number) and a 'urid' (arbitrary 
string; username or username+password combination). With an adequate 
dictionary, it should be possible to determine all 'nextPageUrl' + 'urid' 
pairs. 

This turned out to be unrelated to the solution of the puzzle, but I  gained 
some valuable knowledge. 
