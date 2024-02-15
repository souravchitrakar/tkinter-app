import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Treeview")
window.geometry("800x500")

# Here the tuple passed to the columns are mentioning the names of the columns but not the column headings
# The show is saying that we want the heading to be shown
table = ttk.Treeview(master = window, columns = ("first", "last"), show = "headings")

# Here we are defining the column headings (order does not matters)
table.heading("last", text = "Last Name")
table.heading("first", text = "First Name")

table.pack()

# Inserting values to the table, here parent = "" is saying insert in to the table
# The index 0 is inserting at the top of the table, numbers can be assigned
table.insert(parent = "", index = 0, values = ("Debjani", "Basu"))
table.insert(parent = "", index = 0, values = ("Debangi", "Basu Chitrakar"))
# Here tk.END means insert at the end
table.insert(parent = "", index = tk.END, values = ("Sourav", "Chitrakar"))

window.mainloop()