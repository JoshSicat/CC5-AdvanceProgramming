import tkinter as tk

#checking the validity of the password
def check_password():
    password = entry_password.get()

    #creating the criteria of the password
    criteria = [
        lambda p: any(c.islower() for c in p),
        lambda p: any(c.isupper() for c in p),
        lambda p: any(c.isdigit() for c in p),
        lambda p: any(c in "$#@ " for c in p),
        lambda p: 6<= len(p) <=12
    ]

    if all(criterion(password) for criterion in criteria):
        result_label.config(text="Password is valid!")
    else:
        global attempts
        attempts -=1
        if attempts > 0:
            result_label.config(text=f"Invalid password! attempts left: {attempts}")
        else:
            result_label.config(text="Authorities have been alerted!")

#seting up the GUI
root = tk.Tk()
root.title("The password")

#maximum of attempts
attempts = 5

label_password = tk.Label(root, text="Type Password: ")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

button_check = tk.Button(root, text="Check Password", command=check_password)
button_check.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()