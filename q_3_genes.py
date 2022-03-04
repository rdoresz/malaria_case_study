#!/usr/bin/python
'''
Title: q_3_genome.py
Date: 03.03.2022
Author(s): Dorottya Ralbovszki

Description:
This script was written to answer question 3/number of genes by counting the gene IDs in the fna and this number will be printed on the standard output.

bash run: for f in ../fasta_all/*.fna; do
> python q_3_genes.py "$f"
> echo "$f"
> done > q_3_genes.txt


'''


import sys
genesum = 0
with open(sys.argv[1], 'r') as fin:
    for line in fin:
        if line.startswith('>'):
            genesum += 1
    print(genesum)
