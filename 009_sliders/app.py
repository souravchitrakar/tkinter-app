import tkinter as tk
from tkinter import ttk, scrolledtext

# The value is passed by default which is the internal value of the Scale variable
def scale_func(value):
    print(value)
    print(scale_var.get())

window = tk.Tk()
window.title("Sliders")
window.geometry("800x500")

scale_var = tk.IntVar(value = 15)
# On sliding the Scale the command function will be called, a value parameter will be passed to the function
# A Tkinter variable is assigned with variable to track the progress of the Scale programatically, this is different that value which is passed to the function
scale = ttk.Scale(master = window, command = scale_func, from_= 1, to = 25, length = 300, orient = "horizontal", variable = scale_var)
scale.pack()


progress_var = tk.DoubleVar()
progress = ttk.Progressbar(master = window, variable = progress_var, maximum = 50, orient = "horizontal", mode = "determinate", length = 300)
progress.pack()
label = ttk.Label(master = window, textvariable = progress_var)
label.pack()

# We can start and stop the progress bar using the start and stop methods
button_start = ttk.Button(master = window, text = "Start the Progress Bar", command = lambda: progress.start(500))
button_stop = ttk.Button(master = window, text = "Stop the Progress Bar", command = lambda: progress.stop())

button_start.pack()
button_stop.pack()

scrolled_text = scrolledtext.ScrolledText(master = window, width = 100, height = 3)
scrolled_text.pack()

window.mainloop()