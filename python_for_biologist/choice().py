#random()   ->    generates random number between 0.0 to 1.0
    #choice()                   ->    returns a random item from the list, tuple or string
    #randrange(beg,end,step)    ->    generate random number from specified range and also allow steps to be included


#program to demonstrate the use of choice() method

#import random
import random      #imp step
#print a random value from the list
list1=[1,2,3,4,5,6]
print(random.choice(list1))

'''
output
3

output
5

output
1
'''

#import random
import random      #imp step
#print a random item from the string
string='ATGCGTAAGATACGGCGTGATCTGTA'
print (random.choice(string))

'''
output
T

output
A 
'''

#program to demonstrate randrange()

#import random
import random      #imp step
#print a random value from the range
print (random.randrange(20,50,3))

'''
output
35

output
32
'''