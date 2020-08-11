from tkinter import *
from tkinter import ttk
import pymysql
from tkinter  import messagebox
class Student:
    def __init__(self,root):
#--------------------------variables of the connecting the database----------------------------
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()



        self.root=root
        self.root.title("student management system")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Student management system",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
#-------------------manage frame----------------
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=560)
#------------------------------detail frame-----------------------

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=750, height=560)
#---------------------------tite manage student----------------------
        M_title=Label(Manage_Frame,text="manage student",bg="crimson",fg="white",font=("times new roman",30,"bold"),relief=GROOVE)
        M_title.grid(row=0,columnspan=2,pady=20)
#-------------------roll no label--------------------------
        lbl_roll = Label(Manage_Frame, text="Roll No",bg="crimson", fg="white",font=("times new roman",15, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky="w")

        txt_roll = Entry(Manage_Frame, bg="white", textvariable=self.Roll_No_var,font=("times new roman", 15, "bold"))
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")
#-------------------------------name label----------------------------
        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(Manage_Frame, bg="white", textvariable=self.name_var,font=("times new roman", 15, "bold"))
        txt_roll.grid(row=2, column=1, pady=10, padx=20, sticky="w")
#----------------------------------email label----------------------------
        lbl_email = Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame, textvariable=self.email_var,bg="white", font=("times new roman", 15, "bold",),relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")
#------------------------------for gender----------------------------------
        lbl_gender = Label(Manage_Frame,text="Gender", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",15,"bold"))
        combo_gender['values']=("male","female","others")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        #-----------------------------contact of the student--------------------------------
        lbl_contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var,bg="white", font=("times new roman", 15, "bold",), relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")
#-------------------------------dob of the student---------------------------------
        lbl_dob = Label(Manage_Frame, text="DOB", bg="crimson", fg="white",font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_Frame, bg="white",textvariable=self.dob_var ,font=("times new roman", 15, "bold",), relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        #-----------------------label for address of the student------------------------------
        lbl_adress = Label(Manage_Frame, text="Adress", bg="crimson", fg="white",font=("times new roman", 20, "bold"))
        lbl_adress.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_adress = Text(Manage_Frame, width=30,height=2,bg="white", font=("",10 , "",), relief=GROOVE)
        self.txt_adress.grid(row=7, column=1, pady=10, padx=20, sticky="w")

#----------------------------button frame-------------------------------------------
        btn_frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="yellow")
        btn_frame.place(x=15,y=500,width=420)

        adddbtn=Button(btn_frame,command=self.add_students,text="Add",width=10).grid(row=0,column=1,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="update",command=self.update_data,width=10).grid(row=0,column=2,padx=10,pady=10)
        deletebtn=Button(btn_frame,text="delete",command=self.delete_data,width=10).grid(row=0,column=3,padx=10,pady=10)
        clearbtn=Button(btn_frame,command=self.clear,text="clear",width=10).grid(row=0,column=4,padx=10,pady=10)
#------------------------work on the detail frame-------------------------------
        lbl_search = Label(Detail_Frame, text="search by", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by,font=("times new roman", 10, "bold"))
        combo_search['values'] = ("Roll_no      "
                                  "", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt,bg="white", font=("times new roman", 10, "bold",), relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")



        searchbtn = Button(Detail_Frame, text="search",command=self.search_data, width=10).grid(row=0, column=3, padx=20, pady=10)
        showbtn = Button(Detail_Frame, text="show all",command=self.fetch_data, width=10).grid(row=0, column=4, padx=20, pady=10)

#-------------------------------table frame in detail frame---------------------------------
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="white")
        Table_Frame.place(x=20, y=100, width=700, height=400)

        scrol_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scrol_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)
        scrol_x.pack(fill=X,side=BOTTOM)
        scrol_y.pack(fill=Y,side=RIGHT)

        scrol_x.config(command=self.student_table.xview)
        scrol_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("address", text="Address")

        self.student_table['show']='headings'
        self.student_table.column("roll",width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_students(self):
            if self.Roll_No_var.get()=="" or self.email_var.get()=="":
                    messagebox.showerror("error","please enter the data")

            else:
                    con = pymysql.connect(host="localhost", user="root", password="123456", database="stm")
                    cur = con.cursor()
                    cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                                      self.name_var.get(),
                                                                                      self.email_var.get(),
                                                                                      self.gender_var.get(),
                                                                                      self.contact_var.get(),
                                                                                      self.dob_var.get(),
                                                                                      self.txt_adress.get('1.0', END)
                                                                                      ))
                    con.commit()
                    self.fetch_data()
                    con.close()
                    messagebox.showinfo("succesful","your data has been succesfully inserted")
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="123456", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                        self.student_table.insert('',END,values=row)
                con.commit()
        con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_adress.delete('1.0',END)
    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_adress.delete("1.0",END)
        self.txt_adress.insert(END,row[6])
    def update_data(self):
            con = pymysql.connect(host="localhost", user="root", password="123456", database="stm")
            cur = con.cursor()
            cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(self.name_var.get(),
                                                                                                                         self.email_var.get(),
                                                                                                                         self.gender_var.get(),
                                                                                                                         self.contact_var.get(),
                                                                                                                         self.dob_var.get(),
                                                                                                                         self.txt_adress.get('1.0',END),
                                                                                                                         self.Roll_No_var.get()
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("update succesfull","your data has been updated suusefully")
    def delete_data(self):
            con = pymysql.connect(host="localhost", user="root", password="123456", database="stm")
            cur = con.cursor()
            cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("deleted succesfull", "your data has been deleted suusefully")

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="123456", database="stm")
        cur = con.cursor()
        cur.execute("select * from students where"+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                        self.student_table.insert('',END,values=row)
                con.commit()
        con.close()


root=Tk()
ob=Student(root)
root.mainloop()