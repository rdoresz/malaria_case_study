#!/usr/bin/python3
'''
Title: GC_content.py
Date: 28.02.2022
Author(s): Dorottya Ralbovszki

Description:
Filters out scaffolds with GC content above 30%.
'''

import sys
# setting up empty string for saving headers
Idline = ''
# setting up empty string for saving sequence lines
nucleotides_line = ''
# setting up emty string for gc content calculation
gc = ''
# opening input and output files
with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fout:
    # iterating through input genome file
    for line in fin:
        line=line.rstrip()
        # catching the header lines
        if line.startswith('>'):
            # if sequence lines were previously saved
            if nucleotides_line:
                # calculate gc content
                gc=((nucleotides_line.count('c')+nucleotides_line.count('g'))/len(nucleotides_line))*100
                gcround=round(gc)
                # filter according to gc content
                if int(gcround) <= 30:
                    # keep input format of sequence if it passes filter
                    sequence = '\n'.join(seq)
                    # print its header and the sequence in same format as in input to output genome file
                    print('{}\n{}\n'.format(Idline, sequence), file = foutppr)
            # save next header line
            Idline=line
            # empty gc string
            gc = ''
            # empty the sequence memory
            nucleotides_line = ''
            # empty list for saving sequence lines
            seq = []
        # cathcing sequence lines
        else:
            # saving line in seq list
            seq.append(line)
            # joining the multi lines into single line
            nucleotides_line += line.lower()
