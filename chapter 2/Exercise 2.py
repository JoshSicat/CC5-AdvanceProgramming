import tkinter as tk

root = tk.Tk()
root.title("Resizable Labels")
root.geometry("400x300")

#text with label
label1 = tk.Label(root, text="Label 1", bg="red", width=20)
label2 = tk.Label(root, text="Label 2", bg="blue", width=20)
label3 = tk.Label(root, text="Label 3", bg="green", width=20)
label4 = tk.Label(root, text="Label 4", bg="yellow", width=20)

#pack to place label
label1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
label2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
label3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
label3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()