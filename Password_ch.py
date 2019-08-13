from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import After_new

class Password:
    def __init__(self, uname):
        self.root = Tk()
        self.root.geometry("1145x500+160+100")
        self.root.title('Update Password')
        # self.root.resizable(False,False)
        self.root.configure(background="#ffffcc")

        self.id = uname
        self.conn = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
        self.cursor = self.conn.cursor()

        #  i1 = ImageTk.PhotoImage(Image.open("banksimages/23.jpg"))
        # self.Label1 = Label(self.root,image = i1)
        # self.Label1.place(relx = 0.0,rely = 0.0,relwidth = 0.32,relheight = 0.3)

        i2 = ImageTk.PhotoImage(Image.open("bank_images/PU.gif"))
        self.Label2 = Label(self.root,image = i2)
        self.Label2.place(relx = 0.37,rely = 0.027, width = 380,height = 60)

        i21 = ImageTk.PhotoImage(Image.open("bank_images/pup.jpg"))
        self.Label56 = Label(self.root, image=i21)
        self.Label56.place(relx=0.01, rely=0.0, width=200, height=180)

        i22 = ImageTk.PhotoImage(Image.open("bank_images/pup2.jpg"))
        self.Label200 = Label(self.root, image=i22)
        self.Label200.place(relx=0.81, rely=0.0, width=250, height=160)

        self.Label3 = Label(self.root, text="Enter New Password: ", font=('Times New Roman', '14', 'bold'))
        self.Label3.config(foreground='#070707', background='#85C1E9')
        self.Label3.place(relx=0.26, rely=0.43, width=180, height=40)

        self.Entry1 = Entry(self.root, font=('Times New Roman', 12), show='*')
        self.Entry1.place(relx=0.52, rely=0.43,  width=180,height=40)
        self.Entry1.configure(background="#ebebe0")

        self.Label4 = Label(self.root, text="Confirm Password: ", font=("Times New Roman", '14', 'bold'))
        self.Label4.config(foreground='#070707', background='#85C1E9')
        self.Label4.place(relx=0.26, rely=0.56, width=180, height=40)

        self.Entry2 = Entry(self.root, font=('Times New Roman', 12), show='*')
        self.Entry2.place(relx=0.52, rely=0.56, width=180, height=40)
        self.Entry2.configure(background="#ebebe0")

        self.Button1 = Button(self.root)
        i5 = ImageTk.PhotoImage(Image.open("bank_images/adsec.gif"))
        self.Button1.config(foreground='#070707', command=self.update)
        self.Button1.configure(image=i5)
        self.Button1.place(relx=0.385, rely=0.8, width=150, height=70)

        self.root.mainloop()

    def update(self):
        pwd = self.Entry1.get()
        cpwd = self.Entry2.get()

        if pwd == "" or cpwd == "":
            messagebox.showerror('Info', 'Cannot be empty')

        else:
            if pwd == cpwd:
                self.cursor.execute('update tbadmin set admin_pass = %s where admin_id = %s', (pwd, self.id))
                self.conn.commit()
                messagebox.showinfo('Info', 'Updated successfully')
                self.root.destroy()
                aj=After_new.Menu_Class(self.id)
            else:
                messagebox.showerror('Info', 'Password and Confirm Password should match!!')
                self.Entry1.delete(0, END)
                self.Entry2.delete(0, END)

#obj = Password('100')