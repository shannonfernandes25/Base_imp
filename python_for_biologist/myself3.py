#python program to accept DNA sequence and give the output as complementary sequences
dna=input("Enter the sequence: ").upper()
complement=""
c=''
for i in dna:
    if i=="A":
        complement=i.replace("A","T")
        c+=complement
    elif i=="T":
        complement=i.replace("T","A")
        c+=complement
    elif i=="G":
        complement=i.replace("G","C")
        c+=complement
    elif i=="C":
        complement=i.replace("C","G")
        c+=complement
    else:
        pass
print("complementary sequence: ",c)

'''
output
Enter the sequence: tacg
complementary sequence:  ATGC
'''




#python program to accept protein sequence from the user and display the Nterminal 15 amino acids
pro=input("Enter the protein sequence: ").upper()
count=0
N_terminal=""
for amino_acid in pro:
    N_terminal+=amino_acid
    count+=1
    if count==15:
        break
print("N terminal 15 amino acids: ",N_terminal)

'''
output
Enter the protein sequence: vfgchfgvgfcdxsfxfhgvgv
N terminal 15 amino acids:  VFGCHFGVGFCDXSF
'''



#python program to accept DNA sequence as first string and accept the second string from the user. Check whether the second string is DNA or not 
string1=input("Enter the DNA sequence: ").upper()
string2=input("Enter the 2nd string: ").upper()
valid_dna_bases = {'A', 'T', 'C', 'G'}
for i in string2:
    if i not in valid_dna_bases:
        print("Not a DNA sequence")
        break # Stop checking as soon as an invalid base is found
    else:
        print("2nd string is a DNA sequence")

'''
output
Enter the DNA sequence: atgccgtaERROR!

Enter the 2nd string: hjyhgftjjyajkcj
Not a DNA sequence
'''