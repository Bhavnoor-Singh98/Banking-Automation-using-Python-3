from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import Progressbar
import threading
import Login_new
import time

class load_class:
    def __init__(self):
        self.rt=Tk()
        self.rt.title("YOUR BANKING SOLUTIONS")
        self.rt.config(background="#ccffcc")
        self.rt.geometry("1145x500+160+100")
        #self.rt.geometry("920x450+200+180")

        self.l1=Label(self.rt)
        self.l1.place(relx=0.25, rely=0.0, height=200, width=650)
        self.l1.config(background="#ccffcc")
        img1=ImageTk.PhotoImage(Image.open("bank_images/load.gif"))
        self.l1.configure(image=img1)

        self.label1 = Label(self.rt)
        self.label1.place(relx=0.26, rely=0.29, height=200, width=650)
        self.label1.config(background="#ccffcc")
        imgq = ImageTk.PhotoImage(Image.open("bank_images/l.gif"))
        self.label1.configure(image=imgq)

        self.v1=IntVar() #has the current value of progressbar

        self.l2=Label(self.rt)
        self.l2.place(relx=0.06, rely=0.71, height=40, width=380)
        self.l2.configure(background="#ccffcc")
        self.l2.configure(width=380)

        self.pb=Progressbar(self.rt,orient=HORIZONTAL)
        self.pb.configure(mode='determinate',maximum=100)
        self.pb.configure(variable=self.v1)

        self.pb.place(relx=0.08, rely=0.80, relwidth=0.90, relheight=0.0, height=49)
        self.pb.configure(length="650")

        tup = (101,)
        self.t1=threading.Thread(target=self.move,args=tup,name='first')
        self.t1.start()
        self.rt.after(500,self.check)
        self.rt.mainloop()

    def move(self,a):
        for i in range(a):
            self.v1.set(i)
            self.l2.configure(text="Loading "+str(self.v1.get()) +"%")
            time.sleep(0.01)

    def check(self):
        if self.v1.get() != 100:
            self.rt.after(500,self.check)
        else:
            self.rt.destroy()
            object=Login_new.Login_Class()
#ob=load_class()