#python script to find the factorial of the given number   (for loop)
#n!=n*(n-1)*(n-2).....*1
n=int(input("Enter the number: "))
fact=1
if (n<0):
    print("null")
elif (n==0) or (n==1):
    print('Factorial is 1')
else:
    for i in range(1,n+1):               #in range, last number is not considered so n+1
        fact=fact*i
    print ("Factorial: ",fact)


'''
n=4
fact=1

i=1
fact=1*1   fact=1

i=2
fact=1*2 fact=2

i=3
fact=2*3  fact=6

i=4
fact=6*4  fact=24
'''

'''
output
Enter the number: 0
Factorial is 1

Enter the number: 1
Factorial is 1

Enter the number: -2
null

Enter the number: 4
Factorial:  24
'''

n=int(input("Enter the number: "))
fact=1
for i in range(0,n):
    fact=fact+fact*i
print("Factorial: ",fact)

'''
output
Enter the number: 4
Factorial:  24

Enter the number: 1
Factorial:  1

Enter the number: 0
Factorial:  1

Enter the number: -2            #ans should be null
Factorial:  1
'''

n=int(input("Enter the number: "))
fact=1
if (n<0):
    print("Null")
else:
    for i in range(0,n):
        fact=fact+fact*i
    print("Factorial: ",fact)

'''
output
Enter the number: -2
Null
'''