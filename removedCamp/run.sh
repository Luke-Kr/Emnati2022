#!/bin/bash
cd ~/Courses/5284INPR6Y/FabSim3/results/Emnati2022_MinCamp
for i in {1..10}
do
echo "Running iteration $i"
python3 ~/Courses/5284INPR6Y/flee/runscripts/run.py input_csv source_data 41 simsetting.yml > runsL10/out$i.csv
done
