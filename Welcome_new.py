from tkinter import *
from PIL import Image,ImageTk
import Loading_new
class welcome:
    def __init__(self):
        self.rt=Tk()
        self.rt.title("YOUR BANKING SOLUTIONS")
        self.rt.config(background="#ccffcc")    #FFFFCC       #94b8b8
        self.rt.geometry("1145x500+160+100")

        self.l1=Label(self.rt)
        self.l1.place(relx=0.25, rely=0.0, height=81, width=604)
        img1=ImageTk.PhotoImage(Image.open("bank_images/image1.gif"))
        self.l1.configure(image=img1)
        self.l1.configure(background="#ccffcc")

        self.l2=Label(self.rt)
        self.l2.place(relx=0.13, rely=0.2, height=315, width=990)
        limg=ImageTk.PhotoImage(Image.open("bank_images/Branchless1.jpg"))
        self.l2.configure(image=limg)

        self.but=Button(self.rt,command=self.click)
        self.but.place(relx=0.4, rely=0.84, height=73, width=268)
        img2 = ImageTk.PhotoImage(Image.open("bank_images/cli.gif"))
        self.but.configure(image=img2)
        self.rt.mainloop()

    def click(self):
        self.rt.destroy()
        lo=Loading_new.load_class()


ob=welcome()