from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import After_new
from tkinter.ttk import Treeview

class mini_stat:
    def __init__(self,uname):
        self.rt = Tk()
        self.rt.title("STATEMENT WINDOW")
        self.rt.geometry("1445x400+05+30")
        self.rt.configure(background="#ffffcc")
        self.l1 = Label(self.rt)
        self.l1.place(relx=0.01, rely=0.0, height=220, width=220)
        img1 = ImageTk.PhotoImage(Image.open("bank_images/stat.jpg"))
        self.l1.configure(image=img1)
        self.id = uname
        self.l12 = Label(self.rt)
        self.l12.place(relx=0.35, rely=0.0, height=57, width=479)
        img12 = ImageTk.PhotoImage(Image.open("bank_images/acst.gif"))
        self.l12.configure(image=img12)

        self.l13 = Label(self.rt)
        self.l13.place(relx=0.8, rely=0.0, height=220, width=250)
        img13 = ImageTk.PhotoImage(Image.open("bank_images/act.jpg"))
        self.l13.configure(image=img13)

        self.Label2 = Label(self.rt)
        self.Label2.place(relx=0.35, rely=0.30, height=31, width=169)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''ENTER ACCOUNT NUMBER''')
        self.Label2.configure(width=178,background="#ff66ff")

        self.Entry1 = Entry(self.rt)
        self.Entry1.place(relx=0.56, rely=0.30, height=31, width=178)
        self.Entry1.configure(font="TkFixedFont",background="#ebebe0")
        self.Entry1.insert(0,"#10000")
        self.Entry1.configure(state="normal")

        self.Button1 = Button(self.rt, command=self.check)  #
        img10 = ImageTk.PhotoImage(Image.open("bank_images/clhe.gif"))
        self.Button1.place(relx=0.43, rely=0.70, height=60, width=206)
        self.Button1.configure(image=img10)

        self.fr = Frame(self.rt)
        self.fr.place(relx=0.05, rely=0.3, relheight=0.65, relwidth=0.2)
        self.fr.configure(relief=FLAT)
        self.fr.configure(borderwidth="2")
        self.fr.configure(relief=GROOVE)
        self.fr.configure(background="#c2c2d6")
        self.fr.configure(width=530)

        self.fr.place_forget()

        self.ta=Text(self.fr)
        self.ta.place(relx=0.0, rely=0.0, relheight=0.999, relwidth=0.999)

        self.l1=Label(self.ta)
        self.l1.configure(text="Transaction Id")
        self.l1.place(relx=0.01, rely=0.01, height=30, width=80)

        self.l2 = Label(self.ta)
        self.l2.configure(text="Source Account")
        self.l2.place(relx=0.13, rely=0.01, height=30, width=86)

        self.l3 = Label(self.ta)
        self.l3.configure(text="Destination Account")
        self.l3.place(relx=0.25, rely=0.01, height=30, width=120)

        self.l4 = Label(self.ta)
        self.l4.configure(text="Transaction Type")
        self.l4.place(relx=0.42, rely=0.01, height=30, width=100)

        self.l5 = Label(self.ta)
        self.l5.configure(text="Transaction Amount")
        self.l5.place(relx=0.56, rely=0.01, height=30, width=120)

        self.l6 = Label(self.ta)
        self.l6.configure(text="Transaction Date")
        self.l6.place(relx=0.73, rely=0.01, height=30, width=95)

        self.l7 = Label(self.ta)
        self.l7.configure(text="Transaction Time")
        self.l7.place(relx=0.87, rely=0.01, height=30, width=100)

        #self.tv=Treeview(self.ta)
        #self.tv.pack()
       # self.tv.insert("","0","i1",text=self.)



        self.Button1 = Button(self.fr, command=self.close)  #
        img105 = ImageTk.PhotoImage(Image.open("bank_images/close.gif"))
        self.Button1.place(relx=0.37, rely=0.86, height=60, width=110)
        self.Button1.configure(image=img105)


        self.rt.mainloop()

    def check(self):
        con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
        cursor = con.cursor()
        aid = self.Entry1.get()
        cursor.execute("select * from tbtransacc where trans_src_acc=%s", (aid))
        con.commit()
        rows = cursor.rowcount
        #print(rows)
        if rows > 0:
            #row = cursor.fetchone()
            #self.Label4.configure(text=row[0])
            #self.secans = row[1]
            self.Entry1.config(state='disabled')
            self.fr.place(relx=0.22, rely=0.38, relheight=0.6, relwidth=0.65)
            #self.ta.place(relx=0.0, rely=0.0, relheight=0.999, relwidth=0.999)
            #print(row)
            msg = ""
            # i=0
            # r=self.cursor.fetchone()
            #print(r)

            for i in cursor:
                #sys.stdout.write("\n")
                #sys.stdout.write("\n")
                self.ta.insert("1.0", "\n")
                #self.ta.insert("2.0", "\n")

                msg = msg +"     "+str(i[0]) + '\t' +"          "+ str(i[1]) +"         " + '\t' + "  " + str(i[2])+""+ '\t'+"         " + str(i[3])+"" +'\t'+"        "+ str(i[4])+"      "+ '\t'+"     "+str(i[5])+"   "+ '\t'+"  "+str(i[6]) + '\n'+'\n'
                #self.ta.insert("4.0", msg)
                #self.tv.pack()
                #self.tv.insert("", "0", "i2", text=str(i[0]))
            #print(msg)
            #self.ta.insert(".0", "\n")
            self.ta.insert("3.0", msg)

            self.ta.configure(state="disabled")


        else:
            messagebox.showinfo('Info', 'Invalid Account Number')
            self.Entry1.delete(0, END)
    def close(self):

        self.rt.destroy()
        o1=After_new.Menu_Class(self.id)


#ob = mini_stat(100)