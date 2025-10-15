#program to accept 2 strings and print the common characters
word1=input("Enter the string: ")
word2=input("Enter the string: ")
new=""
for i in word2:                                    #note: word2 is the reference
    if i in word1 and i not in new:                #not in is used to not get repetitive characters
        new=new+i
    else:
        new=new
print("common letters: ",new)


'''
output
Enter the string: biology
Enter the string: bioinformatics
common letters:  bio

Enter the string: maths
Enter the string: bioinformatics
common letters:  mats
'''



word1=input("Enter the string: ")
word2=input("Enter the string: ")
new=""
for i in word2:                                    #note: word2 is the reference
    if i in word1:                                 #repetitive characters are also considered
        new=new+i
    else:
        new=new
print("common letters: ",new)

'''
output
Enter the string: biology
Enter the string: bioinformatics
common letters:  bioioi
'''


word1=input("Enter the string: ").upper()
word2=input("Enter the string: ").upper()
new=""
for i in word2:                                    #note: word2 is the reference
    if i in word1:                
        new=new+i
    else:
        new=new
print("common letters: ",new)

'''
output
Enter the string: khjagbcsthmjk
Enter the string: bndghsnbdh
common letters:  BGHSBH
'''