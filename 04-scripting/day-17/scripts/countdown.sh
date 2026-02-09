#!/bin/bash

read -p "Enter a number: " number

while [ "$number" -ge 0 ]
do
    echo "$number"
    number=$((number - 1))
done

echo "Done!"
