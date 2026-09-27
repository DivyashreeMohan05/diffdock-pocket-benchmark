import csv

SRC = "/home/bdldt_team005/DLDockingBenchSeminar/full_test/full_sealed_test.csv"
DST = "/home/bdldt_team005/DLDockingBenchSeminar/data/full_test.csv"

def build_name(row):
    pdb = row['PDBID'].strip()
    ligname = row['Ligand Name'].strip()
    chain = row['Ligand Chain'].strip()
    resraw = row['Ligand Residue Number'].strip()
    try:
        resnum = str(int(float(resraw)))
    except ValueError:
        resnum = resraw
    return f'{pdb}_{ligname}_{chain}_{resnum}'

rows_out = []
with open(SRC) as f:
    for row in csv.DictReader(f):
        name = build_name(row)
        rows_out.append({
            'ligand_file_name': f'{name}_ligand_refined.sdf',
            'protein_file_name': f'{name}_protein_refined.pdb',
            'Year': row['Year'],
            'Log Binding Affinity': row['Log Binding Affinity'],
            'Binding Affinity Measurement': row['Binding Affinity Measurement'],
            'PDBID': row['PDBID'],
        })

with open(DST, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['ligand_file_name','protein_file_name','Year','Log Binding Affinity','Binding Affinity Measurement','PDBID'])
    w.writeheader()
    w.writerows(rows_out)

print(f'Wrote {len(rows_out)} rows to {DST}')
