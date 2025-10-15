#conditional statement

#if elif else
a=int(input("choose the nnumber: 10  15  20  -"))
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
choose the nnumber: 10  15  20  -10
a is 10

choose the nnumber: 10  15  20  -15
a is 15

choose the nnumber: 10  15  20  -20
a is 20

choose the nnumber: 10  15  20  -200
a is not present
'''