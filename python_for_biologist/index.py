#index
str=("ATGGTCCGAGGG")
loc=str.index("GGG")                   #index function is used to give the position number
print(loc)

'''
output
9
'''

str=("ATG GTC CGA GGG")
loc=str.index("GGG")
print(loc)

'''
output
12
'''



#program to accept protein sequence and also ask for a motiff from the user. If the motiff is present in the protein sequence then print its position
pro=input("Enter the protein sequence: ").upper()
mot=input("Enter the motiff sequence: ").upper()
if (mot in pro):
    loc=pro.index(mot)
    print("Motiff position number: ",loc)
else:
    print("Motiff not found")

'''
output
Enter the protein sequence: phnsfhahddntukf
Enter the motiff sequence: ahdd
Motiff position number:  6

Enter the protein sequence: TGFDahgyAGChyndjagc
Enter the motiff sequence: agc
Motiff position number:  8
'''

