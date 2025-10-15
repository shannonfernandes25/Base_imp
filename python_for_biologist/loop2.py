#loop statements

#nested loop                            inner loop will be executed one time for each iteration of the outer loop
cd = ("AAA","UUU","AUG")
seq=("AUGACU","AUGCCGUA","CGUAAUGC")
for x in cd:
    for y in seq:
        print(x,y)

'''
output
AAA AUGACU
AAA AUGCCGUA
AAA CGUAAUGC
UUU AUGACU
UUU AUGCCGUA
UUU CGUAAUGC
AUG AUGACU
AUG AUGCCGUA
AUG CGUAAUGC
'''

#while loop
i=1
while i<6:
    print(i)
    i+=1

'''
output
1
2
3
4
5
'''

i=1
while i<=6:
    print(i)
    i+=1

'''
output
1
2
3
4
5
6
'''

#break statement
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

'''
output
1
2
3
'''

i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

'''
output
1
2
4
5
6
'''

#pass statement
i=0
while i<6:
    i+=1
    if i==3:
        pass
    print(i)

'''
output
1
2
3
4
5
6
'''

#else statement
i=0
while i<6:
    print(i)
    i+=1
else:
    print("i is not less than 6")
    
'''
output
0
1
2
3
4
5
i is not less than 6
'''