# a file named pro.fasta will be opened with read mode

#open() ---> open(filename, mode)

file = open("pro.fasta", "r")
for data in file:
    print(data)