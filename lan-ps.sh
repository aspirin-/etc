#!/bin/bash
# loads local networks from ifconfig and sends out a pingsweep

for thing in $( \
    ifconfig \
    | grep 'Bcast' \
    | cut -d':' -f2 \
    | sed 's/[0-9]\+[[:space:]].*$//g' \
    ) ; do 
    seq 1 255 \
        | parallel -j 8 fping -q -C1 -t100 "$thing"{} 2>&1 \
        | grep -v '-'
done
