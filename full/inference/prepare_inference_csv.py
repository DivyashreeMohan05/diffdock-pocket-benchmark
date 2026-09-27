#!/usr/bin/env python3

import csv
import os

BASE_DIR = "/home/bdldt_team005/DLDockingBenchSeminar"
TEST_DATA_DIR = os.path.join(BASE_DIR, "full_test", "full_sealed_test")
TEST_CSV = os.path.join(BASE_DIR, "full_test", "full_sealed_test.csv")
OUTPUT_CSV  = os.path.join(BASE_DIR, "inference", "inference_input_full.csv")

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

print(" Preparing DiffDock inference input")
print(f"Test data dir : {TEST_DATA_DIR}")
print(f"Test CSV      : {TEST_CSV}")
print()

rows_out = []
skipped  = []

with open(TEST_CSV, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name    = build_name(row)
        protein = os.path.join(TEST_DATA_DIR, f"{name}_protein_refined.pdb")
        ligand  = os.path.join(TEST_DATA_DIR, f"{name}_ligand_refined.sdf")

        if not os.path.isfile(protein):
            skipped.append(("missing protein", protein))
            continue
        if not os.path.isfile(ligand):
            skipped.append(("missing ligand", ligand))
            continue

        rows_out.append({
            "complex_name": name,
            "experimental_protein": protein,
            "ligand": ligand,
        })

os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

with open(OUTPUT_CSV, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["complex_name", "experimental_protein", "ligand"])
    writer.writeheader()
    writer.writerows(rows_out)

print(f"Wrote {len(rows_out)} rows to {OUTPUT_CSV}")
if skipped:
    print(f"WARNING: skipped {len(skipped)} rows due to missing files:")
    for reason, path in skipped[:10]:
        print(f"  {reason}: {path}")
    if len(skipped) > 10:
        print(f"  ... and {len(skipped) - 10} more")
else:
    print("All test complexes found — no missing files!")
print("\nDone.")
