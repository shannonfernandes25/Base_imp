#defining a function with arguments

#one arguments
def my_function(f_name):
    print(f_name + "Joseph")
    
my_function("Ian")     
my_function("Shannu")
my_function("Fernandes")

'''
output
IanJoseph
ShannuJoseph
FernandesJoseph
'''

def my_function(f_name):
    print(f_name + " Joseph")             #space after "
    
my_function("Ian")     
my_function("Shannu")
my_function("Fernandes")

'''
output
Ian Joseph
Shannu Joseph
Fernandes Joseph
'''


#two arguments
def my_function(f_name,l_name):
    print(f_name + " " + l_name)
    
my_function("shannon","fernandes")     
my_function("ramesh","rathod") 

'''
output
shannon fernandes
ramesh rathod
'''


def my_function(f_name,l_name):
    print(f_name + " " + l_name)
    
my_function("shannon","fernandes")     
my_function("ramesh") 

'''
output
shannon fernandes
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 5, in <module>
TypeError: my_function() missing 1 required positional argument: 'l_name'
'''


#arbitrary arguments
def my_function(*kids):
    print("my youngest child is: " + kids[2])
    
my_function("shannon","fernandes","johny")   

'''
output
my youngest child is: johny
'''

def my_function(*kids):
    print("my youngest child is: " + kids[1])
    
my_function("shannon","fernandes","johny") 

'''
output
my youngest child is: fernandes
'''


#keyword arguments (key - value syntax format)
def my_function(child3,child2,child1):
    print("my youngest child is " + child3)
    
my_function(child1="shannon",child2="fernandes",child3="johny") 

'''
output
my youngest child is johny
'''

def my_function(child3,child2,child1):
    print("my youngest child is " + child2)
    
my_function(child1="shannon",child2="fernandes",child3="johny") 

'''
output
my youngest child is fernandes
'''



#arbitrary kerwords arguments (**kwargs)
def my_function(**kid):
    print("my youngest child is " + kid["l_name"])
    
my_function(f_name="shannon",l_name="fernandes") 

'''
output
my youngest child is fernandes
'''




def my_function(seq):
    for x in seq:
        print(x)
codons=['ATG','TGA','GAC']
my_function(codons)

'''
output
ATG
TGA
GAC
'''

 