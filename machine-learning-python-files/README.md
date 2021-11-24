# `machine-learning-python-files`

machine-learning-python-files illustrates how to develop machine-learing models and perform transfer-learing using bispectrum components (BC) descriptors + LASSO algorithm. 

External files required: 
		       1). training-set-and-pre-train-model/descriptors.tar.gz \\
		       2). training-set-and-pre-train-model/target_energies.tar.gz \\
		       3). training-set-and-pre-train-model/pre_train_models.tar.gz


- develop_ml_models.py proceeds as follows:
	
    1. Load in precomputed BC descriptors and (target) excited state energies for all 10 aromatic molecules.

    2. Develop 7-molecule model using cross-vadliation scheme.
     
    3. Perform transfer-learing for 3 target molecules using the 7-molecule model developed at step 2. 
			      
-  transfer_learn_with_pre_train_models.py proceeds as follows:

    1. Load in precomputed BC descriptors and (target) excited state energies for 3 target molecules  and the pre-train-models.

    2. Perform transfer-learing for 3 target molecules using the 7-molecule model models. 
