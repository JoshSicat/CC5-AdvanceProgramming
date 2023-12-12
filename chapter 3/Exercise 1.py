import tkinter as tk

def update_greeting():
    name = entry_name.get()
    selected_color = colors[color_var.get()]
    greeting = f"KaMusta!, {name}!"
    lbl_display.config(text=greeting, fg=selected_color)

root = tk. Tk()
root.title("greetings")

#creating colore of choice
colors = {
    0: "black",
    1: "red",
    2: "blue",
    3: "orange",
    4: "green",
    5: "brown"
}

#inpuning frame
input_frame = tk.Frame(root, bg="lightblue", padx=20, pady=20)
input_frame.pack(fill=tk.BOTH, expand=True)

#title of the input frame
lbl_title = tk.Label(input_frame, text="Personal greetings", fg="black")
lbl_title.grid(row=0, column=0,  columnspan=2, padx=10, pady=10)

#entry user's name in input frame
entry_name = tk.Entry(input_frame)
entry_name.grid(row=1, column=0, padx=10, pady=5)

#dropdown menu of selectig colors
color_var = tk.IntVar()
color_var.set(0)
dropdown_color = tk.OptionMenu(input_frame, color_var, *colors.keys())
dropdown_color.grid(row=1, column=1, padx=10, pady=5)

#updating the greeting button

btn_update = tk.Button(input_frame, text="Update greeting", command=update_greeting)
btn_update.grid(row=2, column=0,  columnspan=2, padx=10, pady=10)

#display the frame
display_frame = tk.Frame(root, bg="lightyellow", padx=20, pady=20)
display_frame.pack(fill=tk.BOTH, expand=True)

# the label will display a personal greetings
lbl_display = tk.Label(display_frame, text="", font=("Atial", 12))
lbl_display.pack(padx=10, pady=10)

root.mainloop()