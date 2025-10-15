#program to remove all the spaces from the entered string
val=input("Enter the sentence: ").upper()         #converts output to capitals
var_str=val.replace(" ","")                        #replace is a function which replaces words with another word,    here space is replaced with no space
print("New sentence: ",var_str)

'''
output
Enter the sentence: agtc cgta
New sentence:  AGTCCGTA
'''


#program to convert DNA to RNA
dna=input("Enter the DNA sequence: ").upper()
rna=dna.replace("T","U")
print("RNA sequence: ",rna)

'''
output
Enter the DNA sequence: atgccgtaERROR!

RNA sequence:  AUGCCGUA
'''