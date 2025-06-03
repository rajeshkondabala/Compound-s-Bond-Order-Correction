import os, sys
from rdkit import Chem
from rdkit.Chem import AllChem
smiles = sys.argv[1]
input_pose = sys.argv[2]
#smiles = "[B-](CC[C@H](CC[C@H]([C@]1(C(=O)O)N)CN(C)C)C1)([O+])(O)O"
#input_pose = "75523.pdb"
input_pose_name = input_pose.split('.pdb')[0]
template = Chem.MolFromSmiles(smiles)
lig_pose = AllChem.MolFromPDBFile(input_pose)
#Chem.SanitizeMol(lig_pose)
newMol = AllChem.AssignBondOrdersFromTemplate(template, lig_pose)
newMol_H = Chem.AddHs(newMol, addCoords=True)
#Chem.SanitizeMol(newMol_H)
pdbblock = Chem.MolToMolBlock(newMol_H)
open(input_pose_name+"_bond_order.mol",'w').write(Chem.MolToMolBlock(newMol_H))
pdbblock = Chem.MolToPDBBlock(newMol_H)
open(input_pose_name+"_bond_order.pdb",'w').write(Chem.MolToPDBBlock(newMol_H, flavor=4))
# with Chem.SDWriter(input_pose_name+'_bond_order.sdf') as w:
#     w.write(newMol_H)
os.system('obabel '+input_pose_name+'_bond_order.mol -omol2 -O '+input_pose_name+'_bond_order.mol2 -h')
