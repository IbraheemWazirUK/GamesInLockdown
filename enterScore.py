import tkinter as tk
from tkinter import ttk

class EnterScore(tk.Frame):

    def __init__(self,master,main):

        super().__init__(master)
        self.config()

        ##Colour Scheme##
        self.backgroundColour = '#4CAF50' 
        self.fontColour = '#FFFFFF'
        self.fontColour2 = '#FFFFFF'
        self.foregroundColour = '#4E4E50'
        self.outlineColour = '#6F2232'
        self.master = master # Tkinter widget
        self.main = main # Object
        self.page='ScorePage'
        self.tbw = 15

        label = tk.Label(
            self,
            text="Enter the final scores!",
            width=20,
            height=1,
            bg=self.backgroundColour,
            font=("Helvitca 15 bold"),
            fg=self.fontColour2,
            highlightbackground=self.outlineColour,
            highlightthickness=10
        )
        label.pack(side=tk.TOP, pady=(100, 50))

        label1 = tk.Label(
            self,
            text="Player 1:",
            width=20,
            height=1,
            #bg=self.backgroundColour,
            font=("Helvitca 15 bold"),
            fg='#000000',
            highlightbackground=self.outlineColour,
            highlightthickness=10
        )
        label1.pack(side=tk.TOP, pady=15)
        
        textBox = tk.Text(
            self,
            height=1,
            width=self.tbw,
        )
        textBox.pack(side=tk.TOP)

        label2 = tk.Label(
            self,
            text="Player 2:",
            width=20,
            height=1,
            #bg=self.backgroundColour,
            font=("Helvitca 15 bold"),
            fg='#000000',
            highlightbackground=self.outlineColour,
            highlightthickness=10
        )
        label2.pack(side=tk.TOP, pady=15)
        
        textBox1 = tk.Text(
            self,
            height=1,
            width=self.tbw,
        )
        textBox1.pack(side=tk.TOP)

        submit = tk.Button (
            self,
            text="Submit Scores!",
            width=25,
            height=1,
            bg=self.backgroundColour,
            font=("Helvitca 15 bold"),
            fg=self.fontColour2,
            highlightbackground=self.outlineColour,
            highlightthickness=10,
            command=self.submit
        )
        submit.pack(side=tk.TOP, pady=(30, 0))

    def submit(self):
        self.main.add_server_idle()
