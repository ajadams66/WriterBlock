from tkinter import *


BLACK = "#080202"

class Timer(Label):
    """creates a Label on the User Interface"""
    def __init__(self):
        super().__init__()
        self.config(text="5 secs", font=("Helvetica", 30, "bold"), fg=BLACK,)
        self.grid(column=1, row=4,  columnspan=2)