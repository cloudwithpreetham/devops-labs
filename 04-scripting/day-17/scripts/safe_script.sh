#!/bin/bash

set -e

mkdir /tmp/devops-test || echo "Directory already exists"

cd /tmp/devops-test || {
    echo "Failed to enter /tmp/devops-test"
    exit 1
}

touch devops-file.txt || {
    echo "Failed to create file"
    exit 1
}

echo "File created successfully inside /tmp/devops-test"
