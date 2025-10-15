#Adding elements to the list
'''
append()  ->  only one element at a time can be added to the list
              for addition of multiple elements loops are used
              works for addition of elements at the end of a list
insert()  ->  addition of elements at the desired position
              requires two arguments (position,value)
extend()  ->  to add multiple elements at the same time at the end of the list
remove()  ->  to remove elements from the list
              to remove range of elements, iterator is used
			  removes specified item
pop()     ->  remove and return an element from the set
              default removes the last element of the set
			  to remove element from the specific position, index of the element is passed as an argument to the pop() method
'''

'''
clear()    removes all items from tghe list
index()    returns the index of the first matched item
sort()     sort items in a list in ascending order
reverse()  reverse the order of items in a list
copy()     returns a copy of the list
'''

#list operation



#append()

#Creating a list
list = []
print("blank list: ",list)

#Addition of elements in the list
list.append(1)
list.append(2)
list.append("Bioinformatics")
print("List after addition of elements from 1-3: ",list)

#Addition of elements to the list by iteration
for i in range(5,11):
    list.append(i)
print("List after addition of elements from 5-11: ",list)

#Addition of a list to a list
list2=["histone","DNA"]
list.append(list2)
print('List after addition of a list: ',list)

'''
output
blank list:  []
List after addition of elements from 1-3:  [1, 2, 'Bioinformatics']
List after addition of elements from 5-11:  [1, 2, 'Bioinformatics', 5, 6, 7, 8, 9, 10]
List after addition of a list:  [1, 2, 'Bioinformatics', 5, 6, 7, 8, 9, 10, ['histone', 'DNA']]
'''

#insert()
List=[1,2,3,4]
print("Initial list: ",List)

#Addition of element at a specific position
List.insert(3,'Java')
List.insert(0,'Python')
print('list after adding elements: ',List)

'''
output
Initial list:  [1, 2, 3, 4]
list after adding elements:  ['Python', 1, 2, 3, 'Java', 4]
'''

#extend()
list=[1,2,3,4]
print('Initial list: ',list)

list.extend(['Met','DNA','RNA'])
print('list after extend operation: ',list)

'''
output
Initial list:  [1, 2, 3, 4]
list after extend operation:  [1, 2, 3, 4, 'Met', 'DNA', 'RNA']
'''

#remove
list=[1,2,3,4,'DNA',5,6,7,47,8,9,'RNA',10,11]
print('Initial list: ',list)

list.remove('DNA')     #not position number, its character in the list
list.remove('RNA')
list.remove(47)
print('list after removal of 3 elements: ',list)

#using iterator method
for i in range(1,5):
    list.remove(i)
print('list after iteration removal: ',list)

'''
output
Initial list:  [1, 2, 3, 4, 'DNA', 5, 6, 7, 47, 8, 9, 'RNA', 10, 11]
list after removal of 3 elements:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list after iteration removal:  [5, 6, 7, 8, 9, 10, 11]
'''

#pop
list=[1,2,3,4,5]
list.pop()    #removes last element
print('list after popping an element: ',list)

#removing element at a specific position
list.pop(2)    #position
print('list after popping a specific element: ',list)

'''
output
list after popping an element:  [1, 2, 3, 4]
list after popping a specific element:  [1, 2, 4]
'''
















