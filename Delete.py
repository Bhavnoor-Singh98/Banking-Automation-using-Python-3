from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import After_new
class del_acc:
    def __init__(self,uname):
        self.rt=Tk()
        self.rt.title("DELETION WINDOW")
        self.rt.configure(background="#ffffcc")
        self.rt.geometry("1145x500+160+100")
        self.l1 = Label(self.rt)
        self.l1.place(relx=0.22, rely=0.0, height=170, width=700)
        img1 = ImageTk.PhotoImage(Image.open("bank_images/del1.gif"))
        self.l1.configure(image=img1,background="#ffffcc")
        self.id = uname
        self.Label2 = Label(self.rt)
        self.Label2.place(relx=0.3, rely=0.40, height=40, width=169)
        self.Label2.configure(background="#3366cc")

        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''ENTER ACCOUNT NUMBER''')
        #self.Label2.configure(width=169)

        self.Entry1 = Entry(self.rt)
        self.Entry1.place(relx=0.53, rely=0.40, height=40, relwidth=0.21)
        self.Entry1.configure(font="TkFixedFont",background="#ffffff")
        self.Entry1.insert(0,"#0000")
        self.Entry1.configure(state="readonly")
        self.Entry1.configure(state="normal")


        self.Button1 = Button(self.rt, command=self.view)
        self.Button1.place(relx=0.36, rely=0.70, height=110, width=320)
        img3 = ImageTk.PhotoImage(Image.open("bank_images/deln.gif"))
        self.Button1.configure(background="#996633",image=img3)
        #self.Button1.configure(width=156)

        self.rt.mainloop()

    def view(self):#correct this ftn
        con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
        cursor = con.cursor()
        aid = int(self.Entry1.get())
        cursor.execute("select * from tbaccount where acc_no=%s", (aid))
        con.commit()
        rows = cursor.rowcount
        if rows > 0:
            messagebox.showwarning("Warning", "Delete Account")
            con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
            cursor = con.cursor()
            aid = int(self.Entry1.get())
            cursor.execute("delete from tbaccount where acc_no=%s", (aid))
            con.commit()

            messagebox.showinfo('Info', 'Account Deleted')
            self.rt.destroy()
            obs = After_new.Menu_Class(self.id)


        else:
            messagebox.showinfo('Info', 'Invalid Account No.')
            self.Entry1.delete(0, END)



#ab=del_acc()