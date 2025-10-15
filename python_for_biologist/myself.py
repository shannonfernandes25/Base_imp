#program1
num=int(input('Enter the number: '))
remainder=num%2
if (remainder==0):
    new_number=num/2
    print('quotient: ',new_number)
else:
    new_number=(num*3)+1
    print('new number: ',new_number)

'''
output
Enter the number: 8
quotient:  4.0

Enter the number: 9
new number:  28
'''




#program2
m1=int(input('Enter the marks of subject1: '))
m2=int(input('Enter the marks of subject2: '))
m3=int(input('Enter the marks of subject3: '))
total=(m1+m2+m3)
average=(total/3)
percentage=(total/300)*100
print('Total: ',total)
print('Average marks: ',average)
print('Percentage: ',percentage)
if average>80:
    print('Distinction')
elif (average>60 and average<=80):
    print('First class')
elif (average>40 and average<=60):
    print('Second class')
else:
    print('No class. Fail')


'''
output
Enter the marks of subject1: 80
Enter the marks of subject2: 89
Enter the marks of subject3: 85
Total:  254
Average marks:  84.66666666666667
Percentage:  84.66666666666667
Distinction

Enter the marks of subject1: 65
Enter the marks of subject2: 71
Enter the marks of subject3: 78
Total:  214
Average marks:  71.33333333333333
Percentage:  71.33333333333334
First class

Enter the marks of subject1: 45
Enter the marks of subject2: 53
Enter the marks of subject3: 59
Total:  157
Average marks:  52.333333333333336
Percentage:  52.33333333333333
Second class

Enter the marks of subject1: 38
Enter the marks of subject2: 32
Enter the marks of subject3: 35
Total:  105
Average marks:  35.0
Percentage:  35.0
No class. Fail
'''