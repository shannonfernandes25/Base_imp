#program to check whether the first and last character of the string are equal
'''
 M  A  D  A  M
 0  1  2  3  4
-5 -4 -3 -2 -1
slice operation [start:end:step]
step value of -1 reverses a string
'''

string=input("Enter the string: ").upper()
if (string[0]==string[-1:-2:-1]):
    print("Same letters")
else:
    print("Not same letters")

'''
output
Enter the string: madam
Same letters

Enter the string: Anusha     #only first and last are same characters
Same letters

Enter the string: bangalore
Not same letters
'''

#program to chech whether the given input is palindrome or not
string=input("Enter the string: ").upper()
if (string==string[::-1]):
    print("it is a palindrome")
else:
    print("Not palindrome")


'''
output
Enter the string: madam
it is a palindrome

Enter the string: Anusha
Not palindrome

Enter the string: bangalore
Not palindrome
'''

str=("ATGC")
print(str[-1])

'''
output
C
'''

