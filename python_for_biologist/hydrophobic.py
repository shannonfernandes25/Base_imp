#python program to count the number of hydrophobic amino acids in the given sequence
#G,A,V,L,I,P,F,M,W
pro=input('Enter the sequence: ')
length=len(pro)
count=0
for i in range(0,length):                              #last number of the length is not included
    if pro[i]=='G' or pro[i]=='A' or pro[i]=='V' or pro[i]=='L' or pro[i]=='I' or pro[i]=='P' or pro[i]=='F' or pro[i]=='M' or pro[i]=='W':
        count=count+1
    else:
        pass
print('Number of hydrophobic amino acids are: ',count)



'''
output
Enter the sequence: MAPWMHLLTVLALLALWGPNSVQAYSSQHLCGSNLVEALYMTCGRSGFYRPHDRRELEDLQVEQAELGLE
AGGLQPSALEMILQKRGIVDQCCNNICTFNQLQNYCNVPMAPWMHLLTVLALLALWGPNSVQAYSSQHLCGSNLVEALYMTCGRSGFYRPHDRRELEDLQVEQAELGLE

AGGLQPSALEMILQKRGIVDQCCNNICTFNQLQNYCNVP
Number of hydrophobic amino acids are:  37
'''

#python program to count the number of hydrophilic amino acids in the given sequence
#C,Y,N,Q,S,T,H,R,D,E,K
pro=input('Enter the sequence: ')
length=len(pro)
count=0
for i in range(0,length):                              #last number of the length is not included
    if pro[i]=='C' or pro[i]=='Y' or pro[i]=='N' or pro[i]=='Q' or pro[i]=='S' or pro[i]=='T' or pro[i]=='H' or pro[i]=='R' or pro[i]=='D' or pro[i]=='E' or pro[i]=='K':
        count=count+1
    else:
        pass
print('Number of hydrophilic amino acids are: ',count)

'''
output
Enter the sequence: MAPWMHLLTVLALLALWGPNSVQAYSSQHLCGSNLVEALYMTCGRSGFYRPHDRRELEDLQVEQAELGLE
AGGLQPSALEMILQKRGIVDQCCNNICTFNQLQNYCNVPMAPWMHLLTVLALLALWGPNSVQAYSSQHLCGSNLVEALYMTCGRSGFYRPHDRRELEDLQVEQAELGLE

AGGLQPSALEMILQKRGIVDQCCNNICTFNQLQNYCNVP
Number of hydrophilic amino acids are:  33
'''
