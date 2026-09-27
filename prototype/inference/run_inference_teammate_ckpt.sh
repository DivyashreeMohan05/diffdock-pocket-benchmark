#!/bin/bash
set -e
set -x

export HOME=/tmp
export MAMBA_ROOT_PREFIX=/opt/micromamba
export TORCH_HOME=/opt/torch_cache
export CUDA_VISIBLE_DEVICES=0
mkdir -p $HOME/.cache/mamba/proc

cd /home/bdldt_team005/DLDockingBenchSeminar/DiffDock-Pocket

/usr/local/bin/micromamba run -n diffdock-pocket python inference.py \
    --protein_ligand_csv /home/bdldt_team005/DLDockingBenchSeminar/DiffDock-Pocket/inference_input.csv \
    --out_dir /home/bdldt_team005/DLDockingBenchSeminar/DiffDock-Pocket/results/prototype_teammate_checkpoint \
    --model_dir /home/bdldt_team005/DLDockingBenchSeminar/DiffDock-Pocket/teammate_checkpoint \
    --ckpt best_ema_model.pt \
    --filtering_model_dir /home/bdldt_team005/DLDockingBenchSeminar/DiffDock-Pocket/confidence_model \
    --batch_size 8 \
    --samples_per_complex 40 \
    --keep_local_structures
