import tkinter as tk


def login():
    #username and passowrd from fields
    username = entry_username.get()
    password = entry_password.get()

    #you can implement your own verification
    if username == "joshSicat" and password == "how are you":
        lbl_result.config(text="login conform!", fg="green")
    else:
        lbl_result.config(text="wrong username or password", fg="red")

#creating main window
root = tk.Tk()
root.title("my page")

#label of the username and entry field
lbl_username = tk.Label(root, text="username: ")
lbl_username.grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

#label of the password and entry field
lbl_password = tk.Label(root, text="Password: ")
lbl_password.grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="***")
entry_password.grid(row=1, column=1, padx=10, pady=5)

#login button
btn_login = tk.Button(root, text="Login", command=login)
btn_login.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#showing the result
lbl_result = tk.Label(root, text="", fg="black")
lbl_result.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()