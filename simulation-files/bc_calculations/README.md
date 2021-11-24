# `bc_calculations`

bc_calculations illustrates how to perform bispectrum components (BC)
using [fitsnap](https://github.com/FitSNAP/FitSNAP).

External files required: 
			1). aromatic.in
			2). steom_dlpno_ccsd_extxyz

- Warning: "energy = 1.0" shown in each extended xyz file only serves as the place holder for the energy value. We only use fitsnap to compute the descriptors. 

- To set the FitSNAP package into the python path,  set the environment variable as follow:
```bash
export PYTHONPATH="/path/to/FitSNAP"				
```  

- To compute BC descriptors with Fitnsap, execute the following line in terminal:
```python
mpirun -n 8 python -m fitsnap3 aromatic.in --nofit 
```