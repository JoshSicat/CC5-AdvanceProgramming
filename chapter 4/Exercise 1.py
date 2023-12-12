import tkinter as tk

#writing user input to a file 
def write_to_file():
    name = entry_name.get()
    age = entry_age.get()
    hometown = entry_hometwon.get()

    #user data to a file named bio.txt 
    with open('bio.txt', 'w') as file:
        file.write(f"Name: {name}\nAge: {age}\nHometwon: {hometown}")

#read file content and display in the text box
def read_from_file():
    try:
        with open('bio.txt', 'r') as file:
            content = file.read()
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, content)
    except FileNotFoundError:
        #display a message in the text box
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "File ' bio.txt' not found.")

#setting up the GUI
root = tk.Tk()
root.title("Bio")

#The labels and Widgets for user input
label_name = tk.Label(root,text="Name: ")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="Age: ")
label_age.pack()
entry_age = tk.Entry(root)
entry_age.pack()

label_hometown = tk.Label(root, text="Hometown: ")
label_hometown.pack()
entry_hometwon = tk.Entry(root)
entry_hometwon.pack()

#making the button to write the file and reading from file
button_write = tk.Button(root, text="Write to file", command=write_to_file)
button_write.pack()

button_read = tk.Button(root, text="Read from file", command=read_from_file)
button_read.pack()

text_output = tk.Text(root, height=8, width=40)
text_output.pack()

root.mainloop()