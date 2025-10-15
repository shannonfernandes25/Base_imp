#dictionary Operations
reg={}
reg={151801:'Neha',151802:"raju",151803:'Ramesh'}
print(reg)
#update with new key value pair
reg.update({151804:"Suresh"})
print(reg)

'''
output
{151801: 'Neha', 151802: 'raju', 151803: 'Ramesh'}
{151801: 'Neha', 151802: 'raju', 151803: 'Ramesh', 151804: 'Suresh'}
'''


#copy()

reg={}
reg={151801:'Neha',151802:"raju",151803:'Ramesh'}
print(reg)
#copy()
new_reg=reg.copy()
print("new dict: ",new_reg)

'''
output
{151801: 'Neha', 151802: 'raju', 151803: 'Ramesh'}
new dict:  {151801: 'Neha', 151802: 'raju', 151803: 'Ramesh'}
'''



#fromkeys()

abc={'a','e','i','o','u'}
print(abc)
vowels=dict.fromkeys(abc)
print(vowels)

'''
output
{'o', 'i', 'u', 'a', 'e'}
{'o': None, 'i': None, 'u': None, 'a': None, 'e': None}
'''

abc={'a','e','i','o','u'}
print(abc)
val='vowel'
new_dict=dict.fromkeys(abc,val)    #(dictionary,value to be added)
print(new_dict)

'''
output
{'u', 'a', 'i', 'e', 'o'}
{'u': 'vowel', 'a': 'vowel', 'i': 'vowel', 'e': 'vowel', 'o': 'vowel'}
'''


#get()
codon={'TCA':'S',"TCC":"A","ATG":"M"}
print(codon.get("ATG"))

'''
output
M 
'''

#items()-converts key and value pairs to tuples
codon={'TCA':'S',"TCC":"A","ATG":"M"}   
print(codon.items())

'''
output
dict_items([('TCA', 'S'), ('TCC', 'A'), ('ATG', 'M')])
'''

codon={'TCA':'S',"TCC":"A","ATG":"M"}   
#print(codon.items())
for a,b in codon.items():   #a->key   b->value
    print(a)

'''
output
TCA
TCC
ATG
'''

#keys()
codon={'TCA':'S',"TCC":"A","ATG":"M"}   
print(codon.keys()

'''
output
dict_keys(['TCA', 'TCC', 'ATG'])
'''

#values()
codon={'TCA':'S',"TCC":"A","ATG":"M"}   
print(codon.values())

'''
output
dict_values(['S', 'A', 'M'])
'''

#popitem()
codon={'TCA':'S',"TCC":"A","ATG":"M"}   
print(codon)
codon.popitem()
print(codon)

'''
output
{'TCA': 'S', 'TCC': 'A', 'ATG': 'M'}
{'TCA': 'S', 'TCC': 'A'}
'''

#pop()
codon={'TCA':'S',"TCC":"A","ATG":"M"}   
print(codon)
codon.pop("TCA")
print(codon)

'''
output
{'TCA': 'S', 'TCC': 'A', 'ATG': 'M'}
{'TCC': 'A', 'ATG': 'M'}
'''






