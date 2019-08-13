from tkinter import *
import pymysql.cursors
from PIL import Image, ImageTk
from tkinter import messagebox
import Login_new
class Forgot_Class:
    def __init__(self):
        self.top = Tk()
        self.top.geometry("1145x500+160+100")
        self.top.title("YOUR BANKING SOLUTIONS")
        self.top.configure(background="#ccffcc")

        self.Label1 = Label(self.top)
        self.Label1.place(relx=0.25, rely=0.0, height=66, width=650)
        self.Label1.configure(background="#ccffcc")
        img1 = ImageTk.PhotoImage(Image.open("bank_images/Forgot.gif"))
        self.Label1.configure(image=img1)

        self.Label2 = Label(self.top)
        self.Label2.place(relx=0.2, rely=0.40, height=51, width=290) #relx=0.2, rely=0.40, height=31, width=270
        #self.Label2.configure(background="#ccffcc")
        imge = ImageTk.PhotoImage(Image.open("bank_images/adid.gif"))
        self.Label2.configure(image=imge,background="#ccffcc")
        self.Label2.configure(width=169)

        self.Entry1 = Entry(self.top)
        self.Entry1.place(relx=0.53, rely=0.40, height=45, width=255)
        self.Entry1.insert(0,"#78961")
        self.Entry1.configure(state="readonly")
        self.Entry1.configure(state="normal")
        self.Entry1.configure(background="white",font='Helvetica')#, fontsize="15"

        self.Button1 = Button(self.top, command=self.check)
        self.Button1.place(relx=0.4, rely=0.55, height=63, width=190)
        im = ImageTk.PhotoImage(Image.open("bank_images/ch.gif"))
        self.Button1.configure(image=im)#,background="#ccffcc"
        #self.Button1.configure(width=156)

        self.Frame1 = Frame(self.top)
        self.Frame1.place(relx=0.05, rely=0.3, relheight=0.65, relwidth=0.2)
        self.Frame1.configure(relief=FLAT)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#999966")
        self.Frame1.configure(width=530)

        self.Frame1.place_forget()#make it disaapear

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.01, rely=0.00, height=42, width=270)
        #background = "#ccffcc"
        iml = ImageTk.PhotoImage(Image.open("bank_images/sec.gif"))
        self.Label3.configure(image=iml,background="#999966")

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.51, rely=0.00, height=42, width=270)
        #self.Label4.configure(background="#ccffcc")
        iml1 = ImageTk.PhotoImage(Image.open("bank_images/d.gif"))
        self.Label4.configure( background="#999966",image=iml1)

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.01, rely=0.24, height=42, width=330)
        #self.Label5.configure(background="#ccffcc")
        iml5 = ImageTk.PhotoImage(Image.open("bank_images/ans.gif"))
        self.Label5.configure(background="#999966",image=iml5)

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.68, rely=0.24, height=40, width=160)
        self.Entry2.configure(background="white")
        #self.Entry2.insert(0,"DD/MM/YYYY")
        #self.Entry2.configure(state="readonly")
        self.Entry2.configure(state="normal")

        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.08, rely=0.39, relheight=0.8, relwidth=0.9)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#cccccc")
        self.Frame2.configure(width=475)
        self.Frame2.place_forget()

        self.Label6 = Label(self.Frame2)
        self.Label6.place(relx=0.04, rely=0.1, height=20, width=134)
        #self.Label6.configure(background="#ccffcc")
        imlng = ImageTk.PhotoImage(Image.open("bank_images/ep.gif"))
        self.Label6.configure(image=imlng)

        self.Label7 = Label(self.Frame2)
        self.Label7.place(relx=0.039, rely=0.35, height=20, width=155)
        #self.Label7.configure(background="#ccffcc")
        imlng1 = ImageTk.PhotoImage(Image.open("bank_images/cf.gif"))
        self.Label7.configure(image=imlng1)


        self.Entry3 = Entry(self.Frame2, show="*")
        self.Entry3.place(relx=0.46, rely=0.1, height=25, relwidth=0.35)
        self.Entry3.configure(background="white")
        self.Entry3.insert(0, "#*****")
        self.Entry3.configure(state="readonly")
        self.Entry3.configure(state="normal")


        self.Entry4 = Entry(self.Frame2, show="*")
        self.Entry4.place(relx=0.46, rely=0.29, height=25, relwidth=0.35)
        self.Entry4.configure(background="white")
        self.Entry4.insert(0, "#*****")
        self.Entry4.configure(state="readonly")
        self.Entry4.configure(state="normal")

        self.Button3 = Button(self.Frame2, command=self.reset)
        self.Button3.place(relx=0.3, rely=0.64, height=45, width=200)
        imlng2 = ImageTk.PhotoImage(Image.open("bank_images/re.gif"))
        self.Button3.configure(image=imlng2)#,background="#cccccc"
        #self.Button3.configure(width=157)

        self.Button2 = Button(self.Frame1, command=self.verify)
        self.Button2.place(relx=0.39, rely=0.65, height=55.35, width=157.2)
        ime = ImageTk.PhotoImage(Image.open("bank_images/ver1.gif"))
        self.Button2.configure(image=ime)
        #self.Button2.configure(width=157)
        self.top.mainloop()

    def verify(self):
        usrans = self.Entry2.get()
        if (usrans == self.secans):
            self.Frame2.place(relx=0.06, rely=0.39, relheight=0.59, relwidth=0.9)
            self.Entry2.config(state='disabled')
            self.Button2.destroy()
        else:
            messagebox.showinfo('Info', 'Invalid Security Answer')

    def reset(self):
        pwd = self.Entry3.get()
        cpwd = self.Entry4.get()
        if (pwd == cpwd):
            con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
            cursor = con.cursor()
            aid = self.Entry1.get()
            cursor.execute("update tbadmin set admin_pass=%s where admin_id=%s", (pwd, aid))
            con.commit()
            messagebox.showinfo('Info', 'Password updated successfully')
            self.top.destroy()
            obj1 = Login_new.Login_Class()
        else:
            messagebox.showinfo('Info', 'Password and Confirm Password should match')
            self.Entry3.delete(0, END)
            self.Entry4.delete(0, END)

    def check(self):
        con = pymysql.connect(host='localhost', user='root', password='noor#123', db='dbbank')
        cursor = con.cursor()
        aid = self.Entry1.get()
        cursor.execute("select adsecques, adsecans from tbadmin where admin_id=%s", (aid))
        con.commit()
        rows = cursor.rowcount
        if rows > 0:
            row = cursor.fetchone()
            self.Label4.configure(text=row[0])
            self.secans = row[1]
            self.Entry1.config(state='disabled')
            self.Frame1.place(relx=0.22, rely=0.3, relheight=0.65, relwidth=0.65)

        else:
            messagebox.showinfo('Info', 'Invalid ID')
            self.Entry1.delete(0, END)


#obj = Forgot_Class()