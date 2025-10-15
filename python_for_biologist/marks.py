#program to calculate percentage scored by students
name=input("Enter the name: ")
roll_no=(input("Enter the roll number: "))
print("Enter the marks")
m1=int(input("sub1: "))
m2=int(input("sub2: "))
m3=int(input("sub3: "))
total_marks=m1+m2+m3
print ("student name: ",name)
print ("student roll number: ",roll_no)
print ("Total marks: ",total_marks)
percentage=(total_marks/300)*100
print ("percentage scored: ",percentage)
print ("%.2f" %percentage)

'''
output
Enter the name: Shannon
Enter the roll number: 4nm20bt051
Enter the marks
sub1: 70
sub2: 77
sub3: 88
student name:  Shannon
student roll number:  4nm20bt051
Total marks:  235
percentage scored:  78.33333333333333
78.33
'''