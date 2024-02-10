import tkinter as tk

# The inbox widgets are created using the following import but we will use ttkbootstrap
# from tkinter import ttk

import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# Creating the main window in conventional way but we will use ttkbootstrap
# window = tk.Tk()
    
window = ttk.Window(themename = "darkly")

# Setting basic window properties
window.title("Demo")
window.geometry("600x300")

# Creating a label by defining the master (container) is the window and the other properties
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font = "Calibri 24 bold")
# Attaching the label to the window
title_label.pack()

input_frame = ttk.Frame(master = window)

# Creating a Tkinter variable
entry_int = tk.IntVar()

# Values of the field will be set using textvariable and Tkinter variable
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

# The function passed to the command is the on click function
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

output_string = tk.StringVar()
output_label = ttk.Label(master = window, textvariable = output_string, font = "Calibri 24")
output_label.pack(pady = 10)

# Running the window
window.mainloop()