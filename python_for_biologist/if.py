#conditional statement

#if 
a=13
b=200
if (b>a):
  print ('b is greater than a')    #space is important
else:
        print ('a is greater than b')

'''
output
b is greater than a
'''

a=333
b=200
if (b>a):
  print ('b is greater than a')    #space is important
else:
        print ('a is greater than b')

'''
output
a is greater than b
'''

#nested if
x=int(input('Enter the number:'))
if x>10:
	print('above 10')
	if x>20:
		print('above 20')
	else:                             #take care of indentationS
		print('not above 20')

'''
output
Enter the number:12
above 10
not above 20

Enter the number:35
above 10
above 20
'''

#pass
a=int(input("enter the number:"))
b=int(input("enter the number:"))
if a>b:
    pass
else:
    print("b is greater than a")

'''
output
enter the number:20
enter the number:10
=== Code Execution Successful ===

enter the number:15
enter the number:25
b is greater than a
=== Code Execution Successful ===
'''

