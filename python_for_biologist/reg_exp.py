

import re                                            #regular expression
pattern=(r'ATGCCGATGATGC')
sequence=('ATGCCGATGATGCATGCCGATGCGTA')
a=re.match(pattern,sequence)                         #re.match() is a function in re    
print(a)

'''
output
<re.Match object; span=(0, 13), match='ATGCCGATGATGC'>
'''


import re 
pattern=(r'ATGCCGATGAT')
sequence=('ATGCCGATGATGCATGCCGATGCGTA')
if re.match(pattern,sequence):
    print("match")
else:
    print("no match")
    
'''
output
match
'''


import re 
pattern=(r'CGACTGCGAATG')
sequence=('ATGCCGATGATGCATGCCGATGCGTA')
if re.match(pattern,sequence):
    print("match")
else:
    print("no match")

'''
output
no match
'''