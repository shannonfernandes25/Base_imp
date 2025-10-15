#python script to check the presence of particular element in the list
clrs=['red','green','blue','yellow','purple','orange','brown','pink']
status=0
for i in clrs:
    if i=='green':
        status=1
if status==1:
    print("present")
else:
    print("not present")


'''
output
present
'''


clrs=['red','blue','yellow','purple','orange','brown','pink']
status=0
for i in clrs:
    if i=='green':
        status=1
if status==1:
    print("present")
else:
    print("not present")

'''
output
not present
'''