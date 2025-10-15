#tuples
tup1=("chemistry","physics",1997,2000)
tup2=(1,2,3,4,5,6,7)
print("tup1[0]: ",tup1[0])
print("tup2[1:5]: ",tup2[1:5])

'''
output
('tup1[0]:', 'chemistry')
('tup2[1:5]:', (2, 3, 4, 5))
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
cmp(tuple1,tuple2) = compares elements of both the tuples
len(tuple)= gives the total length of the tuple
max(tuple)= returns items from the tuple with max value
min(tuple)= returns items from the tuple with min value
tuple(seq)= converts a tuple into a list
'''