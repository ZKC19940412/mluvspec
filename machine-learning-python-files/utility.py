import numpy as np
import os
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LassoLars
from sklearn.metrics import make_scorer, mean_absolute_error
import subprocess

# --------------------------------------------------------------------------------- #
def cross_validation_scheme(X, Y, estimator=None, objective_function=None, n_cv=10):
    """cross_validation_scheme is used to perform model fitting using k-fold
       cross validation

        Input:
            X: (ndarray) feature matrix
            Y: (ndarray) property vectors
            estimator (sklearn estimator object) estimator
            objective_function (sklearn object) objective function
            n_cv (int) number of cross-validation (cv) folds

    """

    # Generate default estimator and objective function if none of them are provided
    if estimator is None:
        estimator = LassoLars(alpha=1.2e-6, max_iter=10000, normalize=True, fit_intercept=True)
    if objective_function is None:
        
	# Config scoring function
        mean_signed_error_score = make_scorer(mean_signed_error)
        mean_absolute_error_score = make_scorer(mean_absolute_error)

    # Initialize cross validation scheme (cvs)
    print('Performing %d-fold cross validation ....\n' % int(n_cv))
    cvs = cross_validate(estimator, X, Y, cv=n_cv,
                         scoring={'mean_absolute_error': mean_absolute_error_score,
                                  'mean_signed_error': mean_signed_error_score},
                         return_estimator=True,
                         return_train_score=True)

    return cvs


# --------------------------------------------------------------------------------- #

def transfer_learning_scheme(cvs,
                             descriptor,
                             ground_truth,
                             molecule_string):
    """transfer_learning_scheme is used to transfer-learning based on cross-validation scheme (cvs)

            Input:
                cvs: (dictionary) cross validation scheme
                descriptor (ndarray) descriptor/feature matrix
                ground_truth (ndarray) vector that contains ground-truth of target values
                objective_function (sklearn object) objective function
                molecule_string (str) molecule string


    """
    # Declare empty list to intake data
    transfer_learned_molecule_MAE_list = []
    transfer_learned_molecule_prediction_list = []
    transfer_learned_molecule_MSE_list = []

    # Derive number of cv fold from cvs object
    n_cv = int(len(cvs['estimator']))
	
    # Make predictions at each sub-model and then take averages of mae and predictions
    # 1000 is the conversion factor from eV to meV
    for i in range(n_cv):
        energy_transfer_learned_molecule_prediction = cvs['estimator'][i].predict(descriptor)
        transfer_learned_molecule_prediction_list.append(energy_transfer_learned_molecule_prediction)
        MAE_transfer_learned_molecule = mean_absolute_error(ground_truth, energy_transfer_learned_molecule_prediction)
        transfer_learned_molecule_MAE_list.append(MAE_transfer_learned_molecule)
        transfer_learned_molecule_MSE_list.append(np.mean(energy_transfer_learned_molecule_prediction - ground_truth))

    print('Transfer learning molecule: ', molecule_string)
    print('MAE cross test (meV): %.2f ' % (1000 * np.array(transfer_learned_molecule_MAE_list).mean()))
    print('MSE cross test (meV): %.2f' % (1000 * np.array(transfer_learned_molecule_MSE_list).mean()))


# --------------------------------------------------------------------------------- #
def transfer_learning_from_pre_train_models(estimator_para_file_path,
                                            descriptor,
                                            ground_truth,
                                            molecule_string):
    """transfer_learning_from_pre_train_models is used to perform transfer-learning from pretrain models

            Input:
                estimator_para_file_path: (str) estimator parameter files
                descriptor (ndarray) descriptor/feature matrix
                ground_truth (ndarray) vector that contains ground-truth of target values
                objective_function (sklearn object) objective function
                molecule_string (str) molecule string


    """
    # Construct estimators
    estimators = make_estimators(estimator_para_file_path)

    # Initialize cvs with only estimators field from pre-train models (estimators)
    cvs = {'estimator': list()}
    for i in range(len(estimators)):
        cvs['estimator'].append(estimators[i])

    transfer_learning_scheme(cvs,
                             descriptor,
                             ground_truth,
                             molecule_string)


# --------------------------------------------------------------------------------- #
def make_estimators(estimator_para_file_path, estimator_base_structure=None):
    """make_estimators is used to make estimators based on estimator parameter files

                Input:
                    estimator_para_file_path: (str) estimator parameter files
                    estimator_base_structure: (sklearn object) base structure of estimator
                    estimator (sklearn-estimator object) estimator

                Output:
                    estimators: (list) list of estimators

    """
    # Load in estimator parameter files
    estimator_para_files = sorted(os.listdir(estimator_para_file_path))

    # Initialize empty lists to intake data
    estimators = []
    estimator_base_structures = []
 
    # Initialize base structure for the estimators
    if estimator_base_structure is None:
        
	# If no base structure is provided, generate a list of base structures with the same lasso model configurations
        for j in range(len(estimator_para_files)):
            estimator_base_structures.append(LassoLars(alpha=1.2e-6, max_iter=10000, normalize=True, fit_intercept=True))

    for i in range(len(estimator_para_files)):
        estimator_parameters = np.loadtxt(estimator_para_file_path + '/' + estimator_para_files[i])
        intercept = estimator_parameters[0]
        coefficients = estimator_parameters[1:]
        estimator = estimator_base_structures[i]
        estimator.coef_ = coefficients
        estimator.intercept_ = intercept
        estimators.append(estimator)

    return estimators


# --------------------------------------------------------------------------------- #
def mean_signed_error(y_true, y_pred):
    """mean_signed_error is used to compute mean signed error (MSE)

           Input:
               y_true: (ndarray) ground-truth vector
               y_pred: (ndarray) prediction vector


    """
    # Closer to 0 is better
    # < 0 is under-predicted
    # > 0 is over-predicted
    return np.mean(y_pred - y_true)

# --------------------------------------------------------------------------------- #
def extract_dataset(data_path, is_extract_pre_train_model=False):
    """extract_dataset is used to extract data set of descriptors, target energies and pretrain models

        Input:
            data_path: (str) name of the output file
	    is_extract_pre_train_model (boolean): Instruction on whether to extract pretrain model tar gz files
    """

    # Declare descriptor and target energy paths accordingly
    descriptor_path = data_path + '/' + 'descriptors.tar.gz'
    target_energy_path = data_path + '/' + 'target_energies.tar.gz'

    # Extract descriptors and target energies
    print('Descriptor and target energy data extracting ...\n')
    subprocess.call('tar xzvf ' + descriptor_path, shell=True)
    subprocess.call('tar xzvf ' + target_energy_path, shell=True)

    # Extract pre-train models	
    if is_extract_pre_train_model:
        print('Pretrain model extracting ...\n')
        pre_train_model_path = data_path + '/' + 'pre_train_models.tar.gz'
        subprocess.call('tar xzvf ' + pre_train_model_path, shell=True)
