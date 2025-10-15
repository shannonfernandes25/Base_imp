#logical operator

a=int(input("enter the number for a:"))
b=int(input("enter the number for b:"))
c=int(input("enter the number for c:"))
if a > b and c > a:
	print("both conditions are true")
else:
    print('false')
    
'''
output
enter the number for a:100
enter the number for b:10
enter the number for c:1000
both conditions are true

enter the number for a:200
enter the number for b:33
enter the number for c:120
false
'''

