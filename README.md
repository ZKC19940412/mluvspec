# mluvspec
Supplyment files of paper "UV-Visible Absorption Spectra of Solvated Molecules by Quantum Chemical Machine Learning" . 

This repository is structured as follow:
* machine-learning-python-files:
    * develop_ml_models.py: Develop 7-molecule (transfer-learing) model using cross-validation scheme
    * sample_output.log: Example output from running develop_ml_models.py with random-state being 0
    * transfer_learn_with_pre_train_models.py: Transfer-learing for the three target molecules with pre-trained models
    * utility.py: Helper functions for develop_ml_models.py and transfer_learn_with_pre_train_models.py
    
* Code and notebook:
  * BFGS_ase_reference.ipynb: Jupyter note book illusrating geometry optimzation with BFGS using [**ASE**](https://wiki.fysik.dtu.dk/ase/) package
  * utility.py: Python helper functions for read/write xyz files and compute energy and force with LJ potential
  * my_BFGS.py: Python main script to perform geometry optimization with BFGS method
  * my_GD.py: Python main script to perform geometry optimization with steepest decent method
  
* Reference:
   * [ASE Geometry Optimzation](https://wiki.fysik.dtu.dk/ase/ase/optimize.html)
