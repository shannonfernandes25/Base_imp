
#startswith(value, start, end) - Checks if the string starts with the specified value within the given start and end positions.  
seq = ">NUC1234"
x = seq.startswith(">")
print(x)

'''
output
True
'''

seq = ">NUC1234"
x = seq.startswith("12",4)
print(x)

'''
output
True
'''

seq = ">NUC1234"
x = seq.startswith("34",4)
print(x)

'''
output
False
'''

#endswith(value, start, end) - Checks if the string ends with the specified value within the given start and end positions.
seq = "AUGGAGACGCAGCAUUAG"
x = seq.endswith("UAG")
print(x)

'''
output
True
'''

file = open('pro.fasta','r')
for i in file:
    if i.startswith(">"):
        print("yes")
    else:
        print("no")
        
'''
output
yes
no
no
no
no
no
no
no
no
yes
no
no
no
no
no
yes
no
no
no
no
no
no
no
no
no
yes
no
no
no
no
no
no
no
no
no
yes
no
no
no
no
no
no
no
no
no
'''

file = open('pro.fasta','r').readlines()
x = file.startswith(">")
print(x)

'''
output
x = file.startswith(">")
        ^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'startswith'
'''

#program to read the fasta file and to count the number of sequences
data = open('pro.fasta','r').readlines()
count=0
for line in data:
    if line.startswith(">"):
        count = count + 1
print("The number of sequences: ",count)

'''
output
The number of sequences:  5
'''
