#!/bin/bash
cd "$(dirname "$0")"
for i in {1..100}
do
echo "Running iteration $i"
# Might need to adjust the path to your Python script
python3 flee/runscripts/run.py input_csv source_data 41 simsetting.yml > runsE1L/out$i.csv
done
