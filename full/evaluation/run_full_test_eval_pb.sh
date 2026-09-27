#!/bin/bash
set -x
cd /home/bdldt_team005/DLDockingBenchSeminar
/usr/local/bin/micromamba run -n diffdock-pocket python3 evaluation/evaluation.py --dataset full_test --output_csv results/full_test_evaluation_with_pb.csv
