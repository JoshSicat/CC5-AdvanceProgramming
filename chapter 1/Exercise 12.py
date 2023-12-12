import math 

#funtion to calculate the area of square 
def calculate_square_area():
    side_length = float(input("enter the length of a  side of the square: "))
    area = side_length ** 2
    print(f"the area of the square is: {area}")

#funtion to calculate the area of circle
def calculate_circle_area():
    radius = float(input("enter the radius of a circle: "))
    area = math.pi * (radius ** 2)
    print(f"the area of the circle is: {area}")

#funtion to calculate the area of triangle
def calculate_triangle_area():
    base = float(input("enter the length of the side of the triangle: "))
    height = float(input("enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"the area of the triangle is: {area}")

#menu options
while True:
    print("\nMune")
    print("1: calculate the area of  a square")
    print("2: calculate the area of  a circle")
    print("3: calculate the area of  a triangle")
    print("4: Stop")

    choice = input("choose a number to (1-4): ")

    if choice == 'i':
        calculate_square_area()
    elif choice =='2':
        calculate_circle_area()
    elif choice =='3':
        calculate_triangle_area()
    elif choice =='4':
        print("exiting the program. bye bleh :D")
        break
    else:
        print("invalid choice. please enter a number between 1 to 4.")