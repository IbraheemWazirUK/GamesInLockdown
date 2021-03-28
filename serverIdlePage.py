import tkinter as tk
from tkinter import ttk

class ServerIdlePage(tk.Frame):

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
        self.page='ServerIdle'

        label = tk.Label(
            self,
            text="Waiting for players...",
            width=25,
            height=1,
            bg=self.backgroundColour,
            font=("Helvitca 15 bold"),
            fg=self.fontColour2,
            highlightbackground=self.outlineColour,
            highlightthickness=10
        )
        label.pack(side=tk.TOP, pady=(100, 50))

        textBox = tk.Text(
            self,
            height=16,
            width=100,
            state=tk.DISABLED
        )

        textBox.pack(side=tk.TOP)
        
        createGame = tk.Button (
            self,
            text="Start match!",
            width=25,
            height=1,
            bg=self.backgroundColour,
            font=("Helvitca 15 bold"),
            fg=self.fontColour2,
            highlightbackground=self.outlineColour,
            highlightthickness=10,
            command=self.startGame
        )
        createGame.pack(side=tk.TOP, pady=(20,0))
        textBox.config(state=tk.NORMAL)
        textBox.insert(tk.END, "test")
        textBox.config(state=tk.DISABLED)
        self.pack(fill='both')

    def playerJoin(self, name):
        textBox.config(state=tk.NORMAL)
        textBox.insert(tk.END, "Player: " + name)
        textBox.config(state=tk.DISABLED)
        
    def startGame(self):
        # Give access to client 
        self.main.wait_for_score()
        

        
