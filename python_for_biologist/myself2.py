#program to collect nucleotide sequence from user and count the number of 'N' present in the sequence
seq=input("Enter the sequence: ")
length=len(seq)
count=0
for i in range(0,length):
    if seq[i]=="N":
        count+=1
    else:
        pass
print("Number of deciphered sequence: ",count)

'''
output
Enter the sequence: AGTCCGTAANGTAATATGCCGTANGTACNCGCTCA
Number of deciphered sequence:  3
'''





#program to collect data from the user and check whether it begins with '>' symbol or not
str=input("Enter the string: ")
if str[0]=='>':
    print("yes,it begins with '>' symbol")
else:
    print("No '>' symbol found")

'''
output
Enter the string: >AGTCCGTA
yes,it begins with '>' symbol
'''


#program to check whether the sentence ends with fullstop or not
str=input("Enter the string: ")
length=len(str)
end=length-1
if str[end]=='.':
    print("yes,it ends with fullstop")
else:
    print("No fullstop found")

'''
output
Enter the string: AGTCCGTA.
yes,it ends with fullstop

Enter the string: AGTCCGTA
No fullstop found 
'''