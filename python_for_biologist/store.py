#Program to take a dictionary having stationary items as keys and their rates as values. Ask the user which item he wants to buy, after buying the items display the exact bill.
store={'book':40,
    'pencil':5,
    'bottle':420,
    'detergents':125,
    'towel':55,
    'dustpan':72,
    'dustbin':180,
    'pouch':62,
    'sanitizer':70
}
item=int(input("Enter the number of item: "))
tot=0
new={}
for i in range(0,item):
    m=input("Enter the name of the item: ")
    n=int(input("Enter the quantity of item: "))
    if m in store:
        tot=tot+(store[m]*n)
        new[m]=[store[m]]
        new[m].append(n)
        new[m].append(store[m]*n)
print("\nSuperstore bill")
for i in new:
    print(i,"=",new[i])
    print("Total amount: ",tot)

'''
output
Enter the number of item: 3
Enter the name of the item: book
Enter the quantity of item: 2
Enter the name of the item: pencil
Enter the quantity of item: 5
Enter the name of the item: pouch
Enter the quantity of item: 1

Superstore bill
book = [40, 2, 80]
Total amount:  167
pencil = [5, 5, 25]
Total amount:  167
pouch = [62, 1, 62]
Total amount:  167
'''