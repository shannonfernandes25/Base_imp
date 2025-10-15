#write a python script to demonstrate tuple functions
li=[]
for i in range(0,5):
    n=int(input("Enter the numbers: "))
    li.append(n)
tup=tuple(li)
print("tuple: ",tup)
print("sorted: ",sorted(tup))
print("max: ",max(tup))
print("min: ",min(tup))
print("sum: ",sum(tup))
print("length: ",len(tup))

'''
output
Enter the numbers: 23
Enter the numbers: 76
Enter the numbers: 34
Enter the numbers: 90
Enter the numbers: 119
tuple:  (23, 76, 34, 90, 119)
sorted:  [23, 34, 76, 90, 119]
max:  119
min:  23
sum:  342
length:  5
'''



#write a python script to enter a seven amino acid. a)Convert the string to list. b)Create a tuple from the list. c)make changes to fifth value (*) in the amino acid and store it.
amino=input("Enter the sequence: ")
if len(amino)>=7:
    li=list(amino)
    print("list is: ",li)
    tup=tuple(amino)
    print("tuple is: ",tup)
    li[4]="*"
    print("amino acids: ","".join(li))

'''
output
Enter the sequence: ghffdsxdcbvhjhknkmihbgv
list is:  ['g', 'h', 'f', 'f', 'd', 's', 'x', 'd', 'c', 'b', 'v', 'h', 'j', 'h', 'k', 'n', 'k', 'm', 'i', 'h', 'b', 'g', 'v']
tuple is:  ('g', 'h', 'f', 'f', 'd', 's', 'x', 'd', 'c', 'b', 'v', 'h', 'j', 'h', 'k', 'n', 'k', 'm', 'i', 'h', 'b', 'g', 'v')
amino acids:  ghff*sxdcbvhjhknkmihbgv
'''