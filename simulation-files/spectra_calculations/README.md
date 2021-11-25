# `spectra_calculations`

spectra_calculations illustrates how to perform excited state calculations using  [ORCA](https://orcaforum.kofo.mpg.de/app.php/portal) 4.2.1.

- input folder contains ORCA input files for each of the 10 aromatic molecules to perform excited state calculations at the level of STEOM-DLPNO-CCSD/def2-TZVP.
-   output folder contains the corresponding output files for  each of the 10 aromatic molecules shown in the input folder.

- To perform excited state calculations using ORCA 4.2.1, execute the following line in terminal:
```bash
/path/to/orca molecule.inp > molecule.out
```

where /path/to/orca is the directory for your orca program, and molecule.inp refers to one of the orca input files for 10 the aromatic molecules. 