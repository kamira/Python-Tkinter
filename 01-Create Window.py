from tkinter import *
from tkinter import ttk

class Application(Frame):
  def __init__(self, master, str_Title = "None"):
    ttk.Frame.__init__(self, master)
    
    self.grid()
    
    self.master.title(str_Title)
    self.master.geometry("1000x505")
    self.master.resizable(height=False, width=False)
    
 root = Tk()
 app = Application(root)
 
 root.mainloop()
