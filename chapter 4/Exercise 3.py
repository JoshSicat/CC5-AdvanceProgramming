import tkinter as tk

#to count occurrences of a characters in the file
def count_character():
    try:
        char_to_count = entry_char.get()
        with open ('sentences.txt', 'r') as file:
            content = file.read()
            count = content.count(char_to_count)

            #displaying the count in the label
            result_label.config(text=f"Occurrences of '{char_to_count}': {count}")
    except FileNotFoundError:
        result_label.config(text="File 'sentences.txt' not found.")

#seting up the GUI
root = tk.Tk()
root.title("counter")

label_char = tk.Label(root, text="Enter a character")
label_char.pack()

entry_char = tk.Entry(root)
entry_char.pack()

button_count = tk.Button(root, text="count Occurrences", command=count_character)
button_count.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()