#!/bin/bash
set -x
export HOME=/tmp
export MAMBA_ROOT_PREFIX=/opt/micromamba
mkdir -p $HOME/.cache/mamba/proc
cd /home/bdldt_team005/DLDockingBenchSeminar
/usr/local/bin/micromamba run -n diffdock-pocket pip install posebusters --break-system-packages -q
/usr/local/bin/micromamba run -n diffdock-pocket python3 evaluation/evaluation.py --dataset posebusters_filtered --output_csv results/posebusters_filtered_evaluation_3poses.csv
