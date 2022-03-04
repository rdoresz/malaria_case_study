#!/usr/bin/python
'''
Title: q_3_gc.py
Date: 04.03.2022
Author(s): Dorottya Ralbovszki

Description:
This script was written to answer question 3/gc % by converting the multi line fasta into single line and then calculating the gc %.
The gc % in the genome file will be printed on the standard output.

bash run: for f in ../fasta_all/*.fna; do
> python q_3_genes.py "$f"
> echo "$f"
> done > q_3_genes.txt


'''


import sys

nucleotide_line = ''
gc = ''

with open(sys.argv[1], 'r') as fin:
    for line in fin:
        line = line.rstrip()
        if line.startswith('>'):
            continue
        else:
            nucleotide_line += line.lower()
    gc = ((nucleotide_line.count('c')+nucleotide_line.count('g'))/len(nucleotide_line))*100
    print(gc)
