#!/usr/bin/env python
# count_aip_kmers.py
# Import re to support regular expressions in this program
import re
# open Aip02 fastq file for reading
read_Aip02 = open('/home/adham/Documents/Scratch/dmel-2L-CDS-r5.9.fasta', 'r')
# Initialize a variable to contain the lines
line = ' '
# while line is not empty
kmer_length = 6
kmer_dictionary = {}
out = open("aip2_kmers.txt", 'w')
while line:
    # Read one line from the file using the readline() method
    line = read_Aip02.readline()
    # Read only sequence lines
    if re.match('^[ATGC]+$', line):
        for start in range(0, len(line) - kmer_length):
            kmer = line[start:start+kmer_length]
            if kmer in kmer_dictionary:
                  kmer_dictionary[kmer]+=1
            else:
                  kmer_dictionary[kmer]=1
t = "\t"
for kmer in kmer_dictionary:
    count = kmer_dictionary[kmer]
    output = [kmer, str(count)]
    out.write((t.join(output)))
# Close the file using the close() method
read_Aip02.close()
