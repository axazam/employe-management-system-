from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import random

root = Tk()


class Mainwindow:
    def __init__(self):
        self.root = root

        self.root.title("Employee management system")
        self.root.geometry("1530x790+0+0")
        self.frame = Frame(self.root, bg="#dc143c", relief=FLAT)
        self.frame.place(x=0, y=0, width=1520, height=100)

        self.heading_image = PhotoImage(file='image/employe.png')
        self.heading_label = Label(self.frame, text="Employe Management System", fg='White', bg="#DC143C",
                                   font=('times new roman', 35, 'bold'))
        self.heading_label.place(x=0, y=0, width=1000)
        self.heading_label.config(image=self.heading_image, compound=LEFT, width=100, height=100)

        self.frame1 = Frame(self.root, bg='#B0C4DE', relief=FLAT)
        self.frame1.place(x=10, y=110, width=1090, height=330)

        self.label = Label(self.frame1, text="manage employess", font=("times new roman", 22, "bold"), bg="black",
                           fg="white")
        self.label.place(x=0, y=0, width=1090)

        self.fname = Label(self.frame1, text="First name", font=("times new roman", 20, "bold"), bg="#B0C4DE",
                           fg="black")
        self.fname.place(x=30, y=50)

        self.fentry = Entry(self.frame1, font=("times new roman", 20, "bold"), relief=RIDGE)
        self.fentry.place(x=30, y=90, width=250)

        self.lname = Label(self.frame1, text="Last name", font=("times new roman", 20, "bold"), fg="black",
                           bg="#B0C4DE")
        self.lname.place(x=320, y=50)

        self.lentry = Entry(self.frame1, font=("times new roman", 20, "bold"), relief=RIDGE)
        self.lentry.place(x=320, y=90)

        self.post_label = Label(self.frame1, text="Post", font=("times new roman", 20, "bold"), fg="black",
                                bg="#B0C4DE")
        self.post_label.place(x=610, y=50)

        i = ['Software Developer', 'Web Designer', 'Project Leader']
        self.class_combo = ttk.Combobox(self.frame1, values=i, font=("times new roman", 18, "bold"))
        self.class_combo.place(x=610, y=90, width=250)
        self.class_combo.config(state='readonly')
        self.class_combo.set(" select post ")

        self.empno = Label(self.frame1, text="ID NO", font=("times new roman", 20, "bold"), bg="#B0C4DE", fg="black")
        self.empno.place(x=30, y=130)

        self.empno_entry = Entry(self.frame1, font=("times new roman", 18, "bold"), relief=RIDGE)
        self.empno_entry.place(x=30, y=170, width=250)

        self.h_label = Label(self.frame1, text=" ", font=("times new roman", 10, "bold"), bg="#B0C4DE", fg="black")
        self.h_label.place(x=30, y=200)

        self.empno_entry.bind("<Enter>", self.hover)
        self.empno_entry.bind("<Leave>", self.hover_leave)

        self.h_label = Label(self.frame1, text=" ", font=("times new roman", 12, "bold"), bg="#B0C4DE", fg="red")
        self.h_label.place(x=30, y=200)

        self.age = Label(self.frame1, text="Age", font=("times new roman", 20, "bold"), bg="#B0C4DE", fg="black")
        self.age.place(x=320, y=130)

        self.age_entry = Entry(self.frame1, font=("times new roman", 20, "bold"), relief=RIDGE)
        self.age_entry.place(x=320, y=170, width=250)

        self.salary = Label(self.frame1, text="Salary", font=("times new roman", 20, "bold"), bg="#B0C4DE", fg="black")
        self.salary.place(x=610, y=130)

        self.salary_entry = Entry(self.frame1, font=("times new roman", 20, "bold"), relief=RIDGE)
        self.salary_entry.place(x=610, y=170, width=250)

        self.addbutton = Button(self.frame1, text="ADD", font=("times new roman", 15, 'bold'), fg='black', bg='#7FFFD4',bd=4, relief=GROOVE,command=self.addemploye)
        self.addbutton.place(x=890, y=80, width=190)

        self.updatebutton = Button(self.frame1, text="UPDATE", font=("times new roman", 15, 'bold'), fg='black',bg='#7FFFD4', bd=4, relief=GROOVE,command=self.update_employe)
        self.updatebutton.place(x=890, y=140, width=190)

        self.DELETEbutton = Button(self.frame1, text="DELETE", font=("times new roman", 15, 'bold'), fg='black',bg='#7FFFD4', bd=4, relief=GROOVE,command=self.delete_employe)
        self.DELETEbutton.place(x=890, y=200, width=190)

        self.CLEARbutton = Button(self.frame1, text="CLEAR", font=("times new roman", 15, 'bold'), fg='black',bg='#7FFFD4', bd=4, relief=GROOVE,command=self.clear)
        self.CLEARbutton.place(x=890, y=260, width=190)

        self.frame2 = Frame(self.root, relief=FLAT, bg="white")
        self.frame2.place(x=1110, y=110, width=410, height=330)

        self.employe_image = PhotoImage(file='image/men employe.png',width=762,height=512)
        self.emplabel = Label(self.frame2, image=self.employe_image)
        self.emplabel.pack()

        self.frame3=Frame(self.root,relief=FLAT,bg="#b0c4de")
        self.frame3.place(x=10,y=450,width=1510,height=330)

        self.subf=Frame(self.frame3,relief=FLAT,bg="white")
        self.subf.place(x=5,y=5,width=1495,height=55)


        self.search_by=Label(self.subf,text="Search By",font=("times new roman",20,"bold"),fg='black',bg='white')
        self.search_by.place(x=20,y=10)

        j=['ID No','First_Name','Age']
        self.scombo=ttk.Combobox(self.subf,value=j,font=("times new roman",18,"bold"))
        self.scombo.place(x=150,y=10,width=200)
        self.scombo.set("Select Option")

        self.scombo.config(state='readonly')

        self.search_entry=Entry(self.subf,font=("times new roman",18,"bold"),relief=RIDGE,bg="#F5F5DC")
        self.search_entry.place(x=390,y=10,width=300)

        self.search_button=Button(self.subf,text="Search",font=("times new roman",15,"bold"),relief=GROOVE,bd=4,fg="black",bg="#7FFFD4",command=self.search)
        self.search_button.place(x=790,y=5,width=200)

        self.show_button=Button(self.subf,text="Show All",font=("times new roman",15,"bold"),relief=GROOVE,bd=4,fg="black",bg="#7FFFD4",command=self.showall)
        self.show_button.place(x=1000,y=5,width=200)

        self.scroll_x=ttk.Scrollbar(self.frame3,orient=VERTICAL)
        self.scroll_y=ttk.Scrollbar(self.frame3, orient=HORIZONTAL)
        self.treeview=ttk.Treeview(self.frame3,columns=(1,2,3,4,5,6),show="headings",height=11,xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=RIGHT,fill=Y)
        self.scroll_y.pack(side=BOTTOM,fill=X)

        self.treeview.heading(1,text="First Name")
        self.treeview.heading(2, text="Last Name")
        self.treeview.heading(3, text="Post")
        self.treeview.heading(4, text="ID NO")
        self.treeview.heading(5, text="AGE")
        self.treeview.heading(6, text="SALARY")

        self.treeview.column(1,width=100,anchor=CENTER)
        self.treeview.column(2, width=120, anchor=CENTER)
        self.treeview.column(3, width=120, anchor=CENTER)
        self.treeview.column(4, width=100, anchor=CENTER)
        self.treeview.column(5, width=120, anchor=CENTER)
        self.treeview.column(6, width=140, anchor=CENTER)

        self.treeview.place(x=5,y=65,width=1250)
        self.tree()
        self.treeview.bind("<ButtonRelease-1>",self.click_insert)


    def hover(self, event):
        self.h_label.config(text="* Do not enter for new registration")

    def hover_leave(self, event):
        self.h_label.config(text='')

    def addemploye(self):
        if self.fentry.get()=="":
            messagebox.showerror("Error","All fields Are required")
        elif self.lentry.get()=="":
            messagebox.showerror("Error","All fields Are required")
        elif self.class_combo.get()=="Select post":
            messagebox.showerror("Error","All fields Are required")
        elif self.age_entry.get()=="":
            messagebox.showerror("Error","All fields Are required")
        elif self.salary_entry.get()=="":
            messagebox.showerror("Error","All fields Are required")

        else:
            self.Idno=random.randrange(10000,90000)
            print(self.Idno)
            con=pymysql.connect(host='localhost',user='root',password='aksa1234',db='aksa')
            cur=con.cursor()
            cur.execute("insert into employe(First_Name,Last_Name,Post,ID_No,Age,Salary)values('%s','%s','%s','%s','%s','%s')"%(self.fentry.get(),self.lentry.get(),self.class_combo.get(),self.Idno,self.age_entry.get(),self.salary_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","employe added successfully")

    def update_employe(self):
        if self.fentry.get()=="":
            messagebox.showerror("Error","All fields Are required")
        elif self.lentry.get()=="":
            messagebox.showerror("Error","All fields Are required")
        elif self.class_combo.get()=="Select post":
            messagebox.showerror("Error","All fields Are required")
        elif self.age_entry.get()=="":
            messagebox.showerror("Error","All fields Are required")
        elif self.salary_entry.get()=="":
            messagebox.showerror("Error","All fields Are required")
        else:
            con = pymysql.connect(host='localhost', user='root', password='aksa1234', db='aksa')
            cur = con.cursor()
            cur.execute("update employe set First_Name=%s,Last_Name=%s,Post=%s,Age=%s,Salary=%s where ID_No=%s",(self.fentry.get(),self.lentry.get(),self.class_combo.get(),self.age_entry.get(),self.salary_entry.get(),self.empno_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("success",'student update successfully')

    def delete_employe(self):
        if self.empno_entry.get()=='':
            messagebox.showerror("Error",'Please Enter ID No to delete Employe')
        else:
            con = pymysql.connect(host='localhost', user='root', password='aksa1234', db='aksa')
            cur = con.cursor()
            cur.execute("delete from employe where ID_No=%s",self.empno_entry.get())
            con.commit()
            con.close()
            messagebox.showinfo("success","Employe deleted successfully")

    def clear(self):
        self.fentry.delete(0,END)
        self.lentry.delete(0, END)
        self.class_combo.set("Select post")
        self.age_entry.delete(0, END)
        self.salary_entry.delete(0, END)
        self.empno_entry.delete(0, END)

    def tree(self):
        con = pymysql.connect(host='localhost', user='root', password='aksa1234', db='aksa')
        cur = con.cursor()
        cur.execute("select * from employe")
        self.row=cur.fetchall()
        if len(self.row)!=0:
            self.treeview.delete(*self.treeview.get_children())
            for i in self.row:
                self.treeview.insert('','end',values=i)
                con.commit()

    def click_insert(self,ev):
        self.clear()
        self.cur_row=self.treeview.focus()
        self.content=self.treeview.item(self.cur_row)
        self.info=self.content["values"]
        self.fentry.insert(0,self.info[0])
        self.lentry.insert(0, self.info[1])
        self.class_combo.set(self.info[2])
        self.empno_entry.insert(0, self.info[3])
        self.age_entry.insert(0, self.info[4])
        self.salary_entry.insert(0, self.info[5])

    def search(self):
        if self.scombo.get()=='ID No':
            con = pymysql.connect(host='localhost', user='root', password='aksa1234', db='aksa')
            cur = con.cursor()
            cur.execute("select * from employe where Id_No=%s",self.search_entry.get())
            self.row = cur.fetchall()
            if len(self.row) != 0:
                self.treeview.delete(*self.treeview.get_children())
                for i in self.row:
                    self.treeview.insert('', 'end', values=i)
                    con.commit()

        elif self.scombo.get()=='First_Name':
            con = pymysql.connect(host='localhost', user='root', password='aksa1234', db='aksa')
            cur = con.cursor()
            cur.execute("select * from employe where First_Name=%s", self.search_entry.get())
            self.row = cur.fetchall()
            if len(self.row) != 0:
                self.treeview.delete(*self.treeview.get_children())
                for i in self.row:
                    self.treeview.insert('', 'end', values=i)
                    con.commit()

        elif self.scombo.get() == 'Age':
            con = pymysql.connect(host='localhost', user='root', password='aksa1234', db='aksa')
            cur = con.cursor()
            cur.execute("select * from employe where Age=%s", self.search_entry.get())
            self.row = cur.fetchall()
            if len(self.row) != 0:
                self.treeview.delete(*self.treeview.get_children())
                for i in self.row:
                    self.treeview.insert('', 'end', values=i)
                    con.commit()

        else:
            messagebox.showerror("Error","Please select correct option")

    def showall(self):
        self.tree()




















m = Mainwindow()
root.mainloop()



