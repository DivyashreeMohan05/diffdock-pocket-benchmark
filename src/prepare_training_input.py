#!/usr/bin/env python3
import csv
import os

BASE_DIR  = "/home/bdldt_team003/DLDockingBenchSeminar"
TRAIN_DATA_DIR = os.path.join(BASE_DIR, "full_data", "full_sealed_train")
VAL_DATA_DIR  = os.path.join(BASE_DIR, "full_data", "full_sealed_val")
TRAIN_CSV  = os.path.join(BASE_DIR, "full_data", "full_sealed_train.csv")
VAL_CSV = os.path.join(BASE_DIR, "full_data", "full_sealed_val.csv")
TRAINING_DIR = os.path.join(BASE_DIR, "training")
OUTPUT_CSV = os.path.join(TRAINING_DIR, "training_input_full.csv")
TRAIN_SPLIT = os.path.join(TRAINING_DIR, "full_split_train.txt")
VAL_SPLIT = os.path.join(TRAINING_DIR, "full_split_val.txt")
os.makedirs(TRAINING_DIR, exist_ok=True)

def build_name(row):
    pdb = row["PDBID"].strip()
    ligname = row["Ligand Name"].strip()
    chain = row["Ligand Chain"].strip()
    resraw = row["Ligand Residue Number"].strip()
    try:
        resnum = str(int(float(resraw)))
    except ValueError:
        resnum = resraw
    return f"{pdb}_{ligname}_{chain}_{resnum}"

def process_csv(csv_path, data_dir, writer, split_names, missing_log):
    count = 0
    skipped = 0
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name    = build_name(row)
            protein = os.path.join(data_dir, f"{name}_protein_refined.pdb")
            ligand  = os.path.join(data_dir, f"{name}_ligand_refined.sdf")
            if not os.path.isfile(protein) or not os.path.isfile(ligand):
                missing_log.append(name)
                skipped += 1
                continue
            writer.writerow([name, protein, ligand])
            split_names.append(name)
            count += 1
    return count, skipped

print(" Preparing DiffDock training input ")
print(f"Train data dir : {TRAIN_DATA_DIR}")
print(f"Val data dir   : {VAL_DATA_DIR}")
print()

missing = []
train_names = []
val_names   = []

with open(OUTPUT_CSV, "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["complex_name", "experimental_protein", "ligand"])

    print("Processing train split...")
    t_count, t_skip = process_csv(TRAIN_CSV, TRAIN_DATA_DIR, writer, train_names, missing)
    print(f"  Written : {t_count}  |  Skipped (missing files): {t_skip}")

    print("Processing val split...")
    v_count, v_skip = process_csv(VAL_CSV, VAL_DATA_DIR, writer, val_names, missing)
    print(f"  Written : {v_count}  |  Skipped (missing files): {v_skip}")

with open(TRAIN_SPLIT, "w") as f:
    f.write("\n".join(train_names))

with open(VAL_SPLIT, "w") as f:
    f.write("\n".join(val_names))

print()
print(f"Output CSV      : {OUTPUT_CSV}  ({t_count + v_count} rows)")
print(f"Train split file: {TRAIN_SPLIT}  ({len(train_names)} complexes)")
print(f"Val split file  : {VAL_SPLIT}  ({len(val_names)} complexes)")

if missing:
    print(f"\nWARNING: {len(missing)} complexes had missing files and were skipped.")
    print("First 10 missing:")
    for m in missing[:10]:
        print(f"  {m}")
    missing_path = os.path.join(TRAINING_DIR, "missing_complexes.txt")
    with open(missing_path, "w") as f:
        f.write("\n".join(missing))
    print(f"Full missing list saved to: {missing_path}")
else:
    print("\nAll complexes found — no missing files!")

print("\nDone.")
