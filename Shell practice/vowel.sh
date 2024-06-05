#!/bin/bash

# Check if a string is provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <string>"
  exit 1
fi

# Get the input string from the command line argument
input_string=$1

# Use grep to find and print vowels in the string
vowels=$(echo "$input_string" | grep -o -i '[aeiou]')

# Check if any vowels were found and print them
if [ -n "$vowels" ]; then
  echo "Vowels found: $vowels"
else
  echo "No vowels found."
fi