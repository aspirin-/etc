#!/bin/bash
# accepts single argument: domain (e.g. google.com)
# pulls / for that domain, finds all domains listed, and gets IPv4 addresses 
# for those domains. If multiple domains reside at the same IP, there will be 
# duplicates in the output. 

wget -qqq "$1" -O /tmp/index.html

grep 'href=' /tmp/index.html \
    | sed 's/.*href=\"//' \
    | cut -d\" -f1 \
    | egrep '\.[a-z]+{2,3}\/' \
    | sed -e 's/.*\/\///' \
    | cut -d'/' -f1 \
    | sort -u \
    | parallel -j 8 host {} \
    | mawk '/has address/ { print $NF }'
