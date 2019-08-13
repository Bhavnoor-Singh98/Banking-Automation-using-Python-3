from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import Open
import View_new
import Search
import Delete
import Login_new
import Modify
import Withdraw
import Deposit
import Transfer
import Mini
import About_us
import Edit_prof
import Password_ch
import Ad_sec

class Menu_Class:
    def __init__(self,id):
        self.rt=Tk()
        self.rt.title("Main Window")
        self.admid=id
        self.mb=Menu(self.rt)
        self.rt.configure(menu=self.mb)
        self.rt.option_add("*tearOff",False)
        self.rt.geometry("1145x500+160+100")

        self.lab = Label(self.rt)
        self.lab.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)# )
        img12 = ImageTk.PhotoImage(Image.open("bank_images/main2.jpg"))
        self.lab.configure(image=img12)
        self.m1=Menu(self.mb)
        self.m2=Menu(self.mb)
        self.m3=Menu(self.mb)
        self.m4=Menu(self.mb)


        #self.l1.configure()
        #i1 = ImageTk.PhotoImage(Image.open("d:\\va.jpg"))
        #self.Label1 = Label(self.root, image=i1)
        #self.Label1.place(relx=0.0, rely=0.0, width=250, height=180)

        self.mb.add_cascade(menu=self.m1,label="Account")
        self.mb.add_cascade(menu=self.m2, label="Transaction")
        self.mb.add_cascade(menu=self.m3, label="Admin")
        self.mb.add_cascade(menu=self.m4, label="Help")


        self.m1.add_command(label="Open New Account",command=self.open)#
        self.m1.add_command(label="Modify Account",command=self.modify)#,command=self.modify
        self.m1.add_command(label="Delete Account",command=self.delete)#,command=self.delete
        self.m1.add_command(label="View All Account",command=self.view)#,command=self.view
        self.m1.add_command(label="Search",command=self.search)#,command=self.search

        self.m2.add_command(label="Withdraw",command=self.withdraw)#
        self.m2.add_command(label="Deposit",command=self.deposit)#
        self.m2.add_command(label="Transfer",command=self.transfer)#
        self.m2.add_command(label="Mini Statement",command=self.mini)#

        self.m3.add_command(label="Edit Profile",command=self.prof)
        self.m3.add_command(label="Edit Password",command=self.passd)
        self.m3.add_command(label="Edit Security Settings",command=self.sec)
        self.m3.add_separator()
        self.m3.add_command(label="Logout",command=self.log_out)

        self.m4.add_command(label="About Us",command=self.aboutus)

        self.rt.mainloop()
    def open(self):
        self.rt.destroy()
        o1=Open.openi_acc(self.admid)

    def modify(self):
        self.rt.destroy()
        o2 = Modify.mod_acc(self.admid)
    def delete(self):
        self.rt.destroy()
        o3=Delete.del_acc(self.admid)
    def view(self):
        self.rt.destroy()
        o4=View_new.ViewAllAccount(self.admid)
    def search(self):
        self.rt.destroy()
        o5=Search.search_acc(self.admid)
    def withdraw(self):
        self.rt.destroy()
        o6=Withdraw.with_acc(self.admid)
    def deposit(self):
        self.rt.destroy()
        o7=Deposit.depo_acc(self.admid)
    def transfer(self):
        self.rt.destroy()
        o8=Transfer.trans_acc(self.admid)
    def mini(self):
        self.rt.destroy()
        o9=Mini.mini_stat(self.admid)
    def log_out(self):
        messagebox.showinfo("Warning","Logout")
        self.rt.destroy()
        o10 = Login_new.Login_Class()
    def aboutus(self):
        self.rt.destroy()
        o11=About_us.about_us(self.admid)

    def prof(self):
        self.rt.destroy()
        o12=Edit_prof.EditPrf(self.admid)

    def passd(self):
        self.rt.destroy()
        o13=Password_ch.Password(self.admid)

    def sec(self):
        self.rt.destroy()
        o14=Ad_sec.Security(self.admid)


#object=Menu_Class()