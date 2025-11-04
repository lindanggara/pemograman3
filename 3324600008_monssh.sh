#!/bin/bash

while true
do
    if systemctl is-active --quiet ssh
    then
        echo "$(date): SSH service is running."
    else
        echo "$(date): WARNING! SSH service is NOT running!"
    fi
    sleep 10
done
