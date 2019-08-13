from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql.cursors
import datetime
import After_new

class Addnew:
    def __init__(self):
        self.rt=Tk()
        self.rt.title("Add New Book")
        self.rt.configure(background="#80c1ff")
        self.rt.geometry("925x650+120+100")
        self.l1 = Label(self.rt)
        self.l1.place(relx=0.22, rely=0.0, height=120, width=700)