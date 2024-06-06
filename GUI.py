import os
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *


def process_path(path):
    # Placeholder function to represent processing the path
    print(f"Processing files at: {path}")
    # Here, add code to work with files at the given path

    # Naviagate to the input folder

    # Identify all pdf files 

    # use script to populate loss runs one by one

def load_new_content(path):
    # Here, you could process the path or display new widgets
    new_label = tb.Label(main_frame, text=f"Path submitted: {path}", bootstyle="success")
    new_label.pack(pady=20)
    # Additional widgets can be added here as needed

# Initialize the main window
root = tb.Window(themename="superhero")
root.title("Dynamic Content Update")
root.geometry('500x300')

# Initial frame to hold the UI elements
main_frame = tb.Frame(root)
main_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Label for instruction
label = tb.Label(main_frame, text="Enter the path to your submissions folder:", bootstyle="info")
label.pack(pady=(20, 10))

# Entry widget for user to enter the path
path_entry = tb.Entry(main_frame, font=("Helvetica", 16), bootstyle="light")
path_entry.pack(pady=10, padx=50)

# Button to submit the path
submit_button = tb.Button(main_frame, text="Submit Path", bootstyle="success", command=submit_path)
submit_button.pack(pady=20)

# Define a class to stack frames
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # TODO: change where window is initiated

        self.title_font = tk.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ProcessPage, WarningPage, CompletePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
    
            frame.grid(row=0, column=0, sticky="nsew")

        # TODO: Edit order of pages
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''
        Show a frame for the given page name

        input: 
        page_name (str): the variable name of the page
        '''
        frame = self.frames[page_name]
        frame.tkraise()

# Start title page where the end-user enters the path to submissions folder
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

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

    # Button to submit the file path
    def submit_action():
        file_path = file_path_entry.get()  # This gets the text from the entry widget
        print("File Path Entered:", file_path)  # You can replace this with any action you need to perform with the file path


# Process page will be shown when the path is a valid path, and leads to a folder
# that contains at least 1 pdf file
class ProcessPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the process page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        # TODO: Redesign button
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class WarningPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Warning page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        # TODO: Design button
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class CompletePage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label =  tk.Label(self, text="This is the Complete page", font=controller.title_font)

        # TODO: Design button

def run():
    '''
    Initiate both front end and backend
    '''
    # TODO: add frames

    root.mainloop()

