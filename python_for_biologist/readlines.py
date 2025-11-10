#readlines - converts to a list and read all lines,        can be used for small files

file = open('pro.fasta',"r")
print(file.readlines())

file = open('pro.fasta').readlines()
print(file)

#readline() - reads only the first line

file = open('pro.fasta',"r")
print(file.readline())

file = open('pro.fasta').readline()
print(file)


#The .strip() method in Python is a string method that removes leading and trailing whitespace (or specified characters) from a string.

#startswith(value, start, end) - Checks if the string starts with the specified value within the given start and end positions.  
#endswith(value, start, end) - Checks if the string ends with the specified value within the given start and end positions.
