import tkinter as tk
import ScreenClient2
import multiClientServer
import runpy
from threading import Thread
import ScreenServer2
import multiClientServer

class WelcomePage(tk.Frame):
    
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
        self.page='Welcome'

        clientButton = tk.Button (
            self,
            text="Join a match!",
            width=25,
            height=1,
            bg=self.backgroundColour,
            font=("Helvitca 15 bold"),
            fg=self.fontColour2,
            highlightbackground=self.outlineColour,
            highlightthickness=10,
            command=self.clientToServer
        )
        clientButton.pack(side=tk.TOP, pady=(200, 50))


        hostButton = tk.Button (
            self,
            text="Start charity match!",
            width=25,
            height=1,
            bg=self.backgroundColour,
            font=("Helvitca 15 bold"),
            fg=self.fontColour2,
            highlightbackground=self.outlineColour,
            highlightthickness=10,
            command=self.createServer
        )
        hostButton.pack(side=tk.TOP)
        
        self.pack(fill='both')


    def clientToServer(self):
        self.main.connect_client_host()

    def createServer(self):
        Thread(target = multiClientServer.main).start()
        Thread(target = ScreenServer2.main).start()
        self.main.add_server_idle()
        
    
