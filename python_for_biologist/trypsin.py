#program to show the tryptic cleavage in the given protein sequence
pro=['A','T','G','K','P','A','R','Q','A']
for i in range(0,len(pro)):
    if i=='K' or i=='R':
        if (i+1)!='P':
            pro.insert(i+1," ")
str1=""
tryp=str1.join(pro)
print("Protein sequence after trypsin digestion: ",tryp)

'''
output
Protein sequence after trypsin digestion:  ATGKPARQA
'''

