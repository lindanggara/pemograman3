#!/bin/bash

while true; do
    if ! systemctl is-active --quiet ssh; then
        echo "[$(date)] ALERT: Service ssh is down!"
    else
        echo "[$(date)] Service ssh is running."
    fi
    sleep 10
done
