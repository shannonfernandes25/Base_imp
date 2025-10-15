
#Calculate GC Content
num_A=10
num_T=7
num_G=5
num_C=8
GC=((num_G+num_C)/(num_A+num_T+num_G+num_C))*100
print("GC content:",GC)


'''
output
GC content: 43.333333333333336
'''

#Calculate GC Content
num_A=int(input('enter A:'))
num_T=int(input('enter T:'))
num_G=int(input('enter G:'))
num_C=int(input('enter C:'))
GC=((num_G+num_C)/(num_A+num_T+num_G+num_C))*100
print("GC content:",GC)

'''
output
enter A:21
enter T:32
enter G:11
enter C:17
GC content: 34.5679012345679
,,,