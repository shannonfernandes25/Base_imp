#program to print the characters of the second string not in first string
word1="usha"
word2="Anusha"
val=""       #val variable is empty
for i in word2:
    if i not in word1:
        val=val+i
    else:
        val=val
print("characters of the 2nd string not in 1st string: ",val)

'''
output
characters of the 2nd string not in 1st string:  An
'''



word1="usha".upper()
word2="Anusha".upper()
val=""       #val variable is empty
for i in word2:
    if i not in word1:
        val=val+i
    else:
        val=val
print("characters of the 2nd string not in 1st string: ",val)

'''
output
characters of the 2nd string not in 1st string:  N
'''


word1=input("Enter the first string: ").upper()
word2=input("Enter the second string: ").lower()
val=""       #val variable is empty
for i in word2:
    if i not in word1:
        val=val+i
    else:
        val=val
print("characters of the 2nd string not in 1st string: ",val)

'''
output
Enter the first string: biology is my favourite subject
Enter the second string: bio and informatics
characters of the 2nd string not in 1st string:  bioandinformatics
'''



word1=input("Enter the first string: ").upper()
word2=input("Enter the second string: ").upper()
val=""       #val variable is empty
for i in word2:
    if i not in word1:
        val=val+i
    else:
        val=val
print("characters of the 2nd string not in 1st string: ",val)


'''
output
Enter the first string: bio and informatics
Enter the second string: biology is my favourite subject
characters of the 2nd string not in 1st string:  LGYYVUEUJE

Enter the first string: atgccgtatgcgcatgERROR!
Enter the second string: augccgacguguacERROR!
characters of the 2nd string not in 1st string:  UUU
'''