#!/bin/bash

greet() {
    echo "Hello, $1!"
}

add() {
    local num1=$1
    local num2=$2
    local sum=$((num1 + num2))

    echo "Sum: $sum"
}

greet "Preetham"
add 10 20
