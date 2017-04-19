#!/bin/bash -e

# raspi-img-writer_mac.sh
# requires image location. Shows disks and lets you choose. 
# BE CAREFUL. 

# Only one argument, RasPi image location; export so subshells can access
readonly RASPI_IMG="$1"
export RASPI_IMG

show_disks(){
    # show disks so user can see what their options are
    printf "Showing disks:\n\n"
    diskutil list
}

choose_disk(){
    # read user's input and return it
    user_input=$(
        read -p "Choose disk IDENTIFIER (do not type full path): "
        )
    echo "/dev/$user_input"
}

warn_before_continue(){ # chosen_disk
    # pause and ensure the user's choice is really what they want
    # This is the Point of No Return!
    chosen_disk="$1"
    printf "WARNING: Image %s will be written to %s. This cannot be undone.\n" "$RASPI_IMG" "$chosen_disk"
    read -s -n1 -p "Press ENTER to continue; CTRL-C to exit..."
}

write_img_to_disk(){ # chosen_disk
    # perform action
    chosen_disk="$1"
    export chosen_disk
    printf "Writing %s to %s...\n" "$RASPI_IMG" "$chosen_disk"
    img_filesize=$(
        get_img_filesize
        )

    raw_disk=$(
        echo "$chosen_disk" \
        | sed 's./dev/./dev/r'
        )

    # sudo -v to grab sudo creds without interrupting dd
    # sudo -v
    # dd bs=1m if="$RASPI_IMG" \
    # | pv -s "$img_filesize" \
    # | sudo dd bs=1m of="$raw_disk"

    printf "reading from %s...\n" "$RASPI_IMG"
    printf "writing to %s...\n" "$raw_disk"
    printf "complete.\n"
}

get_img_filesize(){
    # retrieve file size of the specified RASPI_IMG
    echo "$(
        ls -l "$RASPI_IMG" \
        | awk '{ print $5 }'
        )"
}

main(){
    if [ -z "$RASPI_IMG"]; then 
        printf "No image specified. Exiting...\n"
        exit 1
    else
        show_disks
        chosen_disk=choose_disk
        warn_before_continue "$chosen_disk"
        write_img_to_disk "$chosen_disk"
    fi
}

main