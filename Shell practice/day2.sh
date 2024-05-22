#!/bin/bash
DIR="./test"

if [ -d "$DIR" ]; then
    echo "directory $DIR exists"
else
    echo "directory $DIR not exists creating new one"
    mkdir -p "$DIR"
fi
