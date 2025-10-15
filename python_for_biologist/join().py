#join() returns a string in which the elements of sequence have been joined by the str separator
#syntax -> string_name.join(iterable)

#program to demonstrate the use of join function to join list elements with a character
list1=['1','2','3','4','5','6']
s=" ".join(list1)      #gives space between each string
print(s)

'''
output
1 2 3 4 5 6
'''

list1=['1','2','3','4','5','6']
s="  ".join(list1)
print(s)

'''
output
1  2  3  4  5  6
'''

list1=['1','2','3','4','5','6']
s="-".join(list1)
print(s)

'''
output
1-2-3-4-5-6
'''

list1=['1','2','3','4','5','6']
a=":"
s=a.join(list1)
print(s)

'''
output
1:2:3:4:5:6
'''