import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Combobox and Spinbox")
window.geometry("800x500")

# Define a list and assign to the values of the combobox
items = ("Ice Cream", "Pizza", "broccoli")

# This Tkinter variable will hold the current selected value
food_string = tk.StringVar(value = items[0])

combo = ttk.Combobox(master = window, textvariable = food_string)
# Assigning the values of the combobox
# combo["values"] = items
combo.configure(values = items)
combo.pack()

# This event will be fired on change of the combobox selection
combo.bind("<<ComboboxSelected>>", lambda event: entry.configure(textvariable=food_string))

entry = ttk.Entry(master = window, textvariable = food_string)
entry.pack()

button = ttk.Button(master = window, text = "A Button", command = lambda: print(food_string.get()))
button.pack()



# Values are defined as the values of the listbox
values = (1, 2, 3, 4, 5)

# This Tkinter variable will hold the current value of the spinbox
int_var = tk.IntVar(value = values[0])

# The command function will be fired when increment or decrement is taking place
spin = ttk.Spinbox(master = window, values = values, textvariable = int_var, command = lambda: print("Increment or Decrement is pressed"))

# Two events are getting bind specifically when increment or decrement is taking place
spin.bind("<<Increment>>", lambda event: print("Increment is pressed"))
spin.bind("<<Decrement>>", lambda event: print("Decrement is pressed"))
spin.pack()

window.mainloop()