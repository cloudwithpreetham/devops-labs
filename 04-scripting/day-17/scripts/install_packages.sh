#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Error: Please run this script as root."
    echo "Example: sudo ./install_packages.sh"
    exit 1
fi

packages=("nginx" "curl" "wget")

for package in "${packages[@]}"
do
    echo "Checking package: $package"

    if dpkg -s "$package" &> /dev/null; then
        echo "$package is already installed."
    else
        echo "$package is not installed. Installing now..."
        apt update
        apt install -y "$package"

        if [ $? -eq 0 ]; then
            echo "$package installed successfully."
        else
            echo "Failed to install $package."
            exit 1
        fi
    fi

    echo "-------------------------"
done
