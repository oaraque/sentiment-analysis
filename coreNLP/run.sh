#!/bin/bash

if [ -z "$1" ]
then
	INPUT="$(pwd)/../data/mydata"
else
	INPUT=$1
fi

if [ -z "$2" ]
then
	OUTPUT="$(pwd)/../data/coreNLP/myout.txt"
else
	OUTPUT=$2
fi

echo "Input from $INPUT"
echo "Output to $OUTPUT"
echo ""

touch ./tmp_input.txt
touch ./tmp_output.txt

python3 preprocess.py $INPUT ./tmp_input.txt

docker run --rm \
	-v $(pwd)/tmp_input.txt:/input.txt \
	-v $(pwd)/tmp_output.txt:/input.txt.out \
	-v $(pwd)/props.properties:/corenlp/props.properties \
	-e -Xmx4g \
	corenlp:latest

python3 read.py ./tmp_output.txt $OUTPUT

rm ./tmp_input.txt ./tmp_output.txt
