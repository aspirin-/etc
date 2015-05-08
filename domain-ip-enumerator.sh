#!/bin/bash

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
