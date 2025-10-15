#python script to create userdefined function to translate DNA to RNA sequence
def rna_seq(dna):
    rna=dna.replace("T","U")
    return(rna)
print(rna_seq("ATGCCGATCAGTTAGTAC"))

'''
output
AUGCCGAUCAGUUAGUAC
'''

print(rna_seq("TGCAGTGTACTTACGGCATTCAGTCATG"))

'''
output
UGCAGUGUACUUACGGCAUUCAGUCAUG
'''