import tkinter as tk
from tkinter import ttk

def outer_func(param):
    def inner_func():
        print(param.get())

    return inner_func

window = tk.Tk()
window.title("Button With Function Parameter")
window.geometry("800x500")

entry_var = tk.StringVar(value = "Provide Value")
entry = ttk.Entry(master = window, textvariable = entry_var)
entry.pack()

# If we want to execute a finction with parameters then we need to define outer and inner function
# The inner function should not have any parameter, the inner function will have access to all the outer parameters by default scope
# return the inner function from the outer function
button = ttk.Button(master = window, text = "Button", command = outer_func(entry_var))
button.pack()

window.mainloop()