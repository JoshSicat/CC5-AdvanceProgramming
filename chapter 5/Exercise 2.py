import tkinter as tk

#making the mark of the students
class students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calc_grade(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3
    
    def display(self):
        avarage = self.calc_grade()
        return f"Student Name: {self.name}\n Average grade: {avarage:.2f}"
    
def create_students():
    #data of the student 1
    name = entry_name.get()
    mark1 = int(entry_mark1.get())
    mark2 = int(entry_mark2.get())
    mark3 = int(entry_mark3.get())

    student1 = students(name, mark1,mark2, mark3)
    label_student1.config(text=student1.display())

    #retrieve data  for student2
    name = entry_name2.get()
    mark1 = int(entry_mark1_2.get())
    mark2 = int(entry_mark2_2.get())
    mark3 = int(entry_mark3_2.get())

    #create student 2objects
    student2 = students(name, mark1,mark2, mark3)
    label_student2.config(text=student2.display())

#creating GUI
root = tk.Tk()
root.title("students")

#student 1 widgets
Label_name = tk.Label(root, text="Enter Name: ")
Label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

Label_mark1 = tk.Label(root, text="Enter Mark 1: ")
Label_mark1.pack()

entry_mark1 = tk.Entry(root)
entry_mark1.pack()

label_mark2 = tk.Label(root, text="Enter Mark 2")
label_mark2.pack()

entry_mark2 = tk.Entry(root)
entry_mark2.pack()

label_mark3 = tk.Label(root, text="Enter Mark 3")
label_mark3.pack()

entry_mark3 = tk.Entry(root)
entry_mark3.pack()

button_create = tk.Button(root, text="Create students", command=create_students)
button_create.pack()

label_student1 = tk.Label(root, text="")
label_student1.pack

#student 2 widgets
Label_name2 = tk.Label(root, text="Enter Name: ")
Label_name2.pack()

entry_name2 = tk.Entry(root)
entry_name2.pack()

Label_mark1_2 = tk.Label(root, text="Enter Mark 1: ")
Label_mark1_2.pack()

entry_mark1_2 = tk.Entry(root)
entry_mark1_2.pack()

label_mark2_2 = tk.Label(root, text="Enter Mark 2")
label_mark2_2.pack()

entry_mark2_2 = tk.Entry(root)
entry_mark2_2.pack()

label_mark3_2 = tk.Label(root, text="Enter Mark 3")
label_mark3_2.pack()

entry_mark3_2 = tk.Entry(root)
entry_mark3_2.pack()

button_create2 = tk.Button(root, text="Create students", command=create_students)
button_create2.pack()

label_student2 = tk.Label(root, text="")
label_student2.pack

root.mainloop()