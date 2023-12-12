import tkinter as tk
from tkinter import messagebox

#function to  the display of selection of the message box
def display_order():
    coffee = coffee_var.get()
    sugar = sugar_var.get()
    milk = milk_var.get()

#display of messages
message = ("You have selected: Coffee: {Latte}\nSugar: {small_sugar}\nMilk: {low_milk}")
#the display message using the message box
messagebox.showinfo("Oder summary", message)

root = tk.Tk()
root.title("Coffee vender")

#the coffee option
coffee_var = tk.StringVar()
coffee_var.set("Espresso")
lbl_coffee = tk.Label(root, text="pleas scelect a Coffee: ")
lbl_coffee.pack()
dropdown_coffee = tk.OptionMenu(root, coffee_var, "Espresso", "latte", "Cappiccino")
dropdown_coffee.pack()

#Option of Sugar and Milk
sugar_var = tk.BooleanVar()
chk_sugar = tk.Checkbutton(root, text="Add sugar", variable=sugar_var)
chk_sugar.pack()

milk_var = tk.BooleanVar()
chk_milk = tk.Checkbutton(root, text="Add milk", variable=milk_var)
chk_milk.pack()

#button to select option
btn_order = tk.Button(root, text="Please oder here", command=display_order)
btn_order.pack()

root.mainloop()