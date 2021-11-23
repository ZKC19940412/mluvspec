# mluvspec
Code & data files of paper "UV-Visible Absorption Spectra of Solvated Molecules by Quantum Chemical Machine Learning" . 

This repository is structured as follow:
* machine-learning-python-files:
    * develop_ml_models.py: Develop 7-molecule (transfer-learing) models using cross-validation scheme
    * sample_output.log: Example output from running develop_ml_models.py with random-state being 0
    * transfer_learn_with_pre_train_models.py: Transfer-learing for the target molecules with pre-trained models
    * utility.py: Helper functions for develop_ml_models.py and transfer_learn_with_pre_train_models.py
    
* simulation-files:
  * bc_calculations: Molecular geometries and [fitsnap](https://github.com/FitSNAP/FitSNAP) input files used to calculate bispectrum components (BC)
  * fpmd: Input files used to perform fpmd, using [cp2k](https://www.cp2k.org/)
  * spectra_calculations: Input files for spectra calculations at the level of DLPNO-STEOM-CCSD/def2-TZVP, using [ORCA](https://orcaforum.kofo.mpg.de/app.php/portal) 4.2.1
  
* training-set-and-pre-train-model:
   * descriptors.tar.gz: BC descriptors computed for the 7-molecule (transfer-learing) model
   * pre_train_models.tar.gz: Pre-trained 7-molecule (transfer-learing) models
   * target_energies.tar.gz: Lowest excited-state energies calculated with ORCA
