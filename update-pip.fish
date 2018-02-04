#!/usr/bin/env fish

function pip2update
    pip2 install -U pip
    pip2 freeze --local \
    | grep -v '^\-e' \
    | cut -d = -f 1  \
    | xargs -n1 pip2 install -U
end

function pip3update
    pip3 install -U pip
    pip3 freeze --local \
    | grep -v '^\-e' \
    | cut -d = -f 1  \
    | xargs -n1 pip3 install -U
end

function main
    begin;
    	pip2update
        pip3update
    end; or begin;
        sudo -v
        sudo -EH pip2update
        sudo -EH pip3update
    end
end

main
