#rjust()   right side justification
#syntax=rjust(length,character)
seq=("ATGTCTCAGATC")
x=seq.rjust(20,'A')
print(x)

'''
 output
 AAAAAAAAATGTCTCAGATC           #total 20 letters
'''

seq=("ATGTCTCAGATC")
x=seq.rjust(20)
print(x)

'''
output
        ATGTCTCAGATC            #total 20    space added at start
'''

seq=("ATGTCTCAGATC")
x=seq.rjust(20,'*')
print(x)

'''
output
********ATGTCTCAGATC
'''

