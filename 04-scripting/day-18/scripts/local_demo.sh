#!/bin/bash

local_variable_demo() {
    local name="Inside Function"
    echo "Local variable value: $name"
}

regular_variable_demo() {
    city="Mangalore"
    echo "Regular variable inside function: $city"
}

local_variable_demo

echo "Trying to access local variable outside function:"
echo "name value outside function: ${name:-Not accessible}"

echo

regular_variable_demo

echo "Trying to access regular variable outside function:"
echo "city value outside function: $city"
