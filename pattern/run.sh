#!/bin/bash

if [ -z "$1" ]
then
	INPUT="$(pwd)/../data/mydata"
else
	INPUT=$1
fi

if [ -z "$2" ]
then
	OUTPUT="$(pwd)/../data/pattern/myout.txt"
else
	OUTPUT=$2
fi

echo "Input from $INPUT"
echo "Output to $OUTPUT"
echo ""


docker run --rm \
	-v $INPUT:/input.txt \
	-v $OUTPUT:/output.txt \
	pattern:latest
