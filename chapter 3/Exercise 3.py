import tkinter as tk
from math import pi

#calculating the area of circle
def calculate_circle_area():
    radius = float(entry_radius.get())
    area = pi * (radius ** 2)
    label_circle_result.config(text=f"The Area fo the circle: {area: 2f}")

#calculating the area of rectangle
def calculate_rectanle_area():
    length = float(entry_length.get())
    width = float(entry_width.get())
    area = length * width 
    label_rectangle_result.congif(text=f"The Area of the rectanle: {area: 2f}")

#calculating the area of circle
def calculate_sqaure_area():
    side = float(entry_side.get())
    area = side ** 2
    label_square_result.congif(text=f"The Area of the square: {area: 2f}")

#crating the main window
root = tk.Tk()
root.title("calculating the shape")

#creating a notebook
notebook = tk.ttk.Notebook(root)

#creating the tab for the shapes
tab_circle = tk.Frame(notebook)
tab_rectangle = tk.Frame(notebook)
tab_square = tk.Frame(notebook)

notebook.add(tab_circle, text='circle')
notebook.add(tab_rectangle, text='rectangle')
notebook.add(tab_square, text='square')

#widgets for circle tab
label_radius = tk.Label(tab_circle, text="Type the Radius: ")
label_radius.pack()
entry_radius = tk.Entry(tab_circle)
entry_radius.pack()
btn_calculate_circle = tk.Button(tab_circle, text="calculate", command=calculate_circle_area)
btn_calculate_circle.pack()
label_circle_result = tk.Label(tab_circle, text="")
label_circle_result.pack()

#widgeta for the rectangle
label_length = tk.Label(tab_rectangle, text="Type the length: ")
label_length.pack()
entry_length = tk.Entry(tab_rectangle)
entry_length.pack()
length_width = tk.label(tab_rectangle, text="Type the width: ")
length_width.pack()
entry_width = tk.Entry(tab_rectangle)
entry_width.pack()
btn_calculate_rectangle = tk.Button(tab_rectangle, text="caculate", command=calculate_rectanle_area)
btn_calculate_rectangle.pack()
label_rectangle_result = tk.Label(tab_rectangle, text="")
label_rectangle_result.pack()

#widgets for the square
label_side = tk.Label(tab_square, text="Type the side length: ")
label_side.pack()
entry_side = tk.Entry(tab_square)
entry_side.pack()
btn_calculate_square = tk.Button(tab_square, text="calculate", command=calculate_sqaure_area)
btn_calculate_square.pack()
label_square_result = tk.label(tab_square, text="")
label_square_result.pack()
notebook.pack()

root.mainloop()