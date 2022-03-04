#!/usr/bin/python3
'''
Title: GC_content.py
Date: 28.02.2022
Author(s): Dorottya Ralbovszki

Description:
Filters out scaffolds that are shorter than 3000 nucleotides.
'''

import sys
# setting up empty dictionary for saving scaffolds
scaffolds = dict()
# opening input and output files
with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fout:
    # iterating through the input genome file
    for line in fin:
        # catching the header lines
        if line.startswith('>'):
            line=line.rstrip()
            # saving them as key in dictionary
            key = line
            # emptying/setting up empty list for saving following sequence lines
            seq = []
        # catching sequence lines
        else:
            line = line.rstrip()
            # adding lines to seq list
            seq.append(line)
            # saving the sequence lines as the item of the key (which is the header)
            scaffolds[key] = seq
    # iterating through the dictionary
    for key in scaffolds:
        # getting the length of each scaffold
        column = key.split("=")
        # filtering according to length
        if int(column[1]) >= 3000:
            # keep input format of sequence if it passes filter
            sequence = '\n'.join(scaffolds[key])
            # printing the headers and their sequence into output genome file
            print('{}\n{}\n'.format(key, sequence), file = fout)
