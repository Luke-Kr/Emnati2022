#!/bin/bash
cd "$(dirname "$0")"
for i in {1..100}
do
echo "Running iteration $i"
# Might need to adjust the path to your Python script
python3 flee/runscripts/run.py input_csv source_data 13 simsetting.yml > runs/out$i.csv
done
