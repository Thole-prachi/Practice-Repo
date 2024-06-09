#! /bin/bash
echo "enter company: $1"
echo "enter project group:  $2"

#!/bin/bash
DIR="./test"

if [ -d "$DIR" ]; then
    echo "directory $DIR exists"
else
    echo "directory $DIR not exists creating new one"
    mkdir -p "$DIR"
fi

#!/bin/bash

File="test.txt"
sed -i 's/Hello this is practice test file to get the details/I am forgiven/g' "$File"

#!/bin/bash
FILE="file.txt"
sed -i 's/old_string/new_string/g' "$FILE"

#!/bin/bash

sum = 0

for ((i = 0;i<=100;i++))
do
    sum=$((sum+i))
done

echo "the sum of 1-100 is : $sum"