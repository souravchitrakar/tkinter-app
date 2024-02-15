# The top most Menu can be added to either the main window or a widget called Menubutton
# We have to pass the top most Manu to the configure function of either main window or the Manuebutton

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Menu")
window.geometry("800x500")

# Creating a top most Menu
menu = tk.Menu(master = window, tearoff = False)

# We want to attach it to the main window so configuring the window property
window.configure(menu = menu)

file_menu = tk.Menu(master = menu, tearoff = False)
# To add any non Menu item to a Menu we need to use add_command, here clicking the Menu item will kick the command function
file_menu.add_command(label = "New", command = lambda: print("New File"))
# Just to add a separator line
file_menu.add_separator()
file_menu.add_command(label = "Open", command = lambda: print("Open File"))

help_menu = tk.Menu(master = menu, tearoff = False)
help_menu.add_command(label = "Help Entry", command = lambda: print(check_menu_var.get()))
check_menu_var = tk.StringVar()
# The onvalue and offvalue are used to tell what will be the value the Tkinter variable will hole then the Menu item is checked or unchecked
help_menu.add_checkbutton(label= "Check", onvalue = "It is Checked", offvalue = "It is not Checked", variable = check_menu_var)

# To add a Menu (not applicable for the top level one, this is handled using configure) inside another Menu we need to use add_cascade
menu.add_cascade(label = "File", menu = file_menu)
menu.add_cascade(label = "Help", menu = help_menu)


menu_button = ttk.Menubutton(master = window, text = "Menu Button")
menu_button.pack()
button_menu = tk.Menu(master = menu_button, tearoff = False)
menu_button.configure(menu = button_menu)

button_menu.add_command(label = "Entry 1", command = lambda: print("Entry 1"))
button_menu.add_command(label = "Entry 2", command = lambda: print("Entry 2"))

window.mainloop()
