#!/bin/bash
set -e
set -x

export HOME=/tmp
export MAMBA_ROOT_PREFIX=/opt/micromamba
export TORCH_HOME=/opt/torch_cache
export CUDA_VISIBLE_DEVICES=0
mkdir -p $HOME/.cache/mamba/proc

cd /home/bdldt_team003/DiffDock-Pocket

/usr/local/bin/micromamba run -n diffdock-pocket python -m train \
    --run_name prototype_training \
    --protein_ligand_csv /home/bdldt_team003/DiffDock-Pocket/training_input.csv \
    --split_train /home/bdldt_team003/DiffDock-Pocket/proto_split_train.txt \
    --split_val /home/bdldt_team003/DiffDock-Pocket/proto_split_val.txt \
    --log_dir /home/bdldt_team003/DiffDock-Pocket/workdir \
    --lr 1e-3 \
    --tr_sigma_min 0.1 --tr_sigma_max 5 \
    --rot_sigma_min 0.03 --rot_sigma_max 1.55 \
    --tor_sigma_min 0.03 --sidechain_tor_sigma_min 0.03 \
    --batch_size 2 \
    --ns 60 --nv 10 --num_conv_layers 6 \
    --distance_embed_dim 64 --cross_distance_embed_dim 64 --sigma_embed_dim 64 \
    --dynamic_max_cross --scheduler plateau --scale_by_sigma --dropout 0.1 \
    --sampling_alpha 1 --sampling_beta 1 \
    --remove_hs \
    --c_alpha_max_neighbors 24 --atom_max_neighbors 8 --receptor_radius 15 \
    --num_dataloader_workers 1 \
    --rot_alpha 1 --rot_beta 1 --tor_alpha 1 --tor_beta 1 \
    --val_inference_freq 5 --use_ema --scheduler_patience 30 \
    --n_epochs 3 \
    --all_atom --sh_lmax 1 \
    --pocket_reduction --pocket_buffer 10 \
    --flexible_sidechains --flexdist 3.5 --flexdist_distance_metric prism \
    --use_original_conformer_fallback
