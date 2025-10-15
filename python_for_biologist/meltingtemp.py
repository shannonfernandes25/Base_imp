#program to calculate the GC content and melting temperature of the DNA sequence
#Tm=(wA+xT)*2 + (yG+zC)*4
#GC Content=(count of (G+C)/count of (A+T+G+C))*100
seq=input("Enter the DNA sequence: ").upper()
size=len(seq)
print("the length of the sequence is ",size)
gc=0
at=0
for i in seq:
    if (i=="G" or i=="C"):
        gc+=1
    else:
        i=="A" or i=="T"
        at+=1
    Tm=(at*2)+(gc*4)
    GC=(gc/size)*100
print("GC Content: ","%.2f"%GC)
print("Melting Temperature: ","%.2f"%Tm)

'''
output
Enter the DNA sequence: atgccgtaERROR!

the length of the sequence is  8
GC Content:  50.00
Melting Temperature:  24.00
'''