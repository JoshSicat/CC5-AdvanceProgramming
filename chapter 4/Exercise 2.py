import tkinter as tk

#count occurrences of specific strings in the fie
def count_strings():
    try:
        with open('sentences.txt', 'r') as file:
            content = file.readlines()
            strings_to_search = [
                "Hello my is Peter parker",
                "I love python programming",
                "Love",
                "Enemy"
            ]
            count = {string: 0 for string in strings_to_search}

            #loop through each line in the file and count 
            for line in content:
                for string in strings_to_search:
                    count[string] += line.count(string)

            #displaying result in the text box 
            text_output.delete(1.0, tk.END)
            for string, count in count.items():
                text_output.insert(tk.END, f"{string}: {count} occurrences\n")
    except FileNotFoundError:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "File 'sentences.txt' not found.")

#setuping the GUI
root = tk.Tk()
root.title("string counter")

#button to trigger counting  string occurrences
button_count = tk.Button(root, text="Count Occurrences", command=count_strings)
button_count.pack()

#text box to display the result 
text_output = tk.Text(root, height=8, width=40)
text_output.pack()

root.mainloop()