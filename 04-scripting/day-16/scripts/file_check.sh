#!/bin/bash

read -p "Enter filename: " FILENAME

if [ -f "$FILENAME" ]; then
    echo "File exists: $FILENAME"
else
    echo "File does not exist: $FILENAME"
fi
