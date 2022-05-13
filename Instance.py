from tkinter import Label, Entry

class Instance:

    def __init__(self, text_input, row_input):
        self.text_input = text_input
        self.row_input = row_input

        self.L = None
        self.E = None
        
    def make_instance(self, top):
        self.L = Label(top, text=self.text_input)
        self.L.grid(row=self.row_input,column=0)
        self.E = Entry(top, bd =5)
        self.E.grid(row=self.row_input,column=1)
