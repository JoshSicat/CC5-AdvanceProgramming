import tkinter as tk
from math import pi

#class shape with methods to input  sides and calculate areas
class shape:
    def __init__(self):
        self.sides = []

    #methods input to sides base on the shape
    def input_sides(self, side_count):
        for i in range(side_count):
            side = float(input(f"Enter side {i + 1}: "))
            self.sides.append(side)

    #holding the place method to calculate the area
    def area(self):
        pass

#subclass circle inheriting from shape and  calculating thearea of circle
class circle(shape):
    def area(self):
        radius = self.sides[0]
        return pi * radius * radius
    
#subclass triangle inheriting from shape and  calculating thearea of triangle
class triangle(shape):
    def area(self):
        side1, side2, side3 = self.sides
        s = (side1, side2, side3) / 2
        return (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    
#subclass rectangle inheriting from shape and  calculating thearea of rectangle
class rectangle(shape):
    def area(self):
        length = self.sides[0]
        width = self.sides[1]
        return length * width
#tringgered by button click to calculate the area based on the  shape
def calculate_area():
    shape_type = shape_choice.get()

    if shape_type == "circle":
        circle = circle()
        circle.input_sides(1)
        area = circle.area()
    elif shape_type == "Triangle":
        triangle = triangle()
        triangle.input_sides(2)
        area = triangle.area()
    elif shape_type == "Rectangle":
        rectangle = rectangle()
        rectangle.input_sides(3)
        area = rectangle.area

    result_label.config(text=f"Area = {area: .2f}")

#creating window
root = tk.Tk()
root.title("Area and shapes")

#creating a dropdown menu
shape_choice = tk.StringVar(root)
shape_choice.set("Circle")

label_shape = tk.Label(root, text="select shape: ")
label_shape.pack()

shape_menu = tk.OptionMenu(root, shape_choice, "Circle", "Triangle", "Rectangle")
shape_menu.pack()

#making the button trigger 
button_calculate = tk.Button(root, text="calculate area", command=calculate_area)
button_calculate.pack()

#label to display calculated area
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()