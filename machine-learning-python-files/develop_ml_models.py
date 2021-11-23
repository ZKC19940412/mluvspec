import numpy as np
from sklearn.utils import shuffle
from utility import cross_validation_scheme
from utility import transfer_learning_scheme
from utility import extract_dataset
import os
import shutil

# Clean up pre-exist files
if os.path.exists('descriptors'):
	shutil.rmtree('descriptors')

if os.path.exists('target_energies'):
	shutil.rmtree('target_energies')

# Declate data path
data_path = '../training-set-and-pre-train-model'

# Extract dataset
extract_dataset(data_path)

# Load in descriptor and target energies for training and transfer-learing sets
descriptor_aromatic = np.loadtxt('descriptors/descriptor_aromatic.dat')
descriptor_aminophenol = np.loadtxt('descriptors/descriptor_aminophenol.dat')
descriptor_guaiacol = np.loadtxt('descriptors/descriptor_guaiacol.dat')
descriptor_pDMB = np.loadtxt('descriptors/descriptor_pDMB.dat')
energy_aromatic = np.loadtxt('target_energies/energy_aromatic.dat')
energy_aminophenol = np.loadtxt('target_energies/energy_aminophenol.dat')
energy_guaiacol = np.loadtxt('target_energies/energy_guaiacol.dat')
energy_pDMB = np.loadtxt('target_energies/energy_pDMB.dat')

# Generalize variable names to X_train and Y_train
X_train = descriptor_aromatic
Y_train = energy_aromatic

# Define random state value for shuffle
random_state_val = None
X_train, Y_train = shuffle(X_train.copy(), Y_train.copy(), random_state=random_state_val)

# Print major stats
print('\n')
print('Train Data Size: ', X_train.shape)
print('Max feature value: %.3f' % X_train.max())
print('Mean feature value: %.3f' % X_train.mean())
print('Min feature value: %.3f' % X_train.min())
print('Std feature value: %.3f' % X_train.std())
print('\n')

# Define number of cross-validation (cv) fold
number_of_cross_validation_fold = 10

# Perform model fitting with cross validation
cvs = cross_validation_scheme(X_train, Y_train, n_cv=number_of_cross_validation_fold)
np.save('cvs.npy', cvs)

# Compute major statics
MAE_cv_test = cvs['test_mean_absolute_error'].mean()
MSE_cv_test = cvs['test_mean_signed_error'].mean()

# Print major statics
# 1000 is the conversion factor from eV to meV
if random_state_val is not None:
	print('Random State: %d' % random_state_val)
print('MAE test(meV): %.2f ' % (1000 * MAE_cv_test))
print('MSE test(meV): %.2f ' % (1000 * MSE_cv_test))
print('\n')

# Perfroming transfer learing for three molecules
transfer_learning_scheme(cvs,
                         descriptor_guaiacol,
                         energy_guaiacol,
                         molecule_string = '1,2-methoxyphenol')
print('\n')
transfer_learning_scheme(cvs,
                         descriptor_aminophenol,
                         energy_aminophenol,
                         molecule_string = '1,4-aminophenol')

print('\n')
transfer_learning_scheme(cvs,
                         descriptor_pDMB,
                         energy_pDMB,
                         molecule_string = '1,4-dimethoxybenzene')
