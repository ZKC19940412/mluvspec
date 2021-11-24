import numpy as np
import os
import shutil
from utility import extract_dataset
from utility import make_estimators
from utility import transfer_learning_from_pre_train_models

# Clean up pre-exist files
if os.path.exists('descriptors'):
  shutil.rmtree('descriptors')

if os.path.exists('target_energies'):
  shutil.rmtree('target_energies')

if os.path.exists('pre_train_models'):
  shutil.rmtree('pre_train_models')


# Declate data path
data_path = '../training-set-and-pre-train-model'

# Extract dataset
extract_dataset(data_path, is_extract_pre_train_model=True)

# Load in descriptor and target energies for training and transfer-learing sets
descriptor_aminophenol = np.loadtxt('descriptors/descriptor_aminophenol.dat')
descriptor_guaiacol = np.loadtxt('descriptors/descriptor_guaiacol.dat')
descriptor_pDMB = np.loadtxt('descriptors/descriptor_pDMB.dat')
energy_aminophenol = np.loadtxt('target_energies/energy_aminophenol.dat')
energy_guaiacol = np.loadtxt('target_energies/energy_guaiacol.dat')
energy_pDMB = np.loadtxt('target_energies/energy_pDMB.dat')

# Perfroming transfer learing for three molecules
print('\n')
transfer_learning_from_pre_train_models('pre_train_models/',
                         descriptor_guaiacol,
                         energy_guaiacol,
                         molecule_string = '1,2-methoxyphenol')
print('\n')
transfer_learning_from_pre_train_models('pre_train_models/',
                         descriptor_aminophenol,
                         energy_aminophenol,
                         molecule_string = '1,4-aminophenol')

print('\n')
transfer_learning_from_pre_train_models('pre_train_models/',
                         descriptor_pDMB,
                         energy_pDMB,
                         molecule_string = '1,4-dimethoxybenzene')
