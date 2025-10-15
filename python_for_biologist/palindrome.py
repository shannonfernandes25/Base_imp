#python script to check whether the given string is palindrome or not
query=input("Enter the string: ")
length=len(query)
#print(length)
#print(query[3])
begin = 0                                 #begin is variable
end=length-1                              #since position of string starts from 0 instead of 1
status=1

while (begin<end):
    if (query[begin]==query[end]):
        begin=begin+1
        end=end-1
    else:
        status=0
        break

if (status==1):
    print(f'{query} is Palindrome')
else:
    print(f'{query} is Non-palindrome')
    
    
    
    
    '''
    m a d a m
    length=5
    begin=0
    end=4
    
    0<4                  1<3          2<2 comes out of loop            
    m==m                 a==a                   
    begin=1              begin=2      
    end=3                end=2        
    '''

'''
output
Enter the string: Bangalore
Bangalore is Non-palindrome

Enter the string: madam
madam is Palindrome
'''