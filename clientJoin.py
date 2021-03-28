import tkinter as tk
from tkinter import ttk
from threading import Thread
import ScreenServer2
import client

class ClientJoin(tk.Frame):

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
            text="Enter the hosts IP!",
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
            text="Enter IP:",
            width=20,
            height=1,
            #bg=self.backgroundColour,
            font=("Helvitca 15 bold"),
            fg='#000000',
            highlightbackground=self.outlineColour,
            highlightthickness=10
        )
        label1.pack(side=tk.TOP, pady=15)

        self.ip = tk.Entry(
            self,
            text="Enter IP:"
        )
        self.ip.pack(side=tk.TOP, pady=5)

        label2 = tk.Label(
            self,
            text="Enter your username:",
            width=20,
            height=1,
            #bg=self.backgroundColour,
            font=("Helvitca 15 bold"),
            fg='#000000',
            highlightbackground=self.outlineColour,
            highlightthickness=10
        )
        label2.pack(side=tk.TOP, pady=15)

        self.username = tk.Entry(
            self,
            text="Enter Username:"
        )
        self.username.pack(side=tk.TOP)
        
        connect = tk.Button (
            self,
            text="Connect!",
            width=25,
            height=1,
            bg=self.backgroundColour,
            font=("Helvitca 15 bold"),
            fg=self.fontColour2,
            highlightbackground=self.outlineColour,
            highlightthickness=10,
            command=self.connect
        )
        connect.pack(side=tk.TOP, pady=(30, 0))

    def connect(self):
        ipAdr = self.ip.get()
        username = self.username.get()
        Thread(target = client.initiate, args=[ipAdr, username, 5006]).start()
        Thread(target = ScreenServer2.main, args=[ipAdr, 5006]).start()
        self.main.connect_client_host()