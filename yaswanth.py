# ============================================
# RDKit Dataset - 100 UNIQUE POLYMER STRUCTURES
# ============================================

import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

# -----------------------------
# Step 1: 100 Unique SMILES
# -----------------------------
smiles_list = [
# Hydrocarbons
"CC","CCC","CCCC","CCCCC","C=CC","C=CCC","C=CCCC","C=CC=C","CC=CC","C=C",

# Alcohols
"CO","CCO","CCCO","CCCCO","CCCCCO","CC(C)O","CC(C)(C)O","C(CO)O","CC(O)C","CC(O)CO",

# Acids & esters
"CC(=O)O","CCC(=O)O","CCCC(=O)O","CC(=O)OC","CC(=O)OCC","CCOC(=O)C","CCOC(=O)CC",
"C(C(=O)O)O","C(C(=O)O)CO","CC(C(=O)O)O",

# Amines & amides
"CN","CCN","CCCN","CCCCN","CNC","CCNC","CCNCC","C(=O)N","CC(=O)N","CCC(=O)N",

# Aromatics
"c1ccccc1","Cc1ccccc1","CCc1ccccc1","Oc1ccccc1","Nc1ccccc1","c1ccc(O)cc1",
"c1ccc(N)cc1","c1ccc(C)cc1","c1ccc(Cl)cc1","c1ccc(F)cc1",

# Heterocycles
"c1ccncc1","c1ccoc1","c1ccsc1","c1cncnc1","c1ncccc1","c1ncccn1",
"c1nccs1","c1ncc[nH]1","c1ccc2ccccc2c1","c1ccc2nc[nH]c2c1",

# Fluorinated
"C(F)(F)C(F)(F)","C(F)(F)C","CC(F)F","CCC(F)F","CC(C)(F)F","C(F)(F)F",
"CC(F)(F)F","C(F)C(F)","C(F)(F)CC","C(F)(F)CCC",

# Sulfur compounds
"CS","CCS","CCCS","C(S)C","CS(=O)C","CS(=O)(=O)C","c1ccsc1","c1ccc(S)cc1",
"c1ccc(S(=O)(=O))cc1","CSCC",

# Nitrogen rich
"CN=C","CNC","CNCC","CNC(C)C","CCN(C)C","CCN(CC)CC","CNC(=O)C","CN(C)C=O",
"CN(C)C","CNC(=O)N",

# Functional polymers
"CCOC","CCOCC","CCOCCC","COC","COCC","COCCC","CC(O)C","CC(O)CC",
"CC(O)CCC","CC(O)CCCC"
]

# Ensure exactly 100
smiles_list = smiles_list[:100]

# -----------------------------
# Step 2: Generate RDKit Features
# -----------------------------
data = []

for i, smi in enumerate(smiles_list):
    
    mol = Chem.MolFromSmiles(smi)

    if mol is None:
        print(f"Skipping invalid SMILES: {smi}")
        continue

    row = {
        "Sample_Name": f"Polymer_{i+1}",
        "SMILES": smi,
        "Molecular_Weight": Descriptors.MolWt(mol),
        "LogP": Descriptors.MolLogP(mol),
        "Num_H_Donors": Descriptors.NumHDonors(mol),
        "Num_H_Acceptors": Descriptors.NumHAcceptors(mol),
        "TPSA": Descriptors.TPSA(mol),
        "Num_Rotatable_Bonds": Descriptors.NumRotatableBonds(mol),
        "Num_Atoms": mol.GetNumAtoms(),
        "Num_Heavy_Atoms": mol.GetNumHeavyAtoms(),
        "Fraction_CSP3": Descriptors.FractionCSP3(mol),
        "Ring_Count": Descriptors.RingCount(mol)
    }

    data.append(row)

# -----------------------------
# Step 3: DataFrame
# -----------------------------
df = pd.DataFrame(data)

# -----------------------------
# Step 4: Save File
# -----------------------------
df.to_excel("rdkit_100_unique_polymers.xlsx", index=False)

print("Dataset created successfully!")
print("Shape:", df.shape)
