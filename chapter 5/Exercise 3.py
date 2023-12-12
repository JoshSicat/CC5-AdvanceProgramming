import tkinter as tk

#creating a employee in class
class employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.id = 0
        self.salary = 0.0

    def set_data(self, name, age, emp_id, salary):
        self.name = name
        self.age = age
        self.id = emp_id
        self.salary = salary

#geting the user input for the employee details 
def add_employee():
    name = entry_name.get()
    age = int(entry_age.get())
    emp_id = int(entry_id.get())
    salary = float(entry_salary.get())

    #creating a employee data set
    emp = employee()
    emp.set_data(name, age, emp_id, salary)
    employees.append(emp)

#adding header  for employee details
def display_employees():
    print("Name\t\tAge\t\tSalary\tID")
    for emp in employees:
        print(emp.get_data())

#creating the window
root = tk.Tk()
root.title("Employees")

#list to hold the employees
employees = []

#label and entry for employee details

label_name = tk.Label(root, text="Type your name: ")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="Type your age: ")
label_age.pack()

entry_age = tk.Entry(root)
entry_age.pack()

label_id = tk.Label(root, text="Type your ID: ")
label_id.pack()

entry_id = tk.Entry(root)
entry_id.pack()

label_salary = tk.Label(root, text="Type your salary: ")
label_salary.pack()

entry_salary = tk.Entry(root)
entry_salary.pack()

#creaing the button
button_add = tk.Button(root, text="add employee", command=add_employee)
button_add.pack()

button_display = tk.Button(root, text="display employee", command=display_employees)
button_display.pack()

root.mainloop()