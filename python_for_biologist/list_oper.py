#write a script to input 5 DNA sequenecs. Join the sequence with ";". Convert the joined string to an list and perform the following operations: split, reverse, insert, pop, sort
DNA=[]
for i in range(0,5):
    seq=input("Enter the DNA sequence: ").upper()
    DNA.append(seq)
print(DNA)

new=";".join(DNA)
print("Joined DNA sequence: ",new)

sp=new.split(";")
print("splitted sequence: ",sp)

sp.reverse()
print("reversed sequence: ",sp)

sp.insert(2,"**")
print("inserted sequence: ",sp)

sp.pop()
print("popped sequence: ",sp)

sp.sort()
print("sorted sequence: ",sp)

'''
output
Enter the DNA sequence: agtcgtactg
Enter the DNA sequence: gctagctgag
Enter the DNA sequence: tgcagtcagt
Enter the DNA sequence: agtcgatctc
Enter the DNA sequence: gtcgatgcta
['AGTCGTACTG', 'GCTAGCTGAG', 'TGCAGTCAGT', 'AGTCGATCTC', 'GTCGATGCTA']
Joined DNA sequence:  AGTCGTACTG;GCTAGCTGAG;TGCAGTCAGT;AGTCGATCTC;GTCGATGCTA
splitted sequence:  ['AGTCGTACTG', 'GCTAGCTGAG', 'TGCAGTCAGT', 'AGTCGATCTC', 'GTCGATGCTA']
reversed sequence:  ['GTCGATGCTA', 'AGTCGATCTC', 'TGCAGTCAGT', 'GCTAGCTGAG', 'AGTCGTACTG']
inserted sequence:  ['GTCGATGCTA', 'AGTCGATCTC', '**', 'TGCAGTCAGT', 'GCTAGCTGAG', 'AGTCGTACTG']
popped sequence:  ['GTCGATGCTA', 'AGTCGATCTC', '**', 'TGCAGTCAGT', 'GCTAGCTGAG']
sorted sequence:  ['**', 'AGTCGATCTC', 'GCTAGCTGAG', 'GTCGATGCTA', 'TGCAGTCAGT']
'''




