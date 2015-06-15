#!/bin/bash 

# DNS Transfer test. Takes 1 argument: domain
# e.g.: dnsXtest.sh google.com

readonly DOMAIN="$1"

function get_nameservers { # 1=domain 
    local nameservers=$(
        host -t ns "$1" \
        | mawk '{ print $4 }' \
        | sed 's/.$//'
        )
    echo "$nameservers"
}

function zone_transfer { # 1=domain, 2=nameserver
    host -l "$1" "$2"
}

function main {  
    for nameserver in $(get_nameservers "$DOMAIN"); do 
        zone_transfer "$DOMAIN" "$nameserver"
    done
}

main 
