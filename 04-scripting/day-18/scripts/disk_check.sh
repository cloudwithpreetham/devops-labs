#!/bin/bash

check_disk() {
    echo "Disk usage for root filesystem:"
    df -h /
}

check_memory() {
    echo "Memory usage:"
    free -h
}

main() {
    echo "===== Disk Check ====="
    check_disk

    echo
    echo "===== Memory Check ====="
    check_memory
}

main
