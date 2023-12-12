import tkinter as tk
from tkinter import ttk

class Arthmeticoperations:
    def __init__(self): 
        self.result = 0

    #creating a calculatetur
    def calculate(self, operation, num1, num2):
        if operation == "addition":
            self.result = num1 + num2
        elif operation == "subraction":
            self.result = num1 - num2
        elif operation == "multiplication":
            self.result = num1 * num2
        elif operation == "division":
            if num2 != 0:
                self.result = num1 / num2
            else:
                self.result = "cant divide by 0"

# triggering the button to click and perform the caculation
def perform_caculation():
    selected_operation = operations_choice.get()
    value1 = float(entry_num1.get())
    value2 = float(entry_num2.get())

    arithmetic = Arthmeticoperations()
    arithmetic.calculate(selected_operation, value1, value2)

    result_label.config(text=f"Result: {arithmetic.result}")

#creating the window
root = tk.Tk()
root.title("arithmetic operation")

#creating the lavel and entry for the numbers inputs
label_num1 = tk.Label(root, text="enter number 1: ")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="enter number 2: ")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

#command bos to select arithmetic operation
label_operation = tk.Label(root, text="select operatopm: ")
label_operation.pack()

operations = ["Additon", "Subraction", " Multiplication", "Division"]
operations_choice = ttk.Combobox(root, values=operations    )
operations_choice.pack()

#making the button to perform the calculation
button_calculate = tk.Button(root, text="calcukate", command=perform_caculation)
button_calculate.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()