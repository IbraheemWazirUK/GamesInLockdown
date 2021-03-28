import tkinter as tk
from welcomePage import WelcomePage
from serverIdlePage import ServerIdlePage
from enterScore import EnterScore
from clientJoin import ClientJoin

class Master():
    def __init__(self, root, geometry):

        self.master = root
        self.geometry = geometry
        self.master.geometry(self.geometry)

        self.activeWidget = None
        self.add_welcome_screen()


    def remove_active_widget(self):
        if self.activeWidget != None:
            self.activeWidget.destroy()
            self.activeWidget = None
        
    def add_welcome_screen(self):   
        self.remove_active_widget()
        self.welcomePage = WelcomePage(self.master, self)
        self.welcomePage.pack(fill='both', expand=True)
        self.activeWidget = self.welcomePage

    def add_server_idle(self):
        self.remove_active_widget()
        self.serverIdlePage = ServerIdlePage(self.master, self)
        self.serverIdlePage.pack(fill='both', expand=True)
        self.activeWidget = self.serverIdlePage

    def wait_for_score(self):
        self.remove_active_widget()
        self.scorePage = EnterScore(self.master, self)
        self.scorePage.pack(fill='both', expand=True)
        self.activeWidget = self.scorePage
        
    def connect_client_host(self):
        self.remove_active_widget()
        self.clientJoin = ClientJoin(self.master, self)
        self.clientJoin.pack(fill='both', expand=True)
        self.activeWidget = self.clientJoin

    def get_master(self):
        return self.master
    
