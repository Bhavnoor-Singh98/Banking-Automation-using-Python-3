from tkinter import *
from PIL import Image, ImageTk
import Forgot_new
import pymysql.cursors
from tkinter import messagebox
import After_new

class Login_Class:
    def __init__(self):
        self.rt = Tk()
        self.rt.geometry("1145x500+160+100")
        self.rt.title("YOUR BANKING SOLUTIONS")
        self.rt.configure(background="#ccffcc")     #FFFFCC

        self.Label1 = Label(self.rt)
        self.Label1.place(relx=0.27, rely=0.0, height=80, width=550)
        self.Label1.configure(background="#ccffcc")

        img1 = ImageTk.PhotoImage(Image.open("bank_images/login.gif"))
        self.Label1.configure(image=img1)

        self.Label2 = Label(self.rt)
        self.Label2.place(relx=0.263, rely=0.32, height=41, width=280)
        self.Label2.configure(background="#cc99ff")

        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''ENTER ADMIN ID''')
        self.Label2.configure(width=169, font=('Helvetica', 20))

        self.Label3 = Label(self.rt)
        self.Label3.place(relx=0.263, rely=0.45, height=41, width=280)
        self.Label3.configure(background="#cc99ff")

        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''ENTER PASSWORD''')
        self.Label3.configure(width=164, font=('Helvetica', 20))

        self.Entry1 = Entry(self.rt)
        self.Entry1.place(relx=0.6, rely=0.32, height=41, relwidth=0.18)
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.insert(0, "#0000")
        self.Entry1.configure(state="readonly")
        self.Entry1.configure(state="normal", font=('Helvetica', 20))

        self.Entry2 = Entry(self.rt)
        self.Entry2.place(relx=0.6, rely=0.45, height=41, relwidth=0.18)
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.insert(0, "*****")
        self.Entry2.configure(state="readonly")
        self.Entry2.configure(state="normal", font=('Helvetica', 20))
        self.Entry2.configure(show="*")

        self.Button1 = Button(self.rt, command=self.login)
        self.Button1.place(relx=0.55, rely=0.7, height=70, width=340)
        imga = ImageTk.PhotoImage(Image.open("bank_images/LOG.gif"))
        self.Button1.configure(image=imga)#,background="#ccffcc"
        #self.Button1.configure(width=156)

        self.Button2 = Button(self.rt, command=self.forgot)
        self.Button2.place(relx=0.03, rely=0.71, height=70, width=399)
        #self.Button2.configure(text='''FORGOT PASSWORD''')
        imge = ImageTk.PhotoImage(Image.open("bank_images/FOR.gif"))
        self.Button2.configure(image=imge)#,background="#ccffcc"
        self.rt.mainloop()

    def login(self):
        con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
        cursor = con.cursor()
        un = self.Entry1.get()
        pwd = self.Entry2.get()
        cursor.execute("select * from tbadmin where admin_id=%s and admin_pass=%s", (un, pwd))
        con.commit()
        rows = cursor.rowcount
        if rows > 0:
            messagebox.showinfo('Info', 'Welcome Admin')
            self.Entry1.delete(0, END)
            self.Entry2.delete(0, END)
            self.rt.destroy()
            object=After_new.Menu_Class(un)

        else:
            messagebox.showinfo('Info', 'Invalid Name or Password')
            self.Entry1.delete(0, END)
            self.Entry2.delete(0, END)
            return

    def forgot(self):
        self.rt.destroy()
        f = Forgot_new.Forgot_Class()

#obj = Login_Class()