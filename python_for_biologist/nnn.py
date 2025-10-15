#program to accept an integer n and compute the value of n+nn+nnn
n=int(input('Enter the number: '))
result=n+(n*n)+(n*n*n)
print('The result of n+nn+nnn is: ',result)

'''
output
Enter the number: 2
The result of n+nn+nnn is:  14

Enter the number: 5
The result of n+nn+nnn is:  155

Enter the number: 1
The result of n+nn+nnn is:  3
'''