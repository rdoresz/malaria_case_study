#!/usr/bin/python

'''
Title: blastprocess.py
Date: 02.03.2022
Author(s): Dorottya Ralbovszki

Description:
This script was written to identify and filter out scaffolds that contain bird genes.
The script first iterates through the uniprot dataset and saves the bird proteins into the linesdict dictionary (the keys are the characters after underscore).
Then, it iterates through the file from the blastp and saves the queries that contain bird protein hits into query_memory set.
Then, it iterates through the fna file (created by gffParse.pl) to identify the scaffold IDs that contained a bird blast hit and saves the IDs into scaffold_memory list.
Then, it iterates through the genome file (previously filtered Haemoproteus genome file) to save the header lines and their sequence lines into the genome_memory dictionary (keys are headers and items are sequenc lines).
Lastly, it iterates through the genome_memory dictionary and prints the keys (and their items) that are NOT in the scaffold_memory list to the output file keeping the original genome file structure.

Usage:
./blastprocess.py blast_file SwissProt_dat_file fna_file genome_file output_genome_file
'''


import sys

#setting up empty dictionary for saving bird protein IDs
linesdict = dict()
# setting up emty set to save the queries from the blast file that contain a bird protein hit
querymemory = set()
# setting up an emty list for saving the scaffold IDs that contain bird genes
scaffold_memory = []
# setting up empty dictionary to save the headers and their sequence lines from the genome file for further printing
genome_memory = dict()

# opening input and output files
with open(sys.argv[1], 'r') as blastp, open(sys.argv[2], "r") as uniprot, open(sys.argv[3], 'r') as fna, open(sys.argv[4], "r") as genome, open(sys.argv[5], "w") as fout:
    # iterating through the SwissProt_dat_file
    for lines in uniprot:
        # catching the IDs
        if lines.startswith('ID'):
            lines = lines.rstrip()
            IDlongD = lines.split('_')
            IDshorterD = IDlongD[1]
            # getting the characters after the underscore
            IDD = IDshorterD[0:5]
            # saving them as keys into the linesdict dictionary
            key = IDD
        # catching the lines with taxonomy information
        if lines.startswith('OC'):
            # catching lines that are bird
            if 'Aves' in lines:
                lines = lines.rstrip()
                # saving those lines into the dictionary with their ID as keys
                linesdict[key] = lines
    # iterating through the blastp file
    for line in blastp:
        # catching the query lines
        if line.startswith('Query='):
            line = line.rstrip()
            query = line.split('=')
            # getting the query id
            queryid = query[1].lstrip()
        # catching the lines that contain the ID used in linesdict as keys
        if line.startswith('>'):
            line = line.rstrip()
            IDlong = line.split('_')
            IDshorter = IDlong[1]
            # getting the IDs same format as the keys in linesdict
            ID = IDshorter[0:5]
            # iterating through linesdict
            for key, value in linesdict.items():
                # catching the IDs that are from bird
                if ID in linesdict:
                    # saving the queries that had a bird hit (set is used to have only one copy of the queries because each query has multiple hits)
                    querymemory.add(queryid)
    # iterating through the fna (fasta) file
    for line in fna:
        # cathcing the header lines
        if line.startswith('>'):
            column = line.split('\t')
            noID = column[0]
            # getting the same format as queryid in the querymemory set
            yesID = noID[1:]
            # checking for query IDs that are in the querymemory
            if yesID in queryid:
                # getting the scaffold ID of those queries
                scaffold_l = column[2]
                scaffold_s = scaffold_l.split('=')
                # keeping those scaffold IDs in scaffold_memory list
                scaffold_memory.append(scaffold_s[1])
    # iterating through the genome file
    for line in genome:
        # catching the header lines
        if line.startswith('>'):
            line = line.rstrip()
            # saving the line as key in genome_memory dictionary
            key = line
            # emptying the sequence memory list to save the following sequence lines belonging to this header
            seq = []
        # catching sequence lines
        else:
            line = line.rstrip()
            # adding them to seq list
            seq.append(line)
            # saving the list into the dictionary as the header's item
            genome_memory[key] = seq
    # iterating through the genome_memory dictionary
    for key in genome_memory:
            # getting the scaffold ID
            column = key.split(' ')
            lscaffold = column[0]
            scaffold = lscaffold[1:]
            # cathcing scaffolds that are not in scaffold_memory list
            if scaffold not in scaffold_memory:
                # getting the genome file format (multi line)
                sequence = '\n'.join(genome_memory[key])
                # printing the scaffolds that are kept into output genome file
                print('{}\n{}\n'.format(key, sequence), file = fout)
