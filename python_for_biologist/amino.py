#Create a list with 20 proteins using single letter code (Eg-A,M etc), input a protein sequence and display position of each base in sequence with respect to its position
amino=['G','P','A','V','L','I','M','C','F','Y','W','H','K','R','Q','N','E','D','S','T']
seq=input("Enter the protein sequence: ").upper()
pos=[]
                                          #add if statement
for i in range(0,len(seq)):
    loc=amino.index(seq[i])
    pos.append(loc)
print('sequence: ',seq)
print("position: ",pos)

'''
output
Enter the protein sequence: GMSARTHLSDRYQHILKATIQHYIATAEPVGSKTLLEEYKFTVSSATIRNALGKLEKEG 
sequence:  GMSARTHLSDRYQHILKATIQHYIATAEPVGSKTLLEEYKFTVSSATIRNALGKLEKEG
position:  [0, 6, 18, 2, 13, 19, 11, 4, 18, 17, 13, 9, 14, 11, 5, 4, 12, 2, 19, 5, 14, 11, 9, 5, 2, 19, 2, 16, 1, 3, 0, 18, 12, 19, 4, 4, 16, 16, 9, 12, 8, 19, 3, 18, 18, 2, 19, 5, 13, 15, 2, 4, 0, 12, 4, 16, 12, 16, 0]
'''