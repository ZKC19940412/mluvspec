# `bc_calculations`

bc_calculations illustrate how to compute bispectrum components (BC)
using [FitSNAP](https://github.com/FitSNAP/FitSNAP).

External files required: 
			1). aromatic.in
			2). steom_dlpno_ccsd_extxyz

- Note: "energy = 1.0" shown in xyz files only serves as the place holder for the energies. We only use FitSNAP to compute the descriptors. 

- To set the FitSNAP package into the python path,  set the environment variable as follow:
```bash
export PYTHONPATH="/path/to/FitSNAP"				
```  

- To compute BC descriptors with FitSNAP, execute the following line in terminal:
```python
mpirun -n 8 python -m fitsnap3 aromatic.in --nofit 
```
