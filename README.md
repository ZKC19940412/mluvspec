# mluvspec
Supplyment files of paper "UV-Visible Absorption Spectra of Solvated Molecules by Quantum Chemical Machine Learning" . 

This repository is structured as follow:
* machine-learning-python-files:
    * develop_ml_models.py: Develop 7-molecule (transfer-learing) model using cross-validation scheme
    * sample_output.log: Example output from running develop_ml_models.py with random-state being 0
    * transfer_learn_with_pre_train_models.py: Transfer-learing for the three target molecules with pre-trained models
    * utility.py: Helper functions for develop_ml_models.py and transfer_learn_with_pre_train_models.py
    
* simulation-files:
  * bispectrum_component_calculations: Molecular geometries and fitsnap[https://github.com/FitSNAP/FitSNAP] input file used to calculate bispectrum component (BC) descriptors
  * fpmd: Sample input files used to perform fpmd
  * spectra_calculations: Sample input files for spectra calculations at the level of DLPNO-STEOM-CCSD/def2-TZVP, using ORCA[https://orcaforum.kofo.mpg.de/app.php/portal] 4.2.1
  
* Reference:
   * [ASE Geometry Optimzation](https://wiki.fysik.dtu.dk/ase/ase/optimize.html)
