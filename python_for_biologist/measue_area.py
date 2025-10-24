#Calculate the Area of different Shapes using functions

def c_circle(radius):
    area = (3.14 * radius * radius)
    print("Area of circle: ", area)

def r_rectangle(height, width):
    area = (height * width)
    print("Area of rectangle: ", area)

def s_square(side):
    area = (side * side)
    print("Area of square: ", area)

print("Simple measurement program")

while True:
    print("\nMain menu")
    print("1. Calculate the area of Circle")
    print("2. Calculate the area of the Rectangle")
    print("3. Calculate the area of the Square")
    print("4. Exit")

    choice1 = int(input("Enter the choice: "))

    if choice1 == 1:
        radius = int(input("Enter the radius: "))
        c_circle(radius)

    elif choice1 == 2:
        height = int(input("Enter the height: "))
        width = int(input("Enter the width: "))
        r_rectangle(height, width)

    elif choice1 == 3:
        side = int(input("Enter the side: "))
        s_square(side)

    elif choice1 == 4:
        break

    else:
        print("Incorrect choice")
        
        
'''
output
Simple measurement program

Main menu
1. Calculate the area of Circle
2. Calculate the area of the Rectangle
3. Calculate the area of the Square
4. Exit
Enter the choice: 1
Enter the radius: 3
Area of circle:  28.259999999999998

Main menu
1. Calculate the area of Circle
2. Calculate the area of the Rectangle
3. Calculate the area of the Square
4. Exit
Enter the choice: 2
Enter the height: 4
Enter the width: 6
Area of rectangle:  24

Main menu
1. Calculate the area of Circle
2. Calculate the area of the Rectangle
3. Calculate the area of the Square
4. Exit
Enter the choice: 3
Enter the side: 4
Area of square:  16

Main menu
1. Calculate the area of Circle
2. Calculate the area of the Rectangle
3. Calculate the area of the Square
4. Exit
Enter the choice: 4

=== Code Execution Successful ===
'''