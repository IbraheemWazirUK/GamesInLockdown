import tkinter as tk
from tkinter import ttk
from master import Master

if __name__ == "__main__":
    root = tk.Tk()
    geometry = '1200x600'
    app = Master(root, geometry) 
    app.get_master().mainloop()
    
