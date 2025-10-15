#program to accept a sequence of lines and print the lines after capitalizing each char in the string
seq=input("Enter the sequence of lines: ")
print(seq.upper())

'''
output
Enter the sequence of lines: atgatctgcat
ATGATCTGCAT

Enter the sequence of lines: ATGCCGTA
ATGCCGTA
'''


seq=input("Enter the sequence of lines: ")
print(seq.lower())

'''
output
Enter the sequence of lines: ATGCCGTA
ERROR!
atgccgta
'''



#islower() isupper()        checks for true or false condition

#program to count the uppercase and lowercase in a string
string=input("Enter the string: ")
count_up=0
count_low=0

for letter in string:                                     #instead of i, letter is used
    if (letter.isupper()):
        count_up=count_up+1
    elif (letter.islower()):
        count_low=count_low+1
    else:                                                 #for space, comma, etc
        pass
print("Number of uppercase letters: ",count_up)
print("Number of lowercase letters: ",count_low)

'''
output
Enter the string: IllUminAti
Number of uppercase letters:  3
Number of lowercase letters:  7

Enter the string: Hello Python!
Number of uppercase letters:  2
Number of lowercase letters:  9
'''




