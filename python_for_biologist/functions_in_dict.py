#create a program to demonstrate various functions on dictionaries

di={'one':['A'],'two':['B'],'three':['C']}
print(di)
di['one'].append('new entry')                        #addition of new value
print("new dict: ",di)

'''
output
{'one': ['A'], 'two': ['B'], 'three': ['C']}
new dict:  {'one': ['A', 'new entry'], 'two': ['B'], 'three': ['C']}
'''

di={'one':['A'],'two':['B'],'three':['C']}
d1={'modify':'yes'}
di.update(d1)                                  #updating
print("merged dict: ",di)

'''
output
merged dict:  {'one': ['A'], 'two': ['B'], 'three': ['C'], 'modify': 'yes'}
'''

di={'one':['A'],'two':['B'],'three':['C']}
di['new value']='something'                                  #adding new key and value
print('After adding new key value: ',di)

print('Length of the dictionary: ',len(di))
print("keys of the dictionary: ",di.keys())
print("items of the dictionary: ",di.items())
print("sorted dictionary: ",sorted(di))

'''
output
After adding new key value:  {'one': ['A'], 'two': ['B'], 'three': ['C'], 'new value': 'something'}
Length of the dictionary:  4
keys of the dictionary:  dict_keys(['one', 'two', 'three', 'new value'])
items of the dictionary:  dict_items([('one', ['A']), ('two', ['B']), ('three', ['C']), ('new value', 'something')])
sorted dictionary:  ['new value', 'one', 'three', 'two']
'''