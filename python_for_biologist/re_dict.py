#write the script to read the following data from a text file
#Samuel:Mangalore,1995,93
#Vinod:Bangalore, 2001,82
#Sana:Udupi,2000,84
#By reading data from the file, create a dictionary using the name as key (Samuel, Vinod, Sana) and the rest of the string as 
#a list of values Eg: {"Samuel":[Mangalore,1995,93]} Use the dictionary to extract name and year
#output should be 
#Samuel: 1995
#Vinod: 2001
#Sana:2000
fo = open('data.txt','r')
d={}
for i in range(0,3):
    k = fo.readline()    #readlines is not used as it returns data in the form of list
    print(k)
    
'''
output
Samuel:Mangalore,1995,93

Vinod:Bangalore, 2001,82

Sana:Udupi,2000,84
'''


fo = open('data.txt','r')
d={}
for i in range(0,3):
    k = fo.readline()    #readlines is not used as it returns data in the form of list
    sp1 = k.split(":")
    print(sp1)
    
'''
output
['Samuel', 'Mangalore,1995,93\n']
['Vinod', 'Bangalore, 2001,82\n']
['Sana', 'Udupi,2000,84\n']
'''

fo = open('data.txt','r')
d={}
for i in range(0,3):
    k = fo.readline()    #readlines is not used as it returns data in the form of list
    sp1 = k.split(":")
    print(sp1[0])
    
'''
output
Samuel
Vinod
Sana
'''

fo = open('data.txt','r')
d={}
for i in range(0,3):
    k = fo.readline()    #readlines is not used as it returns data in the form of list
    sp1 = k.split(":")
    #print(sp1[0])
    d[sp1[0]] = []
    print(d)
    
'''
output
{'Samuel': []}
{'Samuel': [], 'Vinod': []}
{'Samuel': [], 'Vinod': [], 'Sana': []}
'''

fo = open('data.txt','r')
d={}
for i in range(0,3):
    k = fo.readline()    #readlines is not used as it returns data in the form of list
    sp1 = k.split(":")
    #print(sp1[0])
    d[sp1[0]] = []
    #print(d)
    sp2 = sp1[1].replace("\n","").split(",")
    print(sp2)
    
'''
output
['Mangalore', '1995', '93']
['Bangalore', ' 2001', '82']
['Udupi', '2000', '84']
'''

fo = open('data.txt','r')
d={}
for i in range(0,3):
    k = fo.readline()    #readlines is not used as it returns data in the form of list
    sp1 = k.split(":")
    #print(sp1[0])
    d[sp1[0]] = []
    #print(d)
    sp2 = sp1[1].replace("\n","").split(",")
    #print(sp2)
    #print("Dictionary is: ",d)
    for i in range(0,3):
        d[sp1[0]].append(sp2[i])
    #print("Dictionary is: ",d)
    
'''
output
Dictionary is:  {'Samuel': ['Mangalore', '1995', '93']}
Dictionary is:  {'Samuel': ['Mangalore', '1995', '93'], 'Vinod': ['Bangalore', ' 2001', '82']}
Dictionary is:  {'Samuel': ['Mangalore', '1995', '93'], 'Vinod': ['Bangalore', ' 2001', '82'], 'Sana': ['Udupi', '2000', '84']}
'''

fo = open('data.txt','r')
d={}
for i in range(0,3):
    k = fo.readline()    #readlines is not used as it returns data in the form of list
    sp1 = k.split(":")
    #print(sp1[0])
    d[sp1[0]] = []
    #print(d)
    sp2 = sp1[1].replace("\n","").split(",")
    #print(sp2)
    #print("Dictionary is: ",d)
    for i in range(0,3):
        d[sp1[0]].append(sp2[i])
    #print("Dictionary is: ",d)
print("Dictionary is: ",d)
for i in d:
    print(i, ":", d[i][1])   # d[key][value]
    
'''
output
Dictionary is:  {'Samuel': ['Mangalore', '1995', '93'], 'Vinod': ['Bangalore', ' 2001', '82'], 'Sana': ['Udupi', '2000', '84']}
Samuel : 1995
Vinod :  2001
Sana : 2000
'''