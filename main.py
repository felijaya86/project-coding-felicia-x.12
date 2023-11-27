from tkinter import*
import tkinter.font
root = Tk()
root.geometry("300x600")
changefont = tkinter.font.Font(size = 20)
jadi = Label(root, text = "REGISTER", font = changefont)
jadi.place(x = 30, y = 10)
Labelfr = LabelFrame(root, text = "result", padx = 20, pady = 20)
Labelfr.place(x = 60, y = 380)

nama = Label(root,text = "first name")
nama2 = Label(root,text = "last name")
age = Label(root,text = "age")
ussername = Label(root,text = "ussername")
email = Label(root,text = "email")
password = Label(root,text = "password")
gender = Label(root,text = "gender")

e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root)
e4 = Entry(root,width=40)
e5 = Entry(root,width=40)
e6 = Entry(root,width=40)

nama.place ( x = 20 , y = 50 )
nama2.place ( x = 20 , y = 90)
age.place ( x = 20 , y = 130)
ussername.place ( x = 20 , y = 170 )
email.place ( x = 20 , y = 210 )
password.place ( x = 20 , y = 250)
gender.place ( x = 20 , y = 290 )

e1.place( x = 20 , y = 70 )
e2.place( x = 20 , y = 110 )
e3.place( x = 20 , y = 150 )
e4.place( x = 20 , y = 190 )
e5.place( x = 20 , y = 230 )
e6.place( x = 20 , y = 270 )

r = StringVar()
rb = Radiobutton(root, text = " female ", variable = r , value = "female").place(x = 20, y = 310)
rb2 = Radiobutton(root, text = " male ", variable = r , value = "male").place(x = 80, y = 310)
def cetak():
    class orang:
        def __init__(self, nama, nama2, age, ussername, email, password, gender):
           self.nama = nama
           self.nama2 = nama2
           self.age = age
           self.ussername = ussername
           self.email = email
           self.password = password
           self.gender = gender
        def hasil(self):
           ibl = Label(Labelfr , text = "first name = " + self.nama + "\nlast name = " + self.nama2 + "\n age = " + self.age + "\n ussername = " + self.ussername + "\n email = " + self.email + "\n password = " + self.password + "\n gender = " + self.gender)
    ditampilkan = orang(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), r.get())
    ditampilkan.hasil()

btn = Button(root, text = "submit", command = cetak ).place(x = 100, y = 350)
root.mainloop()