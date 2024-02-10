# The widget input output should be handled using Tkinter variables

import tkinter as tk
from tkinter import ttk

def func_button():

    # Prints all the available properties of the widget
    print(entry.configure())

    # Getting the text from the entry widget
    entered_text = entry.get()

    # Setting the text property of the Label widget
    # This is another way: label.configure(text = entered_text)
    label["text"] = entered_text

window = tk.Tk()
window.title("Widget Input Output")
window.geometry("800x500")

ttk.Label(master = window, text = "Text will change dynamically").pack()

label = ttk.Label(master = window)
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = "The button", command = func_button)
button.pack()

window.mainloop()