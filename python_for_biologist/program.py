#program to check if generated random number is equal to 5, print 'you win'. If generated random number is not equal to 5, print 'you loose'

import random

sf=random.randrange(0,10)
print("number generated is: ",sf)
if sf==5:
    print("you win")
else:
    print("you loose")

'''
output
number generated is:  3
you loose

number generated is:  5
you win
'''
	
	
	
#program to generate a random DNA sequence of user defined length and mutate it a number of times
import random

base=['A','T','G','C']
L=int(input("Enter the length: "))
mut=int(input("Enter the position: "))
ch=input("character to be added: ")
new=" "

for i in range(0,L):
    #a=base[random.randrange(0,len(base))]
    new=new+base[random.randrange(0,len(base))]         #base[] ->  list         so base[4]=C     base[2]=T
    print(new)
#incomplete program

'''
output
Enter the length: 8
Enter the position: 3
character to be added: -
 A
 AC
 ACT
 ACTC
 ACTCA
 ACTCAT
 ACTCATA
 ACTCATAA
'''
 
 
 import random

base=['A','T','G','C']
L=int(input("Enter the length: "))
mut=int(input("Enter the position: "))
ch=input("character to be added: ")
new=" "

for i in range(0,L):
    #a=base[random.randrange(0,len(base))]
    new=new+base[random.randrange(0,len(base))]             #base[] ->  list         so base[4]=C     base[2]=T
print(new)
#incomplete program

'''
output
Enter the length: 8
Enter the position: 3
character to be added: *
 TCCGTAGG
'''

import random

base=['A','T','G','C']
L=int(input("Enter the length: "))
mut=int(input("Enter the position: "))
ch=input("character to be added: ")
new=" "

for i in range(0,L):
    new=new+base[random.randrange(0,len(base))]
    a="".join(new[0:mut])
    b="".join(new[(mut+1):L])
    mutation=a+ch+b
print('mutated sequence: ',mutation)

'''
output
Enter the length: 8
Enter the position: 3
character to be added: *
mutated sequence:   GA*ATCT
'''