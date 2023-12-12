import tkinter as tk

#creating a dog's name age and breed
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def woof(self):
        return f"{self.name} say: Woof woof!"

#creating the instances of the dog
dog1 = Dog("Browny", 6, "Labrador")
dog2 = Dog("mariah", 9, "German shepherd")

#cearing the GUI
root = tk.Tk()
root.title("dog name")

#Displaying the dogs information
label_dog1 = tk.Label(root, text=f"Dog 1:{dog1.name}, {dog1.age} years old, breed: {dog1.breed}")
label_dog1.pack()

label_dog2 = tk.Label(root, text=f"Dog 2:{dog2.name}, {dog2.age} years old, breed: {dog2.breed}")
label_dog2.pack()

#fuction to make the oldest dog to woof
def make_oldest_woof():
    oldest_dog = max(dog1, dog2, key=lambda dog: dog.age)
    result_label.config(text=oldest_dog.woof())

button_woof = tk.Button(root, text="make oldest dog woof", command=make_oldest_woof)
button_woof.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()