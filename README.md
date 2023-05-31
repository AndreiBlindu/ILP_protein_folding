# Interger Linear Programming for Protein Folding
In this notebook, we show different integer linear programming (ILP) models for solving semplified versions of the protein folding problem.  
Predicting the three-dimensional structure of a protein, given its amino acid sequence, is a critical task in biochemistry and computational biology since it can help to better understand some diseases and the development of new drugs.
Since the search space is huge brute force is not an option and atomic-level modeling is computationally prohibitive, so many simplified models and approaches have been developed during the years. One of particular interest is the HP model.

## HP model
The HP model relies on three semplifications:
1. divide the 20 amino acids in two 2 groups:
    - Hydrophobic (non-polar) indicated with H
    - Hydrophilic (polar) indicated with P
Hence, our protein sequence becomes a binary string
2. Proteins in a cell are surrounded by water so the H amino acids are likely to be forced in the interior of the folded protein, while the P stay on the exterior.
3. Stability of the folding is maximized by the number of bonds between hydrophobic amino acids (H-H bonds)

In the first section of this notebook we aim to predict the 2-D structure of a protein by considering it as a binary string (according to the HP model) embed on a two-dimensional grid. The code and results shown take inspiration from the paper [Protein folding on lattices : An integer programming approach](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2154543).  


Whereas in the second section we try to predict the 3-D structure of a protein embed on three-dimensional cubic lattice by using the ILP model described in the paper [An integer programming model for protein structure prediction using the 3D-HP side chain model](https://www.sciencedirect.com/science/article/pii/S0166218X15003078). 