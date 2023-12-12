import tkinter as tk

root = tk.Tk()

# frames to contain the labels/ left frame
left_frame = tk.Frame(root, borderwidth=5, relief=tk.SOLID)
left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

#right frame
right_frame = tk.Frame(root, borderwidth=5, relief=tk.SOLID)
right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

#labels A to D and place them to their frames
label_a = tk.Label(left_frame, text="A", bg="lightblue")
label_a.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

label_b = tk.Label(left_frame, text="B", bg="lightblue")
label_b.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

label_c = tk.Label(right_frame, text="C", bg="lightblue")
label_c.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

label_d = tk.Label(right_frame, text="D", bg="lightblue")
label_d.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

root.mainloop