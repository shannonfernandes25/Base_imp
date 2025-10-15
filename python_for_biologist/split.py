#program to convert string to list
str1=input("Enter the sequence: ").upper()
li=str1.split(" ")                                      # split function converts string to list
print(li)

'''
output
Enter the sequence: atgccgtatgcaERROR!
['ATGCCGTATGCA']

Enter the sequence: atg gca tgc cga
['ATG', 'GCA', 'TGC', 'CGA']
'''
