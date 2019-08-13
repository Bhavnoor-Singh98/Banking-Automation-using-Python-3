from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import After_new


class EditPrf:
    def __init__(self, uname):

        self.root = Tk()
        self.root.geometry("1145x500+160+100")
        self.root.title("Edit Admin's Profile")
        # self.root.resizable(False,False)
        self.root.configure(background="#ffffcc")

        self.id = uname
        self.conn = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
        self.cursor = self.conn.cursor()

        i1 = ImageTk.PhotoImage(Image.open("bank_images/admod1.png"))
        self.Label1 = Label(self.root,image = i1)
        self.Label1.place(relx = 0.01,rely = 0.0, width = 210,height = 210)

        i2 = ImageTk.PhotoImage(Image.open("bank_images/adprof.gif"))
        self.Label2 = Label(self.root)
        self.Label2.place(relx = 0.32,rely = 0.0, width = 475,height = 60)
        self.Label2.configure(image=i2)

        i3 = ImageTk.PhotoImage(Image.open("bank_images/admod2.jpg"))
        self.Label7 = Label(self.root)
        self.Label7.place(relx=0.79, rely=0.0, width=275, height=210)
        self.Label7.configure(image=i3)

        self.Label3 = Label(self.root, text="Name: ", font=('Times New Roman', '14', 'bold'))
        self.Label3.config(foreground='#070707', background='#85C1E9')
        self.Label3.place(relx=0.26, rely=0.35, width=180, height=40)

        self.Entry1 = Entry(self.root,font=('Times New Roman', 12))
        self.Entry1.place(relx=0.5, rely=0.35,width=180, height=40)
        self.Entry1.configure(background="#ebebe0")

        self.Label4 = Label(self.root, text="Address: ", font=("Times New Roman", '14', 'bold'))
        self.Label4.config(foreground='#070707', background='#85C1E9')
        self.Label4.place(relx=0.26, rely=0.45, width=180, height=40)

        self.Text1 = Text(self.root, font=('Times New Roman', 12))
        #self.Text1.place(relx=0.55, rely=0.46, width=100, height=40)
        self.Text1.configure(background="#ebebe0")
        self.Text1.place(relx=0.5, rely=0.45, width=180, height=40)

        self.Label5 = Label(self.root, text="Mobile No: ", font=("Times New Roman", '14', 'bold'))
        self.Label5.config(foreground='#070707', background='#85C1E9')
        self.Label5.place(relx=0.26, rely=0.55, width=180, height=40)

        self.Entry2 = Entry(self.root, font=('Times New Roman', 12))
        self.Entry2.place(relx=0.5, rely=0.55, width=180, height=40)
        self.Entry2.configure(background="#ebebe0")

        self.Label6 = Label(self.root, text="Email ID: ", font=("Times New Roman", '14', 'bold'))
        self.Label6.config(foreground='#070707', background='#85C1E9')
        self.Label6.place(relx=0.26, rely=0.65, width=180, height=40)

        self.Entry3 = Entry(self.root, font=('Times New Roman', 12))
        self.Entry3.place(relx=0.5, rely=0.65, width=180, height=40)
        self.Entry3.configure (background="#ebebe0")

        self.Button2 = Button(self.root)
        i5 = ImageTk.PhotoImage(Image.open("bank_images/admod.gif"))
        self.Button2.config(image=i5, command=self.modify)
        self.Button2.place(relx=0.39, rely=0.83, width=150, height=60)

        self.cursor.execute("select admin_name,admin_add,admin_el,admin_ph from tbadmin where admin_id = %s", (self.id))
        row = self.cursor.fetchone()
        self.Entry1.insert(0, row[0])
        self.Text1.insert('1.0', row[1])
        self.Entry2.insert(0, row[3])
        self.Entry3.insert(0, row[2])

        self.conn.commit()


        self.root.mainloop()

    def modify(self):
        nm = self.Entry1.get()
        add = self.Text1.get('1.0', END)
        mob = self.Entry2.get()
        email = self.Entry3.get()

        if nm == "" or len(add) == 0 or email == "" or mob == "":
            messagebox.showerror('Info', "Can't be empty")

        else:
            try:
                mob1 = int(mob)
            except ValueError as e:
                messagebox.showerror('Info', 'Contact no. can only be an integer value!!')
                return

            if len(mob) != 9:
                messagebox.showerror('Info', 'Contact no. can only be of 9-digits!!')
                return

            elif not ('@gmail.com' in email):
                messagebox.showerror('Info', 'Invalid Email ID!!')
                return
            else:
                self.cursor.execute('update tbadmin set admin_name = %s,admin_add = %s,admin_el = %s,admin_ph = %s where admin_id = %s',(nm, add, email, mob, self.id))
                self.conn.commit()
                messagebox.showinfo('Info', 'Updated successfully!!')
                self.root.destroy()
                obj2 = After_new.Menu_Class(self.id)


#obj = EditPrf('')