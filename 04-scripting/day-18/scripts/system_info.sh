#!/bin/bash
set -euo pipefail

print_section() {
    echo
    echo "========================================"
    echo "$1"
    echo "========================================"
}

show_hostname_os() {
    print_section "Hostname and OS Information"

    echo "Hostname: $(hostname)"
    echo "Operating System:"
    cat /etc/os-release | grep -E "PRETTY_NAME|VERSION="
}

show_uptime() {
    print_section "System Uptime"

    uptime
}

show_disk_usage() {
    print_section "Top 5 Disk Usage"

    df -h | sort -hr -k 5 | head -n 5
}

show_memory_usage() {
    print_section "Memory Usage"

    free -h
}

show_top_cpu_processes() {
    print_section "Top 5 CPU Consuming Processes"

    ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6
}

main() {
    echo "System Information Report"
    echo "Generated on: $(date)"

    show_hostname_os
    show_uptime
    show_disk_usage
    show_memory_usage
    show_top_cpu_processes

    echo
    echo "Report completed successfully."
}

main
