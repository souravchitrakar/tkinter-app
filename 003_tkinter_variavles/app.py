import tkinter as tk
from tkinter import ttk

def button_func():
    
    # Getting the value of the Tkinter variable
    print(string_var.get())

    # Setting the value of the Tkinter variable
    string_var.set("Reset")


window = tk.Tk()
window.title("Tkinter Variables")
window.geometry("800x500")

# Creating a Tkinter string variable
# Passing the value is optional
string_var = tk.StringVar(value = "Start value")

# The textvariable is an important property of the widget where we can set Tkinter variables directly
label = ttk.Label(master = window, textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = "Button", command = button_func)
button.pack()

window.mainloop()