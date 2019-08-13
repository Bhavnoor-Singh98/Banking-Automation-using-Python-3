from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import After_new
class ViewAllAccount:
    def __init__(self,uname):
        self.root = Tk()

        self.root.title("View All accounts")
        self.root.geometry("1145x800+160+0")
        #self.root.geometry("920x560+100+100")
        #self.root.resizable(False, False)
        self.root.config(background='#ffffcc')

        self.conn = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
        self.cursor = self.conn.cursor()

        i1 = ImageTk.PhotoImage(Image.open("bank_images/va.jpg"))
        self.Label1 = Label(self.root, image=i1)
        self.Label1.place(relx=0.0, rely=0.0, width=250, height=180)
        self.id = uname
        i2=ImageTk.PhotoImage(Image.open("bank_images/ba.jpg"))#i2 = PhotoImage(file="banksimages/ViewAllAccounts.gif")
        self.Label2 = Label(self.root, image=i2)
        self.Label2.place(relx=0.35, rely=0.0, width=320, height=210)

        self.l=Label(self.root)
        self.l.place(relx=0.74, rely=0.15, width=320, height=30)
        self.l.configure(text="AVAILABLE ACCOUNTS:-", font=('Times New Roman', 20, 'underline') , background="#66b3ff")#, background=""#ac7339  #85C1E9
        #, foreground = '#070707', background = '#ac7339'

        self.ls = Listbox(self.root, selectmode=SINGLE)
        self.ls.place(relx=0.84, rely=0.22, relwidth=0.15, relheight=0.76)
        #self.ls.configure(foreground='#070707', background='#ac7339')

        self.fr = Frame(self.root, relief=RAISED, background='#85C1E9')
        self.fr.place(relx=0.26, rely=0.32, width=558, height=375)

        self.l1 = Label(self.fr, text="Account No", font=('Times New Roman', 14, 'bold'), foreground='#070707',
                        background='#85C1E9')
        self.l1.place(relx=0.0, rely=0.0, height=20, width=195)
        self.l2 = Label(self.fr, text="       Customer Name", font=('Times New Roman', 14, 'bold'), foreground='#070707',
                        background='#85C1E9')
        self.l2.place(relx=0.0, rely=0.1, height=20, width=195)
        self.l3 = Label(self.fr, text="         Customer Address", font=('Times New Roman', 14, 'bold'), foreground='#070707',
                        background='#85C1E9')
        self.l3.place(relx=0.0, rely=0.2, height=20, width=195)
        self.l4 = Label(self.fr, text="        Customer Gender", font=('Times New Roman', 14, 'bold'), foreground='#070707',
                        background='#85C1E9')
        self.l4.place(relx=0.0, rely=0.3, height=20, width=195)
        self.l5 = Label(self.fr, text="    Customer Email", font=('Times New Roman', 14, 'bold'), foreground='#070707',
                        background='#85C1E9')
        self.l5.place(relx=0.0, rely=0.4, height=20, width=195)
        self.l6 = Label(self.fr, text="         Customer Contact", font=('Times New Roman', 14, 'bold'), foreground='#070707',
                        background='#85C1E9')
        self.l6.place(relx=0.0, rely=0.5, height=20, width=195)
        self.l7 = Label(self.fr, text="       Customer's Father Name", font=('Times New Roman', 14, 'bold'),
                        foreground='#070707', background='#85C1E9')
        self.l7.place(relx=0.0, rely=0.6, height=20, width=265)
        self.l8 = Label(self.fr, text="        Customer's Mother Name", font=('Times New Roman', 14, 'bold'),
                        foreground='#070707', background='#85C1E9')
        self.l8.place(relx=0.0, rely=0.7, height=20, width=265)
        self.l9 = Label(self.fr, text="     Account Opening Date", font=('Times New Roman', 14, 'bold'),
                        foreground='#070707', background='#85C1E9')
        self.l9.place(relx=0.0, rely=0.8, height=20, width=265)
        self.l10 = Label(self.fr, text="Account Balance", font=('Times New Roman', 14, 'bold'),
                         foreground='#070707', background='#85C1E9')
        self.l10.place(relx=0.0, rely=0.9, height=20, width=235)

        self.t1 = Entry(self.fr, width=30, font=('Times New Roman', 12))
        self.t2 = Entry(self.fr, width=30, font=('Times New Roman', 12) )
        self.t3 = Entry(self.fr, width=30, font=('Times New Roman', 12))
        self.t4 = Entry(self.fr, width=30, font=('Times New Roman', 12))
        self.t5 = Entry(self.fr, width=30, font=('Times New Roman', 12))
        self.t6 = Entry(self.fr, width=30, font=('Times New Roman', 12))
        self.t7 = Entry(self.fr, width=30, font=('Times New Roman', 12))
        self.t8 = Entry(self.fr, width=30, font=('Times New Roman', 12))
        self.t9 = Entry(self.fr, width=30, font=('Times New Roman', 12))
        self.t10 = Entry(self.fr, width=30, font=('Times New Roman', 12))

        #self.l1.place(relx=0.015, rely=0.02, relwidth=0.2, relheight=0.05)
        #self.l2.place(relx=0.019, rely=0.12, relwidth=0.25, relheight=0.05)
        #self.l3.place(relx=0.0185, rely=0.22, relwidth=0.28, relheight=0.05)
        #self.l4.place(relx=0.0185, rely=0.32, relwidth=0.275, relheight=0.05)
        #self.l5.place(relx=0.019, rely=0.42, relwidth=0.26, relheight=0.05)
        #self.l6.place(relx=0.0243, rely=0.52, relwidth=0.28, relheight=0.05)
        #self.l7.place(relx=0.021, rely=0.62, relwidth=0.39, relheight=0.05)
        #self.l8.place(relx=0.035, rely=0.72, relwidth=0.378, relheight=0.05)
        #self.l9.place(relx=0.0264, rely=0.82, relwidth=0.35, relheight=0.05)
        #self.l10.place(relx=0.029, rely=0.92, relwidth=0.39, relheight=0.05)

        self.t1.place(relx=0.5, rely=0.0)
        self.t2.place(relx=0.5, rely=0.1)
        self.t3.place(relx=0.5, rely=0.2)
        self.t4.place(relx=0.5, rely=0.3)
        self.t5.place(relx=0.5, rely=0.4)
        self.t6.place(relx=0.5, rely=0.5)
        self.t7.place(relx=0.5, rely=0.6)
        self.t8.place(relx=0.5, rely=0.7)
        self.t9.place(relx=0.5, rely=0.8)
        self.t10.place(relx=0.5,rely=0.9)

        self.view()
        self.disable()
        self.ls.bind("<Double-Button-1>", self.fetchsingle)

        self.Butto = Button(self.root, command=self.other)
        self.Butto.place(relx=0.4, rely=0.87, height=57, width=197)
        img15 = ImageTk.PhotoImage(Image.open("bank_images/cvh.gif"))
        self.Butto.configure(image=img15)

        self.root.mainloop()

    def view(self):
        self.cursor.execute("select acc_no from tbaccount")
        # self.conn.commit()
        self.ls.delete(0, END)
        index = 0
        for row in self.cursor:
            self.ls.insert(index, row)
            index += 1

    def fetchsingle(self, evt):
        ind = self.ls.curselection()
        accno = self.ls.get(ind)
        self.cursor.execute("select * from tbaccount where acc_no = %s", (accno))
        #self.conn.commit()
        row = self.cursor.fetchone()
        self.clear()
        self.t1.insert(0, row[0])
        self.t2.insert(0, row[1])
        self.t3.insert(0, row[2])
        self.t4.insert(0, row[3])
        self.t5.insert(0, row[4])
        self.t6.insert(0, row[5])
        self.t7.insert(0, row[6])
        self.t8.insert(0, row[7])
        self.t9.insert(0, row[8])
        self.t10.insert(0, row[9])
        self.disable()

    def clear(self):
        self.normal()
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)
        self.t4.delete(0, END)
        self.t5.delete(0, END)
        self.t6.delete(0, END)
        self.t7.delete(0, END)
        self.t8.delete(0, END)
        self.t9.delete(0, END)
        self.t10.delete(0, END)

    def disable(self):
        self.t1.config(state='disabled')
        self.t2.config(state='disabled')
        self.t3.config(state='disabled')
        self.t4.config(state='disabled')
        self.t5.config(state='disabled')
        self.t6.config(state='disabled')
        self.t7.config(state='disabled')
        self.t8.config(state='disabled')
        self.t9.config(state='disabled')
        self.t10.config(state='disabled')

    def normal(self):
        self.t1.configure(state='normal')
        self.t2.configure(state='normal')
        self.t3.configure(state='normal')
        self.t4.configure(state='normal')
        self.t5.configure(state='normal')
        self.t6.configure(state='normal')
        self.t7.configure(state='normal')
        self.t8.configure(state='normal')
        self.t9.configure(state='normal')
        self.t10.configure(state='normal')
    def other(self):
        self.root.destroy()
        obja=After_new.Menu_Class(self.id)


#obj = ViewAllAccount(100)
