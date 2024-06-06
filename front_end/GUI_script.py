import os
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename = "litera")

# here, make sure the working directory is frontend
root.title("Ascot Automated Loss Runs Entry")

# TODO: adapt working directory to general case

# TODO: put icon command in the right place
root.iconbitmap('./images/ascot.ico')
root.geometry('500x350')

# Welcome message
welcome_label = tb.Label(text = "Welcome to the Ascot Automated Loss Runs Entry system!", bootstyle = "primary")
welcome_label.pack(pady=(50, 15))

# instructions
instructions_label = tb.Label(text = "Please right click on the folder that contains submissions you wish to convert, \nselect 'Properties', copy the path under 'Location' and paste it into the box below:", bootstyle = "info")
instructions_label.pack(pady = (10, 10), padx = 30)

# entry_label = tb.Label(text="Enter the path to your submissions folder:", bootstyle="secondary")
# entry_label.pack(pady=(10, 0))

# Entry Widget for file path
file_path_entry = tb.Entry(root, font=("Helvetica", 16), bootstyle="primary")
file_path_entry.pack(pady=10, padx=50)

# Submit button
submit_button = tb.Button(root, text="Submit", bootstyle="success", command=submit_action)
submit_button.pack(pady=20)

root.mainloop()

