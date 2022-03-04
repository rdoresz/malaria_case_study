#!/usr/bin/python
'''
Title: q_3_gc.py
Date: 04.03.2022
Author(s): Dorottya Ralbovszki

Description:
This script was written to answer question 3/gc % by converting the multi line fasta into single line and then calculating the gc %.
The gc % in the genome file will be printed on the standard output.


'''


import sys
# setting up empty string for saving sequence lines
nucleotide_line = ''
# setting up empty string to calculate gc content
gc = ''
# opening input file
with open(sys.argv[1], 'r') as fin:
    # iterating through the file
    for line in fin:
        line = line.rstrip()
        # passing the header lines
        if line.startswith('>'):
            continue
        # saving the sequence lines    
        else:
            # converting from multi line to single line
            nucleotide_line += line.lower()
    # calculating gc content        
    gc = ((nucleotide_line.count('c')+nucleotide_line.count('g'))/len(nucleotide_line))*100
    # printing to standard output
    print(gc)
