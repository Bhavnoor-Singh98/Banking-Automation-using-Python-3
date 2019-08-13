from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import After_new

class Security:
    def __init__(self, uname):
        self.root = Tk()
        self.root.geometry('1145x500+160+100')
        self.root.title('Update Security Settings')
        # self.root.resizable(False,False)
        self.root.configure(background="#ffffcc")

        self.id = uname
        self.conn = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
        self.cursor = self.conn.cursor()

        i0 = ImageTk.PhotoImage(Image.open("bank_images/setsec.gif"))
        self.Label1 = Label(self.root, image=i0)
        self.Label1.place(relx=0.39, rely=0.0, width=450, height=60)

        i1 = ImageTk.PhotoImage(Image.open("bank_images/secu.jpg"))
        self.Label1 = Label(self.root,image = i1)
        self.Label1.place(relx = 0.01,rely = 0.0,width = 250,height = 140)

        i2 = ImageTk.PhotoImage(Image.open("bank_images/secu1.jpg"))
        self.Label2 = Label(self.root,image = i2)
        self.Label2.place(relx = 0.84,rely = 0.00, width = 200,height = 150)

        self.Label3 = Label(self.root, text="Your Security Question is: ", font=('Times New Roman', '14', 'bold'))
        self.Label3.config(foreground='#070707', background='#85C1E9')
        self.Label3.place(relx=0.25, rely=0.43, width=250, height=50)

        self.Entry1 = Entry(self.root, font=('Times New Roman', 12))
        self.Entry1.place(relx=0.55, rely=0.43, width=180,height=50)
        self.Entry1.configure(background="#ebebe0")
        #self.Entry1.insert(0,)

        self.Label4 = Label(self.root, text="Security Answer: ", font=("Times New Roman", '14', 'bold'))
        self.Label4.config(foreground='#070707', background='#85C1E9')
        self.Label4.place(relx=0.25, rely=0.58, width=250, height=50)

        self.Entry2 = Entry(self.root, font=('Times New Roman', 12))
        self.Entry2.place(relx=0.55, rely=0.58, width=180,height=50)
        self.Entry2.configure(background="#ebebe0")

        self.cursor.execute('select adsecques, adsecans from tbadmin where admin_id = %s', (self.id))
        row=self.cursor.fetchone()
        self.Entry1.insert(0,row[0])
        self.Entry2.insert(0, row[1])
        self.conn.commit()

        self.Button1 = Button(self.root ) #text="Update", font=('Times New Roman', 16, 'bold')
        self.Button1.config( command=self.update) #foreground='#070707',
        self.Button1.place(relx=0.445, rely=0.8, width=150, height=55)
        img=ImageTk.PhotoImage(Image.open("bank_images/adsec.gif"))
        self.Button1.configure(image=img)

        self.root.mainloop()

    def update(self):
        secques = self.Entry1.get()
        secans = self.Entry2.get()

        if secques == "" or secans == "":
            messagebox.showerror('Info', 'Cannot be empty')

        else:
            self.cursor.execute('update tbadmin set adsecques = %s , adsecans = %s where admin_id = %s',
                                (secques, secans, self.id))
            self.conn.commit()
            messagebox.showinfo('Info', 'Updated successfully')
            self.root.destroy()
            u=After_new.Menu_Class(self.id)

#obj = Security("100")