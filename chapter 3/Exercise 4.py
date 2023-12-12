import tkinter as tk

def draw_shape():
    canvas.delete("all")

    if  shape_var.get() == 1:
        canvas.creat.oval(50, 50, 200, 150, outline="black", width=2)
    elif shape_var() == 2:
        canvas.creat.rectangle(50, 50, 200, 150, outline="black", width=2)
    elif shape_var() == 3:
        canvas.creat.rectangle(50, 50, 200, 150, outline="black", width=2)
    elif shape_var() == 4:
        canvas.creat.ploygon(50, 150, 125, 50, 200, 150, outline="black", width=2)

#creating a window
root = tk.Tk()
root.title("drawing od the shapre")

#creating a frame to hold the buttons
frame = tk.Frame(root)
frame.pack(pady=20)

#varriable to store  the selected shape
shape_var = tk.IntVar()

#button for selected shape
shapes = [("Oval", 1), ("Rectangle", 2), ("square", 3), ("Triangle", 4)]
for shape, val in shapes:
    tk.Radiobutton(frame, text="shape", variable=shape_var, value=val).pack(side=tk.LEFT, padx=10)

#button to draw the shapes
draw_button = tk.Button(root, text="Draw a shape", command=draw_shape)
draw_button.pack(pady=20)

#creating a canva boread to draw
canvas = tk.Canvas(root, width=250, height=200, bg="white")
canvas.pack()

root.mainloop()