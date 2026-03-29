# ============================================
# RDKit - Additional 10 Features (Separate Code)
# ============================================

import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

# -----------------------------
# Same 100 SMILES
# -----------------------------
smiles_list = [
"CC","CCC","CCCC","CCCCC","C=CC","C=CCC","C=CCCC","C=CC=C","CC=CC","C=C",
"CO","CCO","CCCO","CCCCO","CCCCCO","CC(C)O","CC(C)(C)O","C(CO)O","CC(O)C","CC(O)CO",
"CC(=O)O","CCC(=O)O","CCCC(=O)O","CC(=O)OC","CC(=O)OCC","CCOC(=O)C","CCOC(=O)CC",
"C(C(=O)O)O","C(C(=O)O)CO","CC(C(=O)O)O",
"CN","CCN","CCCN","CCCCN","CNC","CCNC","CCNCC","C(=O)N","CC(=O)N","CCC(=O)N",
"c1ccccc1","Cc1ccccc1","CCc1ccccc1","Oc1ccccc1","Nc1ccccc1","c1ccc(O)cc1",
"c1ccc(N)cc1","c1ccc(C)cc1","c1ccc(Cl)cc1","c1ccc(F)cc1",
"c1ccncc1","c1ccoc1","c1ccsc1","c1cncnc1","c1ncccc1","c1ncccn1",
"c1nccs1","c1ncc[nH]1","c1ccc2ccccc2c1","c1ccc2nc[nH]c2c1",
"C(F)(F)C(F)(F)","C(F)(F)C","CC(F)F","CCC(F)F","CC(C)(F)F","C(F)(F)F",
"CC(F)(F)F","C(F)C(F)","C(F)(F)CC","C(F)(F)CCC",
"CS","CCS","CCCS","C(S)C","CS(=O)C","CS(=O)(=O)C","c1ccsc1","c1ccc(S)cc1",
"c1ccc(S(=O)(=O))cc1","CSCC",
"CN=C","CNC","CNCC","CNC(C)C","CCN(C)C","CCN(CC)CC","CNC(=O)C","CN(C)C=O",
"CN(C)C","CNC(=O)N",
"CCOC","CCOCC","CCOCCC","COC","COCC","COCCC","CC(O)C","CC(O)CC",
"CC(O)CCC","CC(O)CCCC"
]

data = []

for i, smi in enumerate(smiles_list):
    mol = Chem.MolFromSmiles(smi)

    if mol is None:
        continue

    row = {
        "Sample_Name": f"Polymer_{i+1}",
        "SMILES": smi,

        # NEW 10 FEATURES
        "MolMR": Descriptors.MolMR(mol),
        "HeavyAtomMolWt": Descriptors.HeavyAtomMolWt(mol),
        "NHOHCount": Descriptors.NHOHCount(mol),
        "NOCount": Descriptors.NOCount(mol),
        "NumValenceElectrons": Descriptors.NumValenceElectrons(mol),
        "MaxPartialCharge": Descriptors.MaxPartialCharge(mol),
        "MinPartialCharge": Descriptors.MinPartialCharge(mol),
        "MaxAbsPartialCharge": Descriptors.MaxAbsPartialCharge(mol),
        "MinAbsPartialCharge": Descriptors.MinAbsPartialCharge(mol),
        "FpDensityMorgan1": Descriptors.FpDensityMorgan1(mol)
    }

    data.append(row)

df = pd.DataFrame(data)

df.to_excel("rdkit_extra_10_features.xlsx", index=False)

print("Additional 10 features dataset created!")
print("Shape:", df.shape)
