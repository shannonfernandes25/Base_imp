#read() mode

file=open("pro.fasta","r")
print(file.read())

'''
output

reads the file without spaces
'''

file=open("pro.fasta","r")
print(file.read(500))

'''
output

shows only 500 characters
'''