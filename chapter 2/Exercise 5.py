import tkinter as tk

def perform_operation():
    try:
        #input the values from entrying the fields andconvert the float
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        #selection from the dropdown mune
        operation = operations_var.get()
        result = None

        #the selection
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result =num1 - num2
        elif operation == "Multiplication":
            result =num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "cant divide by zero"

        elif operation == "modulo":
            if num2 != 0:
                result = num1 % num2
            else:
                result = "cant modulo by zero"

        
        #displaying the result 
        lbl_result.config(text=f"Result: {result}", fg="black")
    except ValueError:
        lbl_result.config(text="please enter a number", fg="red")

#creating the main window
root = tk.Tk()
root.title("calculate")

#entry fields for numbers
lbl_num1 = tk.Label(root, text="Type a number of your choice: ")
lbl_num1.grid(row=0,column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0,column=1, padx=10, pady=5)

lbl_num2 = tk.Label(root, text="Type a number of your choice:")
lbl_num2.grid(row=1,column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1,column=1, padx=10, pady=5)

#operation usingthe dropdown menu
operations = ["Addition", "Subtraction", "Multiplcation", "Division", "Modulo"]
operations_var = tk.StringVar(root)
operations_var.set(operations[0])

lbl_operation = tk.Label(root, text="Select a operation:")
lbl_operation.grid(row=2,column=0, padx=10, pady=5)
dropdown_operation = tk.OptionMenu(root, operations_var, *operations)
dropdown_operation.grid(row=2, column=1, padx=10, pady=10)

#calculate button
btn_calc =  tk.Button(root, text="calculate", command=perform_operation)
btn_calc.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

#display of the result
lbl_result = tk.Label(root, text="", fg="black")
lbl_result.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()