#loop statement

codons=["UUU","UUG","AUU","GUU","GAU","GGG"]          #list
for x in codons:
	print(x)                                          #x1=UUU  x2=UUG  x3=AUU  x4=GUU  x5=GAU  x6=GGG 

'''
output
UUU
UUG
AUU
GUU
GAU
GGG
'''

#loop through a string
for x in "biology":
    print (x)

'''
output
b
i
o
l
o
g
y
'''

sub="biology"
for x in sub:
    print (x)

'''
output
b
i
o
l
o
g
y
'''

#break statement
codons=["UUU","UUG","AUU","GUU","GAU","GGG"]
for x in codons:
    print(x)
    if x=="GAU":
        break

'''
output
UUU
UUG
AUU
GUU
GAU
'''

codons=["UUU","UUG","AUU","GUU","GAU","GGG"]
for x in codons:
   if x=="GAU":
        break
   print(x)

'''
output
UUU
UUG
AUU
GUU
'''

#continue statement
codons=["UUU","UUG","AUU","GUU","GAU","GGG"]
for x in codons:
   if x=="GAU":
        continue
   print(x)

'''
output
UUU
UUG
AUU
GUU
GGG
'''

#range ()
for x in range(6):                     #by de3fault starts from 0 and increments
    print(x)

'''
output
0
1
2
3
4
5
'''

for x in range(2,6):
    print(x)

'''
output
2
3
4
5
'''

for x in range(2,30,3):              #3 is the increment value
    print(x)

'''
output
2
5
8
11
14
17
20
23
26
29
'''

#else in loop
for x in range(6):
    print(x)
else:
    print("Finally finished")
    
'''
output
0
1
2
3
4
5
Finally finished
'''

for x in range(1,11,2):
    print(x)
else:
    print("Finally finished")

'''
output
1
3
5
7
9
Finally finished
'''

for x in range(1,11,2):
    #print(x)
else:
    print("Finally finished")

'''
output
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 4
    else:
    ^^^^
IndentationError: expected an indented block after 'for' statement on line 2
'''

for x in range(1,11,2):
    #print(x)
    pass
else:
    print("Finally finished")

'''
output
Finally finished
'''