#dictionary
'''
={key : value}
'''

dict={'Name':'Shannon'" "'ramesh'" "'suresh'" "'raju','Age': 22,'Class': 'First'}
print(dict)
print(dict['Name'])
print (dict['Age'])

'''
output
{'Age': 22, 'Name': 'Shannon ramesh suresh raju', 'Class': 'First'}
Shannon ramesh suresh raju
22
'''

dict={'name':'shannon','Age':27,'Class':'First'}
dict['Age']=22        #updating dictionary
dict['School']='St Marys School'      #adding new entry

print("new age: ",dict['Age'])
print('School:',dict['School'])


'''
output
('new age: ', 22)
('School:', 'St Marys School')
'''

'''
Built-in Dictionary functions
cmp(dict1,dict2) = compares elements of both the dicts
len(dict)= gives the total length of the dict
str(dict)= produces a printable string representation of dictionary
type(dict)= returns the type of the passed variable, if variable is dictionary then it would return a dictionary type
'''