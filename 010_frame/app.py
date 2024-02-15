import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("800x500")
window.title("Frame")

# The Frame is the container inside the main window, by default Frames do not have width and height
frame = ttk.Frame(master = window, width = 300, height = 200, borderwidth = 10, relief = tk.GROOVE)
# By default Frames contain the size of the inner widgets even if we are mentioning the width and height
# If we are setting the pack_propagate to false then the Frame will maintain that provided height and width
frame.pack_propagate(False)
frame.pack()

label = ttk.Label(master = frame, text = "Lable in Frame")
label.pack()

window.mainloop()