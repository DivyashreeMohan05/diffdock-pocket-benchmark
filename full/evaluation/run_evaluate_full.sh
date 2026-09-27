#!/bin/bash
set -e
set -x

export HOME=/tmp
export MAMBA_ROOT_PREFIX=/opt/micromamba
mkdir -p $HOME/.cache/mamba/proc

cd /home/bdldt_team005/DLDockingBenchSeminar/inference

/usr/local/bin/micromamba run -n diffdock-pocket python3 -u evaluate_files.py \
    --complex_names_path /home/bdldt_team005/DLDockingBenchSeminar/inference/full_test_names.txt \
    --data_dir /home/bdldt_team005/DLDockingBenchSeminar/full_test/full_sealed_test_eval \
    --results_path /home/bdldt_team005/DLDockingBenchSeminar/results/full_test_predictions \
    --results_path_flex /home/bdldt_team005/DLDockingBenchSeminar/results/full_test_predictions \
    --all_dirs_in_results \
    --num_predictions 1 \
    --protein_file protein_refined
