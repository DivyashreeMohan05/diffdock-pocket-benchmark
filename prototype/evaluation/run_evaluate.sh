#!/bin/bash
set -e
set -x

export HOME=/tmp
export MAMBA_ROOT_PREFIX=/opt/micromamba
mkdir -p $HOME/.cache/mamba/proc

cd /home/bdldt_team005/DLDockingBenchSeminar/DiffDock-Pocket

/usr/local/bin/micromamba run -n diffdock-pocket python3 -u evaluate_files.py \
    --complex_names_path proto_test_names_good.txt \
    --data_dir eval_data_dir \
    --results_path results/inference_files \
    --results_path_flex results/inference_files \
    --all_dirs_in_results \
    --num_predictions 40 \
    --protein_file protein_refined
