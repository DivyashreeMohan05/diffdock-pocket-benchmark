#!/bin/bash
set -e
set -x
export MAMBA_ROOT_PREFIX=/opt/micromamba
export TORCH_HOME=/opt/torch_cache
export CUDA_VISIBLE_DEVICES=0
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512
mkdir -p /tmp/.cache/mamba/proc
cd /home/bdldt_team005/DLDockingBenchSeminar/inference

/usr/local/bin/micromamba run -n diffdock-pocket python inference.py \
  --protein_ligand_csv /home/bdldt_team005/DLDockingBenchSeminar/inference/posebusters_filtered_input.csv \
  --model_dir /home/bdldt_team005/DLDockingBenchSeminar/training/workdir/full_training \
  --ckpt best_ema_model.pt \
  --filtering_model_dir /home/bdldt_team005/DLDockingBenchSeminar/DiffDock-Pocket/confidence_model \
  --out_dir /home/bdldt_team005/DLDockingBenchSeminar/results/posebusters_filtered_predictions_3poses \
  --inference_steps 20 \
  --samples_per_complex 3 \
  --batch_size 4 \
  --actual_steps 18 \
  --no_final_step_noise
