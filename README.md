# mluvspec
Supplyment files of paper "UV-Visible Absorption Spectra of Solvated Molecules by Quantum Chemical Machine Learning" . 

This repository is structured as follow:
* Data:
    * Argon_30K.xyz: Argon cluster xyz file, generated at 30K
    
* Code and notebook:
  * BFGS_ase_reference.ipynb: Jupyter note book illusrating geometry optimzation with BFGS using [**ASE**](https://wiki.fysik.dtu.dk/ase/) package
  * utility.py: Python helper functions for read/write xyz files and compute energy and force with LJ potential
  * my_BFGS.py: Python main script to perform geometry optimization with BFGS method
  * my_GD.py: Python main script to perform geometry optimization with steepest decent method
  
* Reference:
   * [ASE Geometry Optimzation](https://wiki.fysik.dtu.dk/ase/ase/optimize.html)
