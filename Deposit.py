from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import datetime
import time
import After_new

class depo_acc:
    def __init__(self,uname):
        self.rt=Tk()
        self.rt.title("DEPOSIT WINDOW")
        self.rt.configure(background="#ffffcc")
        self.rt.geometry("1145x500+160+100")
        self.id = uname
        self.l1 = Label(self.rt)
        self.l1.place(relx=0.31, rely=0.0, height=66, width=480)
        img1 = ImageTk.PhotoImage(Image.open("bank_images/depos.gif"))
        self.l1.configure(image=img1)

        self.Label2 = Label(self.rt)
        self.Label2.place(relx=0.3, rely=0.20, height=31, width=169)
        self.Label2.configure(background="#ff66ff")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''ENTER ACCOUNT NUMBER''')
        self.Label2.configure(width=169)

        self.Entry1 = Entry(self.rt)
        self.Entry1.place(relx=0.5, rely=0.2, height=31, width=189)
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.insert(0,"#00000")
        self.Entry1.configure(state="readonly")
        self.Entry1.configure(state="normal")

        self.lab=Label(self.rt)
        self.lab.place(relx=0.01, rely=0.0, height=220, width=280)
        img12 = ImageTk.PhotoImage(Image.open("bank_images/deposit.jpg"))
        self.lab.configure(image=img12)

        self.lab1 = Label(self.rt)
        self.lab1.place(relx=0.83, rely=0.0, height=220, width=220)
        img13 = ImageTk.PhotoImage(Image.open("bank_images/deposit2.png"))
        self.lab1.configure(image=img13)

        self.Button1 = Button(self.rt, command=self.check)
        self.Button1.place(relx=0.4, rely=0.38, height=58, width=173)
        img14 = ImageTk.PhotoImage(Image.open("bank_images/wm.gif"))
        self.Button1.configure(image=img14)

        #self.Label3.configure(width=169)

        self.Frame1 = Frame(self.rt)
        self.Frame1.place(relx=0.28, rely=0.3, relheight=0.25, relwidth=0.068)
        self.Frame1.configure(relief=FLAT)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#999966")
        self.Frame1.configure(width=530)

        self.Frame1.place_forget()

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.01, rely=0.03, height=31, width=178)
        self.Label3.configure(background="#ff66ff")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''CURRENT BALANCE''')

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.5, rely=0.03, height=31, width=178)
        self.Entry2.configure(font="TkFixedFont")
        #self.Entry2.insert(0, "#5896")
        #self.Entry2.configure(state="readonly")
        #self.Entry2.configure(state="normal")

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.01, rely=0.28, height=31, width=178)
        self.Label4.configure(background="#ff66ff")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''ENTER DEPOSIT AMOUNT''')

        self.Entry3 = Entry(self.Frame1)
        self.Entry3.place(relx=0.5, rely=0.28, height=31, width=178)
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.insert(0, "#5896")
        self.Entry3.configure(state="readonly")
        self.Entry3.configure(state="normal")

        self.Butto = Button(self.Frame1, command=self.other)
        self.Butto.place(relx=0.22, rely=0.6, height=58, width=240)
        img15 = ImageTk.PhotoImage(Image.open("bank_images/dm.gif"))
        self.Butto.configure(image=img15)


        #self.Button1.configure(width=456)

        self.rt.mainloop()
    def check(self):
        aid=self.Entry1.get()
        con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
        cursor = con.cursor()
        #aid = self.Entry1.get()
        cursor.execute("select op_bal from tbaccount where acc_no=%s", (aid))
        con.commit()
        rows = cursor.rowcount
        if rows > 0:
            row = cursor.fetchone()
            print(row)
            self.Entry1.configure(state="disabled")
            self.Frame1.place(relx=0.26, rely=0.3, relheight=0.45, relwidth=0.43)
            self.Entry2.insert(0, row)
            self.Entry2.configure(state="disabled")
        else:
            messagebox.showerror("Info","Enter Correct Account Number")
    def other(self):
        #abc=self.Entry3.get()
        aid = self.Entry1.get()
        if (self.Entry3.get() == ""):
            messagebox.showerror("Info", "Can't be Empty")
        else:
            try:
                abc = int(self.Entry3.get())

            except ValueError as e:
                messagebox.showerror("Info","Can be Integers Only")
                self.Entry3.delete(0, END)
                return
            self.Entry3.configure(state="disabled")
            abc1=int(abc)
        #aid = self.Entry1.get()
            con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
            cursor = con.cursor()
        # aid = self.Entry1.get()
            cursor.execute("select op_bal from tbaccount where acc_no=%s", (aid))
            con.commit()
            rows = cursor.rowcount
            if rows > 0:
                row = cursor.fetchone()
                row1=int(row[0])
                #print(row[0])
                #for i in row:
                    #print(row[0])#
                if(abc1 <=0):
                    messagebox.showerror("Info","Insufficient Amount")
                    self.Entry3.configure(state="normal")

                else:
                    con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
                    cursor = con.cursor()
                    aid = self.Entry1.get()
                    avalue=self.Entry3.get()
                    abvalue=self.Entry2.get()
                    sub=int(abvalue) + int(avalue)
                    cursor.execute("update tbaccount set op_bal=%s where acc_no=%s", (sub,aid))
                    con.commit()
                    rows = cursor.rowcount
                    if rows > 0:
                        row = cursor.fetchone()
                        messagebox.showinfo("Info","Successful")
                        a1 = datetime.date.today()
                        a2 = time.strftime("%H:%M:%S")
                        a3 = int(self.Entry3.get())
                        aid = int(self.Entry1.get())
                        con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
                        cursor = con.cursor()
                        cursor.execute("select ifnull(max(trans_id),0) from tbtransacc")
                        con.commit()
                        row = cursor.fetchone()
                        ano = row[0]
                        ano = ano + 1
                        tp = "Deposit"
                        con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
                        cursor = con.cursor()
                        cursor.execute("insert into tbtransacc values(%s,%s,%s,%s,%s,%s,%s)",(ano, aid, aid, tp, a3, a1, a2))
                        con.commit()

                        self.rt.destroy()
                        of = After_new.Menu_Class(self.id)

                    else:
                        messagebox.showerror("Info","Transaction Failed")
                        self.Entry3.configure(state="normal")
                        o1=After_new.Menu_Class(self.id)
    #def trans(self):



#ob=depo_acc(100)




