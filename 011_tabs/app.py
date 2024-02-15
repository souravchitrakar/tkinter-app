import tkinter as tk
from tkinter import ttk, scrolledtext

window = tk.Tk()
window.title("Tabs")
window.geometry("800x500")

# The Notebook is used to create tabs
notebook = ttk.Notebook(master = window)
notebook.pack()

tab_one = ttk.Frame(master = notebook)
tab_two = ttk.Frame(master = notebook)

# Add frames to the Notebook to create the required tabs
notebook.add(tab_one, text = "Text One")
notebook.add(tab_two, text = "Text Two")

label_one = ttk.Label(master = tab_one, text = "In Tab One")
label_one.pack()
label_two = ttk.Label(master = tab_two, text = "In Tab Two")
label_two.pack()


window.mainloop()