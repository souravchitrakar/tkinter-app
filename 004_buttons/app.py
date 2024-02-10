import tkinter as tk
from tkinter import ttk

click = 3

def button_func():
    print("A simple button")
    # The get method is used to get the value of the Tkinter variable
    print(button_var.get())
    global click
    click = click + 1
    button_var.set(f"A button with string var: Click no - {click}")

def check_func():
    print("A simple check")

def radio_func():
    print("A simple radio")

window = tk.Tk()
window.title("Buttons")
window.geometry("800x500")

# Defining a Tkinter string variable
button_var = tk.StringVar(value = "A button with string var: Click no 0")

# Assigning the Tkinter variable to textvariable, changing the value og the Tkinter variable will update the button text
button = ttk.Button(master = window, textvariable = button_var, command = button_func)
button.pack()


# The checkbox does not have textvariable rather have variable, we assign the Tkinter variable to the variable
# We need to define two properties onvalue and offvalue, when the checkbox is selected the onvalue will be set to Tkinter variable or the versa
# As the initial value of the Tkinter variable is 10 which is matching onvalue so the checkbox will be checked initially
# It is recomended to use Boolean Tkinter variable with checkbox
# When we check or uncheck the checkbox the function assigned to the command will be executed
check_var = tk.IntVar(value = 10)
check = ttk.Checkbutton(master = window, text = "Checkbox 1", command = check_func, variable = check_var, onvalue = 10, offvalue = 5)
check.pack()

# The checkbox does not have textvariable rather have variable, we assign the Tkinter variable to the variable
# A common Tkinter variable will be assigned to all the radio buttons of the same group of radio buttons
# When we check the radio button the function assigned to the command will be executed
# The value of each and every radio button should be unique
# When a radio button is checked the value of the radio button will be assigned to the Tkinter variable
# As the innitial value of the radio button is 0 which is not matching any radion button's value so no one will be checked
radio_var = tk.IntVar(value = 0)
radoi_1 = ttk.Radiobutton(master = window, text = "Radio 1", command = radio_func, variable = radio_var, value = 1)
radoi_1.pack()
radoi_2 = ttk.Radiobutton(master = window, text = "Radio 1", command = radio_func, variable = radio_var, value = 2)
radoi_2.pack()

window.mainloop()

