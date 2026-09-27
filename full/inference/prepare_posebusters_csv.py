import os, csv

SRC_DIR = "/home/bdldt_team005/DLDockingBenchSeminar/full_data/posebusters_filtered_raw/posebusters_filtered"
OUT_CSV = "/home/bdldt_team005/DLDockingBenchSeminar/inference/posebusters_filtered_input.csv"

names = sorted(set(f.replace("_ligand.sdf", "").replace("_protein.pdb", "")
                    for f in os.listdir(SRC_DIR) if f.endswith("_ligand.sdf") or f.endswith("_protein.pdb")))

rows = []
for name in names:
    protein = os.path.join(SRC_DIR, f"{name}_protein.pdb")
    ligand = os.path.join(SRC_DIR, f"{name}_ligand.sdf")
    if os.path.isfile(protein) and os.path.isfile(ligand):
        rows.append({"complex_name": name, "experimental_protein": protein, "ligand": ligand})

with open(OUT_CSV, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["complex_name", "experimental_protein", "ligand"])
    w.writeheader()
    w.writerows(rows)

print(f"Wrote {len(rows)} rows to {OUT_CSV}")
