from tkinter import *
from PIL import Image, ImageTk
import After_new

class about_us:
    def __init__(self,uname):
        self.root1 = Tk()
        self.root1.geometry("1145x900+160+5")
        self.root1.title('Banking Solutions')
        # self.root1.resizable(False,False)
        self.root1.configure(background="#ffffcc")
        self.id = uname
        i1 = ImageTk.PhotoImage(Image.open("bank_images/crb.jpg"))
        self.Label1 = Label(self.root1, image=i1)
        self.Label1.place(relx=0.01, rely=0.0, width=310, height=160)

        i2 =ImageTk.PhotoImage(Image.open("bank_images/auh.jpg"))
        self.Label2 = Label(self.root1,image = i2)
        self.Label2.place(relx = 0.79,rely = 0.0, width = 270, height = 162)

        i3 = ImageTk.PhotoImage(Image.open("bank_images/cbh2.png"))
        self.Label3 = Label(self.root1, image=i3)
        self.Label3.place(relx=0.34, rely=0.0, width=470, height=265)

        self.Text1 = Text(self.root1, width=100, height=15, wrap='word')

        self.Text1.place(relx=0.3, rely=0.44) #replace file
        self.Text1.insert('1.0', '''This project has been developed by BHAVNOOR SINGH under the supreme guidance of Er. PUNEET AGGARWAL.
Core (centralized online real-time exchange) banking is a banking service provided by a group of networked bank branches
where customers may access their bank account and perform basic transactions from any of the member branch offices.
A Core banking system(CBS) is defined as a back-end system that processes daily banking transactions, and posts updates
to accounts and other financial records. It is called core because it is a central to the business of the bank.
A core banking system, when implemented well, ensures accurate and error-free delivery
of financial services to customers regardless of where he maintains his account,thus adding to the
banks' efficiency and performance.Thus CBS is a step towards enhancing customer convenience through anywhere and anytime Banking.

Minimum Software Requirements:

1. Operation System : Windows
2. Language : PYTHON 3.6
3. Front End: PyCharm IDE
4. Back End: MySQL Server 5.0''')
        self.Text1.config(state='disabled', font=('Times New Roman', '12', 'italic'), background="#d2a679")

        self.Text2 = Text(self.root1, width=40, height=15, wrap='word')

        self.Text2.place(relx=0.01, rely=0.44)  # replace file
        self.Text2.insert('1.0', '''CONTACT DETAILS:-

        1.MOBILE NO.- +919877308355
        2.E-MAIL- bhav27noor@gmail.com
        3.ADDRESS- 90, Waryam Villa,Ferozepur
        4.POSTAL ADDRESS- 152001
        ''')
        self.Text2.config(state='disabled', font=('Times New Roman', '12', 'italic'), background="#d2a679")



        self.b = Button(self.root1, command=self.back)
        self.b.place(relx=0.47, rely=0.88, width=118, height=68)
        i4 = ImageTk.PhotoImage(Image.open("bank_images/close.gif"))
        self.b.configure(image=i4)

        self.root1.mainloop()
    def back(self):
        self.root1.destroy()
        zx=After_new.Menu_Class(self.id)


#obj = about_us()