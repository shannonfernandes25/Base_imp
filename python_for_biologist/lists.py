#lists
list1=['DNA','RNA',324,0.6,-2]
print (list1)
print (list1[0])
print (list1[1])
print (list1[2])
print (list1[3])
print (list1[4])
print (len(list1))
print (list1[0:2])



'''
output
['DNA', 'RNA', 324, 0.6, -2]
DNA
RNA
324
0.6
-2
5
['DNA', 'RNA']
'''

'''
python expression              results                                   Description
len((1,2,3))                   3                                         length
(1,2,3)+(4,5,6)                (1,2,3,4,5,6)                             Concatenation
('ATG')*4                      ('ATG','ATG','ATG','ATG')                 Repetition
3 in (1,2,3)                   True                                      Membership
for x in (1,2,3):print x,      1 2 3                                     Iteration
'''

'''
cmp(list1,list2) = compares elements of both the lists
len(list)= gives the total length of the list
max(list)= returns items from the list with max value
min(list)= returns items from the list with min value
'''