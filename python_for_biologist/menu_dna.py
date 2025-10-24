# Menu driven program to have functions for:
# 1) DNA Ligase
# 2) Transcribe to RNA sequence
# 3) Base count of a DNA Sequence
# 4) Location of a codon in a sequence

def ligase(d1, d2):
    d3 = d1 + d2
    print("DNA sequence after ligation: ", d3)

def RNA(d1):
    rna = d1.replace("T", "U")
    print("RNA sequence: ", rna)

def dna_count(d1):
    print("count of A:", d1.count('A'))
    print("count of T:", d1.count('T'))
    print("count of G:", d1.count('G'))
    print("count of C:", d1.count('C'))

def pattern(pt, d1):
    if pt in d1:
        print("Index of pattern is:", d1.index(pt))
    
print("Sequence Analysis")

while True:
    print("\n Main menu")
    print("1. DNA ligase")
    print("2. RNA sequence")
    print("3. Base pair count")
    print("4. Location of codon in a sequence")
    print("5. Exit")
    
    choice = int(input("Enter the choice: "))
    
    if choice == 1:
        d1 = (input("Enter the first DNA sequence: ")).upper()
        d2 = (input("Enter the second DNA sequence: ")).upper()
        ligase(d1, d2)
    elif choice == 2:
        d1 = (input("Enter the DNA sequence: ")).upper()
        RNA(d1)
    elif choice == 3:
        d1 = (input("Enter the DNA sequence: ")).upper()
        dna_count(d1)
    elif choice == 4:
        d1 = (input("Enter the DNA sequence: ")).upper()
        pt = (input("Enter the codon: ")).upper()
        pattern(pt, d1)
    elif choice == 5:
        break
    else:
        print("Incorrect choice")
        
        
        
'''
output
Sequence Analysis

 Main menu
1. DNA ligase
2. RNA sequence
3. Base pair count
4. Location of codon in a sequence
5. Exit
Enter the choice: 6
Incorrect choice

 Main menu
1. DNA ligase
2. RNA sequence
3. Base pair count
4. Location of codon in a sequence
5. Exit
Enter the choice: 1
Enter the first DNA sequence: atgcatgc
Enter the second DNA sequence: cgtacgta
DNA sequence after ligation:  ATGCATGCCGTACGTA

 Main menu
1. DNA ligase
2. RNA sequence
3. Base pair count
4. Location of codon in a sequence
5. Exit
Enter the choice: 2
Enter the DNA sequence: atgcatgc
RNA sequence:  AUGCAUGC

 Main menu
1. DNA ligase
2. RNA sequence
3. Base pair count
4. Location of codon in a sequence
5. Exit
Enter the choice: 3
Enter the DNA sequence: ERROR!
atgccagtcatg
count of A: 3
count of T: 3
count of G: 3
count of C: 3

 Main menu
1. DNA ligase
2. RNA sequence
3. Base pair count
4. Location of codon in a sequence
5. Exit
Enter the choice: 4
Enter the DNA sequence: atgcagtttgcagca
Enter the codon: ttt
Index of pattern is: 6

 Main menu
1. DNA ligase
2. RNA sequence
3. Base pair count
4. Location of codon in a sequence
5. Exit
Enter the choice: 5

=== Code Execution Successful ===
'''