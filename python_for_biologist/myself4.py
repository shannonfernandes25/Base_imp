#program to input DNA sequence: a. add spaces to the right of the sequence
#                               b. convert DNA to RNA 
#                               c. split the sequence wrt U
dna=input("Enter the DNA sequence: ").upper()
right=dna.rjust(20)
print("justified sequence: ",right)
rna=right.replace("T","U")
print("RNA sequence: ",rna)
sp=rna.split("U")
print("split sequence: ",sp)

'''
output
Enter the DNA sequence: atgtcgattgcatat
justified sequence:       ATGTCGATTGCATAT
RNA sequence:       AUGUCGAUUGCAUAU
split sequence:  ['     A', 'G', 'CGA', '', 'GCA', 'A', '']
'''

#python script to input a pre mrna and perform post-translational modifications- ply A tail and 5' capping
mrna=input("Enter the sequence: ").upper()
new_mrna="MET"+mrna+"AAAAAAAA"
print(new_mrna)

'''
output
Enter the sequence: auucgacgucagu
METAUUCGACGUCAGUAAAAAAAA
'''

#write a code to get the count of ATGCs in your sequence.Check is the sequence is a gene or not
dna=input("Enter the sequence: ").upper()
a=dna.count("A")
t=dna.count("T")
g=dna.count("G")
c=dna.count("C")
print("count of A: ",a,"\ncount of T: ",t,"\ncount of G: ",g,"\ncount of C: ",c)
at=a+t
gc=g+c
if (at>gc):
    print("its not a gene")
else:
    print("it is a gene")

'''
output
Enter the sequence: attcgtactgcagcaggct
count of A:  4 
count of T:  5 
count of G:  5 
count of C:  5
it is a gene
'''

#write a program to act as DNA ligase
dna_seq1=input("Enter the 1st DNA sequence: ").upper()
dna_seq2=input("Enter the 2nd DNA sequence: ").upper()
ligated_dna=dna_seq1+dna_seq2
print("DNA sequence before ligation: ",ligated_dna)

'''
output
Enter the 1st DNA sequence: atgc
Enter the 2nd DNA sequence: gtca
DNA sequence before ligation:  ATGCGTCA
'''



#write a code to find if a start and stop codon UAG is present in a DNA sequence    (refer clrs.py)
DNA_seq=['CGTAGTCA','GATGCGCTCG','TGATGTGUAG','CGAGCUAGC','AGTCUGUAGATGC']
stop_codon='UAG'
count=0
for i in DNA_seq:
    if stop_codon in i:
        count=1
if count==1:
    print("stop codon is present")
else:
    print('not present')

'''
output
stop codon is present
'''



#Program to convert a DNA into its reverse. Count the number of times ATG is repeated in the sequence. Find the first position of ATG in the sequence in 3' and 5' direction
dna = input("Enter the sequence: ").upper()

reverse_dna = dna[::-1]                                                                # Reverse DNA
print("The reverse DNA is:", reverse_dna)

repeated_1 = dna.count("ATG")                                                          # Count occurrences of ATG
print("The number of times ATG is repeated in dna:", repeated_1)

repeated_2 = reverse_dna.count("ATG")
print("The number of times ATG is repeated in reverse dna:", repeated_2)

if repeated_1 >= 1:                                                                     # Position of ATG in 5' -> 3' direction
    pos_5 = dna.index("ATG") + 1   # +1 for biological indexing
    print("The position of ATG in 5' direction is:", pos_5)
else:
    print("ATG is not found in dna")

if repeated_2 >= 1:                                                                      # Position of ATG in 3' -> 5' direction
    pos_3 = reverse_dna.index("ATG") + 1
    print("The position of ATG in 3' direction is:", pos_3)
else:
    print("ATG is not found in reverse dna")


'''
Enter the sequence: AATGCATGCCGACCGTACG
The reverse DNA is:  GCATGCCAGCCGTACGTAA
The number of times ATG is repeated in dna:  2
the position of ATG in 5' direction is:  1
the position of ATG in 3' direction is:  2

Enter the sequence: GCGTACGCGG
The reverse DNA is: GGCGCATGCG
The number of times ATG is repeated in dna: 0
The number of times ATG is repeated in reverse dna: 1
ATG is not found in dna
The position of ATG in 3' direction is: 6
'''
