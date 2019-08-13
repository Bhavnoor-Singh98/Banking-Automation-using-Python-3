from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql.cursors
import datetime
import After_new

class openi_acc:
    def __init__(self,uname):
        self.rt=Tk()
        self.rt.title("ACCOUNT OPENING")
        self.rt.configure(background="#ffffcc")
        self.rt.geometry("925x650+120+100")
        self.l1=Label(self.rt)
        self.l1.place(relx=0.22, rely=0.0, height=120, width=700)
        img1 = ImageTk.PhotoImage(Image.open("bank_images/open2.gif"))
        self.l1.configure(image=img1,background="#ffffcc")
        self.id = uname

        self.Label2 = Label(self.rt)
        self.Label2.place(relx=0.255, rely=0.28, height=25, width=169)
        self.Label2.configure(background="#99ccff")

        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''    ACCOUNT NUMBER''')
        self.Label2.configure(width=169)

        self.Entry1 = Entry(self.rt)
        self.Entry1.place(relx=0.44, rely=0.28, height=25, relwidth=0.21)
        self.Entry1.configure(font="TkFixedFont")

        self.Label3 = Label(self.rt)
        self.Label3.place(relx=0.255, rely=0.32, height=25, width=169)
        self.Label3.configure(background="#99ccff")

        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text=''' CUSTOMER NAME''')
        self.Label3.configure(width=169)

        self.Entry2 = Entry(self.rt)
        self.Entry2.place(relx=0.44, rely=0.32, height=25, relwidth=0.21)
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.insert(0,"#Your Name")
        self.Entry2.configure(state="readonly")
        self.Entry2.configure(state="normal")

        self.Label4 = Label(self.rt)
        self.Label4.place(relx=0.255, rely=0.64, height=25, width=169)
        self.Label4.configure(background="#99ccff")

        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''     CUSTOMER ADDRESS''')
        self.Label4.configure(width=169)

        self.Entry3 = Entry(self.rt)
        self.Entry3.place(relx=0.44, rely=0.642, height=25, relwidth=0.21)
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.insert(0, "#Your Address")
        self.Entry3.configure(state="readonly")
        self.Entry3.configure(state="normal")


        self.Label5 = Label(self.rt)
        self.Label5.place(relx=0.255, rely=0.36, height=25, width=169)
        self.Label5.configure(background="#99ccff")

        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''    CUSTOMER GENDER''')
        self.Label5.configure(width=169)

        self.s1 = StringVar()
        self.s1.set("MALE")
        self.r1 = Radiobutton(self.rt, text="MALE", variable=self.s1, value="MALE")
        self.r1.place(relx=0.44, rely=0.36, height=25, relwidth=0.08)

        self.r2 = Radiobutton(self.rt, text="FEMALE", variable=self.s1, value="FEMALE")
        self.r2.place(relx=0.51, rely=0.36, height=25, relwidth=0.14)

        self.Label6 = Label(self.rt)
        self.Label6.place(relx=0.255, rely=0.40, height=25, width=169)
        self.Label6.configure(background="#99ccff")

        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text=''' CUSTOMER E-MAIL''')
        self.Label6.configure(width=169)

        self.Entry5 = Entry(self.rt)
        self.Entry5.place(relx=0.44, rely=0.40, height=25, relwidth=0.21)
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.insert(0, "Me@gmail.com")
        self.Entry5.configure(state="readonly")
        self.Entry5.configure(state="normal")

        self.Label7 = Label(self.rt)
        self.Label7.place(relx=0.255, rely=0.44, height=25, width=169)
        self.Label7.configure(background="#99ccff")

        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''   CUSTOMER MOBILE''')
        self.Label7.configure(width=169)

        self.Entry6 = Entry(self.rt)
        self.Entry6.place(relx=0.44, rely=0.44, height=25, relwidth=0.21)
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.insert(0, "#8164")
        self.Entry6.configure(state="readonly")
        self.Entry6.configure(state="normal")

        self.Label8 = Label(self.rt)
        self.Label8.place(relx=0.255, rely=0.48, height=25, width=169)
        self.Label8.configure(background="#99ccff")

        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''FATHER'S NAME''')
        self.Label8.configure(width=169)

        self.Entry7 = Entry(self.rt)
        self.Entry7.place(relx=0.44, rely=0.48, height=25, relwidth=0.21)
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.insert(0, "#Name")
        self.Entry7.configure(state="readonly")
        self.Entry7.configure(state="normal")

        self.Label9 = Label(self.rt)
        self.Label9.place(relx=0.255, rely=0.52, height=25, width=169)
        self.Label9.configure(background="#99ccff")

        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''MOTHER'S NAME''')
        self.Label9.configure(width=169)

        self.Entry8 = Entry(self.rt)
        self.Entry8.place(relx=0.44, rely=0.52, height=25, relwidth=0.21)
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.insert(0, "#Name")
        self.Entry8.configure(state="readonly")
        self.Entry8.configure(state="normal")

        self.Label10 = Label(self.rt)
        self.Label10.place(relx=0.254, rely=0.56, height=25, width=168.7)
        self.Label10.configure(background="#99ccff")

        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''OPENING DATE ''')
        self.Label10.configure(width=169)

        self.a1=datetime.date.today()

        self.l1=Label(self.rt)
        self.l1.place(relx=0.44, rely=0.56, height=25, relwidth=0.21)
        self.l1.config( text=self.a1)

        self.Label11 = Label(self.rt)
        self.Label11.place(relx=0.255, rely=0.60, height=25, width=169)
        self.Label11.configure(background="#99ccff")

        self.Label11.configure(foreground="#000000") #adad85  #000000
        self.Label11.configure(text=''' OPENING BALANCE''')
        self.Label11.configure(width=169)

        self.Entry10 = Entry(self.rt)
        self.Entry10.place(relx=0.44, rely=0.60, height=25, relwidth=0.21)
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.insert(0,"0")
        self.Entry10.configure(state="disabled")
        #self.Entry10.set(text="0")

        self.but = Button(self.rt,command=self.save)#
        self.but.place(relx=0.4, rely=0.8, height=35, width=200)
        img2 = ImageTk.PhotoImage(Image.open("d:\\but.gif"))
        self.but.configure(image=img2)  #text="SAVE YOUR ACCOUNT" ,background="#ff3399"

        self.ta = Text(self.rt)
        self.generateAccno()

        self.rt.mainloop()
    def generateAccno(self):
        con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
        cursor = con.cursor()
        cursor.execute("select ifnull(max(acc_no),9999) from tbaccount")
        con.commit()
        row=cursor.fetchone()
        ano=row[0]
        ano=ano+1
        self.Entry1.configure(state="normal")
        self.Entry1.delete(0,END)
        self.Entry1.insert(0,ano)
        self.Entry1.configure(state="disabled")



    def save(self):
        if(self.Entry2.get()=="" or self.Entry3.get()=="" or self.Entry5.get()=="" or self.Entry7.get()=="" or self.Entry8.get()=="" ):
            messagebox.showerror("Info","Can't be Empty")
        elif(len(self.Entry6.get()) < 9  or len(self.Entry6.get()) > 9 ):
            messagebox.showerror("Info","Enter 9-digit Mobile Number")
        else:
            try:
                accno = int(self.Entry1.get())
                cmob = int(self.Entry6.get())
                copb = int(self.Entry10.get())
            except ValueError as e:
                messagebox.showerror("Info","Account No, Mobile No. and  Opening Balance can be Integers Only")
                return
            cname = self.Entry2.get()
            cname1=cname.title()
            cadd = self.Entry3.get()
            cadd1=cadd.title()
            cgen = self.s1.get()
            cmail = self.Entry5.get()
            f_name = self.Entry7.get()
            f_name1=f_name.title()
            m_name = self.Entry8.get()
            m_name1=m_name.title()
            copd = self.a1
            try:
                con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
                cursor = con.cursor()
                cursor.execute("insert into tbaccount values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(accno, cname1, cadd1, cgen, cmail, cmob, f_name1, m_name1, copd, copb))
                con.commit()
                rows = cursor.rowcount
                if rows > 0:
                    row = cursor.fetchone()
                    self.Entry1.config(state='disabled')
                    self.Entry2.config(state='disabled')
                    self.Entry3.config(state='disabled')
                    self.Entry5.config(state='disabled')
                    self.Entry6.config(state='disabled')
                    self.Entry7.config(state='disabled')
                    self.Entry8.config(state='disabled')
                    #self.Entry10.config(state='disabled')
                    messagebox.showinfo('Info', 'Saved')
                    self.ftn = self.back()

                else:
                    messagebox.showinfo('Info', 'Insert Correct Values')
                    self.Entry1.delete(0, END)
                    self.Entry2.delete(0, END)
                    self.Entry3.delete(0, END)
                    self.Entry5.delete(0, END)
                    self.Entry6.delete(0, END)
                    self.Entry7.delete(0, END)
                    self.Entry8.delete(0, END)
                    #self.Entry10.delete(0, END)

            except Exception as e:
                messagebox.showerror("Info",e)
                return

    def back(self):
        self.rt.destroy()
        f = After_new.Menu_Class(self.id)




#ob=openi_acc()