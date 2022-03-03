#!/usr/bin/python
'''
Title: q_3_genome.py
Date: 03.03.2022
Author(s): Dorottya Ralbovszki

Description:
This script was written to answer question 3/genome size by adding up the nucleotides from the scaffolds from the genome files.
The number of nucleotides in the genome file will be printed on the standard output.

'''


import sys
#setting up empty list for sequnce line memory
seq = []
#setting up a variable for calculating genome size
sum_of_length = 0
#opening the input genome file
with open(sys.argv[1], 'r') as fin:
    for line in fin:
        #this part is used when the header in the genome file contains the lenght of the scaffold
    #     if line.startswith('>'):
    #         line = line.rstrip()
    #         long = line.split('=')
    #         sum_of_length += int(long[1])
    # print(sum_of_length)

    #otherwise this part is used
        #passing the header lines
        if line.startswith('>'):
            continue
        # catching the sequence lines
        else:
            #getting rid of \n characters
            line = line.rstrip()'
            #saving the lines into the sequnce memory list
            seq.append(line)
    # transforming the sequence memory list into a string
    sequence = ''.join(seq)
    # getting the number of nucleotides in the string
    print(len(sequence))
