import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f"x: {event.x} y: {event.y}")

window = tk.Tk()
window.title("Event Binding")
window.geometry("800x500")

text = tk.Text(master = window)
text.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = "A Button")
button.pack()

# Events can be attached to any widget including the window using bind method
# The bind  method accept the event as a string (for example <Alt-KeyPress-a>, <KeyPress>) and a function (with a parameter event)
button.bind("<Alt-KeyPress-a>", lambda event: print("An Event"))
window.bind("<KeyPress>", lambda event: print(f"Key pressed: {event.char}"))
window.bind("<Motion>", get_pos)

entry.bind("<FocusIn>", lambda event: print("Entry field selected"))
entry.bind("<FocusOut>", lambda event: print("Entry field unselected"))

window.mainloop()