import tkinter as tk 

def change_font():
    label.config(font=("Arial", 12, "bold italic"))

root = tk.Tk()
root.title("Welcome GUI")
#window size
root.geometry("400x300")
root.resizable(False, False)
#background color
root.configure(background='lightblue')

welcome_text = "Welcome the GUI!"
label = tk.Label(root, text=welcome_text, font=("Helvetica", 14), bg="lightblue")
label.pack(pady=20)

font_button = tk.Button(root, text="Change Font", command=change_font)
font_button.pack()

root.mainloop()