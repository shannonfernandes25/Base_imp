#Menu driven program to create a simple calculator

def addition(a,b):
    sum = a+b
    print(a, "+", b, "=", sum)
    
def difference(a,b):
    sub = a-b
    print(a, "-", b, "=", sub)
    
def multiplication(a,b):
    multi = a*b
    print(a, "X", b, "=", multi)
    
def division(a,b):
    div = a/b
    print(a, "/", b, "=", div)
    
print("Welcome to a simple calculator")

while True:
    print("\n Menu")
    print("1. Addition of two numbers")
    print("2. Subtraction of two numbers")
    print("3. Multiplication of two numbers")
    print("4. Division of two numbers")
    print("5. Exit")
    
    choice = int(input("\n Enter the choice number: "))
    
    if choice == 1:
        print("\n ADDITION")
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        addition(a,b)
        
    elif choice == 2:
        print("\n SUBTRACTION")
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        difference(a,b)
        
    elif choice == 3:
        print("\n MULTIPLICATION")
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        multiplication(a,b)
        
    elif choice == 4:
        print("\n DIVISION")
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        division(a,b)
        
    elif choice == 5:
        break
    
    else:
        print("Please enter a valid input")
    
    
'''
output
Welcome to a simple calculator

 Menu
1. Addition of two numbers
2. Subtraction of two numbers
3. Multiplication of two numbers
4. Division of two numbers
5. Exit

 Enter the choice number: 8
Please enter a valid input

 Menu
1. Addition of two numbers
2. Subtraction of two numbers
3. Multiplication of two numbers
4. Division of two numbers
5. Exit

 Enter the choice number: 1

 ADDITION
Enter the first number: 30
Enter the second number: 15
30 + 15 = 45

 Menu
1. Addition of two numbers
2. Subtraction of two numbers
3. Multiplication of two numbers
4. Division of two numbers
5. Exit

 Enter the choice number: 2

 SUBTRACTION
Enter the first number: 45
Enter the second number: 20
45 - 20 = 25

 Menu
1. Addition of two numbers
2. Subtraction of two numbers
3. Multiplication of two numbers
4. Division of two numbers
5. Exit

 Enter the choice number: 3

 MULTIPLICATION
Enter the first number: 6
Enter the second number: 4
6 X 4 = 24

 Menu
1. Addition of two numbers
2. Subtraction of two numbers
3. Multiplication of two numbers
4. Division of two numbers
5. Exit

 Enter the choice number: 4

 DIVISION
Enter the first number: 116
Enter the second number: 2
116 / 2 = 58.0

 Menu
1. Addition of two numbers
2. Subtraction of two numbers
3. Multiplication of two numbers
4. Division of two numbers
5. Exit

 Enter the choice number: 5

=== Code Execution Successful ===
'''
    