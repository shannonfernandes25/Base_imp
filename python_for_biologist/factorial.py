#python script to find the factorial of the given number
#n!=n*(n-1)*(n-2).....*1
n=int(input("Enter the number: "))
fact=1
while (n>1):
    fact=fact*n
    n=n-1
print('Factorial: ',fact)

'''
output
Enter the number: 4
Factorial:  24

Enter the number: -2
Factorial:  1
'''

#first                      second              third              fourth
#n=4                        n=3                 n=2                n=1
#   4>1                     3>1                 2>1                comes out of loop
#   fact=1*4                fact=4*3            fact=12*2          Factorial: 24
#   fact=4                  fact=12             fact=24
#   n=4-1  n=3              n=3-1  n=2          n=2-1  n=1

n=int(input("Enter the number: "))
fact=1
if (n<1):
    print ("null")
else:
    while (n>1):
        fact=fact*n
        n=n-1
    print('Factorial: ',fact)

'''
output
Enter the number: -4
null

Enter the number: 0                     #factorial of 0 is 1
null

Enter the number: 5
Factorial:  120
'''

n=int(input("Enter the number: "))
fact=1
if (n<0):
    print ("null")
elif (n==0) or (n==1):
    print ("Factorial is 1")
else:
    while (n>1):
        fact=fact*n
        n=n-1
    print('Factorial: ',fact)

'''
output
Enter the number: 3
Factorial:  6

Enter the number: 0
Factorial is 1

Enter the number: 1
Factorial is 1

Enter the number: -7
null
'''




'''
n=int(input("Enter the number: "))
fact=1
if (n<0):
    print ("null")
else:
    while (n>=1):
        fact=fact*n
        n=n-1
    print('Factorial: ',fact)
'''
