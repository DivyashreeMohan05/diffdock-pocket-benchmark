#!/bin/bash
set -x
cd /home/bdldt_team005/DLDockingBenchSeminar
/usr/local/bin/micromamba run -n diffdock-pocket python3 evaluation/evaluation.py --dataset posebusters_filtered --output_csv results/posebusters_filtered_evaluation.csv
