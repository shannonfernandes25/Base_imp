#conditional statement

#if elif else
a=int(input("choose the number: 10  15  20  -"))
if (a==10):
    print('a is 10')
elif (a==15):
    print('a is 15')
elif(a==20):
    print('a is 20')
else:
    print('a is not present')
    
'''
output
choose the number: 10  15  20  -10
a is 10

choose the number: 10  15  20  -15
a is 15

choose the number: 10  15  20  -20
a is 20

choose the number: 10  15  20  -200
a is not present
'''

a=int(input("enter the number for a:"))
b=int(input("enter the number for b:"))
if (a>b):
    print("a is greater than b")
elif(a==b):
    print("a is same as b")
else:
    print("a is less than b")

'''
outputenter the number for a:20
enter the number for b:10
a is greater than b

enter the number for a:10
enter the number for b:10
a is same as b

enter the number for a:10
enter the number for b:20
a is less than b
