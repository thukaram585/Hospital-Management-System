import tkinter
import tkinter as Tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def main():
    win=Tk()
    app=login(win)
    win.mainloop()

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Sign Up")
        self.root.geometry("1350x700+0+0")
        #self.root.resizable(False,False)

        #bg
        self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\mainpage.png')
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.root,text="HOSPITAL MANAGEMENT SYSTEM", font=("helvetica", 35, "bold"), fg="black", bg="white").place(x=50, y=85,width=1140)

        dct_btn = Button(self.root, text="Doctor", font=("helvetica", 25, "bold"), fg="black", bg="white",
                            cursor='hand2',activebackground='darkblue',activeforeground='white',
                          command=self.home_dct).place(x=384, y=590,width=150,height=49)

        user_btn = Button( self.root,text="Patient", font=("helvetica", 25, "bold"), fg="black", bg="white",
                           cursor='hand2',activebackground='darkblue',activeforeground='white',
                           command=self.home_pat).place(x=573,y=590,width=150,height=49)

        adm_btn = Button( self.root,text="Admin", font=("helvetica", 25, "bold"), fg="black",
                            cursor='hand2',bg="white",activebackground='darkblue',activeforeground='white',
                          command=self.home_adm).place(x=760, y=590,width=150,height=49)

    def home_dct(self):
        self.new_window=Toplevel(self.root)
        self.app=doctor_login(self.new_window)

    def home_pat(self):
        self.new_window = Toplevel(self.root)
        self.app = user_login(self.new_window)

    def home_adm(self):
        self.new_window = Toplevel(self.root)
        self.app = admin_login(self.new_window)
###############################################################
###############################################################
#                                           2 page
###########################################################################################
class doctor_login:
    def __init__(self,root):
        self.root=root
        self.root.title("Sign Up")
        self.root.geometry("1350x700+0+0")
        #self.root.resizable(False,False)
        self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\d2.png')
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        title=Label(self.root,text="Doctor Login ",font=("Impact",33,"bold","underline"),fg="orange",bg="white")
        title.place(x=160,y=125)
        desc=Label(self.root,text="Doctor Login Area",font=("Goudy old style",16,"bold","underline"),fg="orange",bg="white").place(x=210,y=195)

        email=Label( self.root,text="Email", font=("times new roam", 20, "bold"), bg="white", fg="black").place(x=80, y=260)
        self.email= Entry(self.root, font=("times new roman", 15),bg="lightgray")
        self.email.place(x=80, y=305, width=350,height=40)

        password = Label(self.root,text="Password ", font=("times new roam", 20, "bold"), bg="white", fg="black").place(x=80, y=360)
        self.password= Entry(self.root,font=("times new roman", 15),bg="lightgray",show="*")
        self.password.place(x=80, y=405, width=350,height=40)

        forget_btn = Button(self.root,text="Forgot Password?",bg="white",fg="red",bd=0,font=("times new roman",13),
                            command=self.email_frgt).place(x=340,y=455)

        Login_btn = Button( self.root,text="Submit ", bg="white", fg="red",font=("times new roman", 20),cursor='hand2',
                           command=self.usr_fun,).place(x=230, y=503)

    ##########################################################
        ################################################################3
        home_btn = Button(self.root, text="Home", bg="#D7F2F2", fg="black", font=("times new roman", 17),
                          cursor='hand2', bd=2,command=self.new7_window).place(x=0, y=0, width=215)
        admin_btn = Button(self.root, text="Doctor", bg="#D7F2F2", fg="black", font=("times new roman", 17),
                           cursor='hand2', bd=2).place(x=215, y=0, width=215)
        doctor_btn = Button(self.root, text="Patient", bg="#D7F2F2", fg="black", font=("times new roman", 17),
                            cursor='hand2', bd=2,command=self.new9_window).place(x=430, y=0, width=215)
        patient_btn = Button(self.root, text="Admin", bg="#D7F2F2", fg="black", font=("times new roman", 17),
                             cursor='hand2', bd=2,command=self.new10_window).place(x=645, y=0, width=215)
        abt_btn = Button(self.root, text="Developed By", bg="#D7F2F2", fg="black", font=("times new roman", 17),
                         cursor='hand2', bd=2,command=self.pic_window).place(x=860, y=0, width=215)
        cnt_btn = Button(self.root, text="Back", bg="#D7F2F2", fg="black", font=("times new roman", 17),
                         cursor='hand2', bd=2,command=self.back_window).place(x=1075, y=0, width=215)


    def new7_window(self):
        self.root.destroy()

    # def new8_window(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = admin_login(self.new_window)

    def new9_window(self):
        self.new_window = Toplevel(self.root)
        self.app = user_login(self.new_window)

    def new10_window(self):
        self.new_window = Toplevel(self.root)
        self.app = admin_login(self.new_window)

    def pic_window(self):
        self.new_window = Toplevel(self.root)
        self.app = pic_page(self.new_window)

    def back_window(self):
        self.new_window = Toplevel(self.root)
        self.app = login(self.new_window)



    # def new11_window(self):
    #    self.new_window = Toplevel(self.root)
    #   self.app = (self.new_window)
    # def new12_window(self):
    #   self.new_window = Toplevel(self.root)
    #   self.app = frgt(self.new_window)

    def usr_fun(self):
        if self.email.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="project")
                cur = con.cursor()
                cur.execute("select * from dct_reg where email=%s and password=%s",(self.email.get(), self.password.get()))
                row = cur.fetchone()
                if row == None:
                        messagebox.showerror("Error", "Invalid username & password", parent=self.root)
                else:
                    open_main = messagebox.askyesno("Error", "Welcome yes to continue",parent=self.root)
                    if open_main > 0:
                        self.new_window = Toplevel(self.root)
                        self.app = dct_page(self.new_window)
                    else:
                        if not open_main:
                            return
                con.commit()
                con.close()
            except Exception as es:
                  messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)


# ###
#     def dct_window(self):
#         self.new_window = Toplevel(self.root)
#         self.app = dct_frgt(self.new_window)
#
# class dct_frgt:
#     def __init__(self,root):
#          #   self.root = Toplevel()
#             self.root=root
#             self.root.title("Forgot Password")
#             self.root.geometry("400x400+400+150")
#             self.root.focus_force()
#             self.root.grab_set()
#             self.root.config(bg="white")
#
#
#             Frame_login=Frame (self.root,bg="#E3E3E3")
#             Frame_login.place(x=12,y=20,height=350,width=376)
#
#             title = Label(self.root, text="  Forgot Password  ", font=("Goudy old style", 23 ,"bold","underline"), fg="black", bg="white")
#             title.place(x=82, y=30)
#
#             question = Label(self.root, text="Security question", font=("times new roam", 15, "bold"), bg="#E3E3E3",
#                          fg="black").place(x=20, y=100)
#             cmb_quest = ttk.Combobox(self.root, font=("times new roman", 15), state='readonly', justify=CENTER)
#             cmb_quest['value'] = ("Select", "Year of born", "Pet dog name", "Birth place","Favourite Actor")
#             cmb_quest.place(x=20, y=130, width=300)
#             cmb_quest.current(0)
#
#             ans = Label(self.root, text="Answer", font=("times new roam", 15, "bold"), bg="#E3E3E3",
#                          fg="black").place(x=20, y=180)
#             self.ans = Entry(self.root, font=("times new roman", 15), bg="white")
#             self.ans.place(x=20, y=210, width=300)
#
#             new_pass = Label(self.root, text="New password", font=("times new roam", 15, "bold"), bg="#E3E3E3",
#                          fg="black").place(x=20, y=260)
#
#             self.new_pass = Entry(self.root, font=("times new roman", 15), bg="white")
#             self.new_pass.place(x=20, y=290, width=300)
#
#             Login_btn = Button(self.root, text="Reset password", bg="white", fg="red", font=("times new roman", 17),cursor='hand2',
#                            command=self.frgt_dct,).place(x=120, y=340)
#
#     def frgt_dct(self):
#         if self.ans.get()=="" or self.new_pass.get()=="":
#              messagebox.showerror("Error","All fields are required",parent=self.root)
# ##################################
##

    def email_frgt(self):
        if self.email.get()=="":
            messagebox.showerror("Error","Enter email address to reset password",parent=self.root)
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="project")
            cur = con.cursor()
            query=("select * from dct_reg where email=%s")
            value=(self.email.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Enter the valid email-id",parent=self.root)
            else:
                con.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x400+400+150")
                self.root.config(bg="#EAEAEA")
                self.root2.focus_force()
                self.root2.grab_set()
                self.root2.config(bg="white")

                Frame_login = Frame(self.root2, bg="#E3E3E3",bd=5,relief=RIDGE)
                Frame_login.place(x=12, y=20, height=350, width=376)

                title = Label(self.root2, text="  Forgot Password  ", bd=2,relief=RIDGE,font=("Goudy old style", 23, "bold", "underline"),
                              fg="black", bg="#EAEAEA")
                title.place(x=82, y=30)

                question = Label(self.root2, text="Security question", font=("times new roam", 15, "bold"), bg="#E3E3E3",
                                 fg="black").place(x=20, y=100)
                self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 15), state='readonly', justify=CENTER)
                self.cmb_quest['value'] = ("Select", "Year of born", "Pet dog name", "Birth place", "Favourite Actor","Best friend name")
                self.cmb_quest.place(x=20, y=130, width=300)
                self.cmb_quest.current(0)

                ans = Label(self.root2, text="Answer", font=("times new roam", 15, "bold"), bg="#E3E3E3",
                            fg="black").place(x=20, y=180)
                self.ans = Entry(self.root2, font=("times new roman", 15), bg="white")
                self.ans.place(x=20, y=210, width=300)

                new_pass = Label(self.root2, text="New password", font=("times new roam", 15, "bold"), bg="#E3E3E3",
                                 fg="black").place(x=20, y=260)
                self.new_pass = Entry(self.root2, font=("times new roman", 15), bg="white")
                self.new_pass.place(x=20, y=290, width=300)

                Login_btn = Button(self.root2, text="Reset password", bg="white", fg="red", font=("times new roman", 17),
                                   cursor='hand2',command=self.done_reset).place(x=120, y=340)

    def done_reset(self):
          if self.cmb_quest.get()=="Select":
              messagebox.showerror("Error","Select security question",parent=self.root2)
          elif self.ans.get()=="" or self.new_pass.get()=="":
              messagebox.showerror("Error","All fields are required",parent=self.root2)
          else:
              con = pymysql.connect(host="localhost", user="root", password="", database="project")
              cur = con.cursor()
              qury = ("select * from dct_reg where email=%s and cmb_quest=%s and answer=%s")
              value=(self.email.get(),self.cmb_quest.get(),self.ans.get())
              cur.execute(qury,value)
              row=cur.fetchone()
              if row==None:
                  messagebox.showerror("Error","Wrong Answer or Question",parent=self.root2)
              else:
                  query=("update dct_reg set password=%s where email=%s")
                  value=(self.new_pass.get(),self.email.get())
                  cur.execute(query,value)
                  messagebox.showinfo("Info","Your password as been rested,\n"
                                             "please enter the new password to login",parent=self.root2)

              con.commit()
              con.close()
              self.root2.destroy()



                                ######################################
    #                              Goes to new final doctor page
                                ##################################################

class dct_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Sign Up")
        self.root.geometry("1350x700+0+0")
        #self.root.resizable(False,False)

        self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\doctor.png')
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Login=Label(self.root, text=" Sun Shine Speciality Hospital ", bg="white", fg="black", font=("times new roman", 30,"underline"),
                           cursor='hand2').place(x=420,y=0,width=480)

        pat=Label(self.root, text=" Doctor Area ", bg="white", fg="black", font=("times new roman", 25,"underline"),
                           cursor='hand2').place(x=560,y=47,width=220)

        viapp_btn = Button(self.root, text="  View\n Appointments", fg="black", bg="#9CCDFF",bd=0,
                            font=("times new roman", 25), cursor='hand2',command=self.viewap).place(x=270, y=361,width=210)

        add_pat= Button(self.root, text=" Register\n New Patient", fg="black", bg="#9CCDFF", font=("times new roman",25),
                         cursor='hand2',bd=0,command=self.dctpat_reg).place(x=720, y=361,width=210)

        back_pat = Button(self.root, text="Back", fg="black", bg="violet", font=("times new roman", 25),
                     cursor='hand2', bd=2, command=self.back).place(x=1135, y=110,width=150)
    def viewap(self):
        self.new_window = Toplevel(self.root)
        self.app = viewap_window(self.new_window)

    def dctpat_reg(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def back(self):
       self.root.destroy()

class viewap_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Details")
        self.root.geometry("1000x320+100+150")
        self.root.focus_force()
        self.root.grab_set()
        self.root.config(bg="white")
        self.root.resizable(False, False)

        Frame_login = Frame(self.root, bg="#FFE4E1",bd=10,relief=RIDGE)
        Frame_login.place(x=12, y=20, height=280, width=970)

        connect= pymysql.connect(host="localhost", user="root", password="", database="project",port=3306)
        con = connect.cursor()
        con.execute("select * from appointment")
        tree=ttk.Treeview(Frame_login)
        tree['show']='headings'
        s=ttk.Style(Frame_login)
        s.theme_use("clam")
        tree["columns"]=("pat_name","gender","age","cno","address","symptoms","date","doctor")
        tree.column( "pat_name",width=100,minwidth=50,anchor=tkinter.CENTER)
        tree.column("gender", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("age", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("cno", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("address", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("symptoms", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("date", width=130, minwidth=50, anchor=tkinter.CENTER)
        tree.column( "doctor",width=130,minwidth=50,anchor=tkinter.CENTER)

        tree.heading("pat_name",text="Patient name",anchor=tkinter.CENTER)
        tree.heading("gender", text="Gender", anchor=tkinter.CENTER)
        tree.heading("age", text="Age", anchor=tkinter.CENTER)
        tree.heading("cno", text="Contact Number", anchor=tkinter.CENTER)
        tree.heading("address", text="Address", anchor=tkinter.CENTER)
        tree.heading("symptoms", text="Symptoms", anchor=tkinter.CENTER)
        tree.heading("date", text="Appointment Date", anchor=tkinter.CENTER)
        tree.heading("doctor", text="Appointed Doctor", anchor=tkinter.CENTER)

        i=0
        for rows in con:
            tree.insert('',i,text="",values=(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7]))
            i=i+1
        tree.pack()



##############################             FINSH      DOCTOR     PAGE             #################################
###############################################################
######################################################################################
#                                           page 2
##############################################################################################################3

###############################################################
###############################################################
class user_login:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("1350x700+0+0")
        # self.root.resizable(False,False)

        # bg
        self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\regpage.png')
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.root, text="Login ", font=("helvetica", 35, "bold","underline"), fg="orange", bg="white").place(x=270,
                                                                                                               y=135)

        desc = Label(self.root, text="Patient Login Area", font=("Goudy old style", 15, "bold","underline"), fg="orange",
                     bg="white").place(x=260, y=205)

        email = Label(self.root, text="Email", font=("times new roam", 20, "bold"), bg="white", fg="black").place(
            x=110, y=260)
        self.email = Entry(self.root, font=("times new roman", 15), bg="lightgray")
        self.email.place(x=110, y=305, width=350, height=40)

        pasw = Label(self.root, text="Password ", font=("times new roam", 20, "bold"), bg="white", fg="black").place(
            x=110, y=360)
        self.pasw = Entry(self.root, font=("times new roman", 15), bg="lightgray",show="*")
        self.pasw.place(x=110, y=405, width=350, height=40)

        forget_btn = Button(self.root, text="Forgot Password?", fg="red", bg="white", bd=0,
                            font=("times new roman", 12), cursor='hand2',command=self.email_frgt).place(x=380, y=455)

        new_btn = Button(self.root, text="Create Account?", fg="red", bg="white", bd=0, font=("times new roman", 12),
                         cursor='hand2',command=self.reg_window).place(x=380, y=480)

        Login_btn = Button(self.root, text="Submit ", bg="white", fg="red", font=("times new roman", 20),
                           cursor='hand2',command=self.log_fun).place(x=280, y=525)


        home_btn = Button(self.root, text="Home", bg="#FAF3E1", fg="orange", font=("times new roman", 17),
                          cursor='hand2', bd=2,command=self.new13_window).place(x=0, y=0, width=215)
        admin_btn = Button(self.root, text="Doctor", bg="#FAF3E1", fg="orange", font=("times new roman", 17),
                           cursor='hand2', bd=2,command=self.new14_window).place(x=215, y=0, width=215)
        doctor_btn = Button(self.root, text="Patient", bg="#FAF3E1", fg="orange", font=("times new roman", 17),
                            cursor='hand2', bd=2).place(x=430, y=0, width=215)
        patient_btn = Button(self.root, text="Admin", bg="#FAF3E1", fg="orange", font=("times new roman", 17),
                             cursor='hand2', bd=2,command=self.new16_window).place(x=645, y=0, width=215)
        abt_btn = Button(self.root, text="Developed By", bg="#FAF3E1", fg="orange", font=("times new roman", 17),
                         cursor='hand2', bd=2,command=self.pic_window).place(x=860, y=0, width=215)
        cnt_btn = Button(self.root, text="Back", bg="#FAF3E1", fg="orange", font=("times new roman", 17),
                         cursor='hand2', bd=2,command=self.back_window).place(x=1075, y=0, width=215)

    def new13_window(self):
        self.new_window = Toplevel(self.root)
        self.app = login(self.new_window)

    def new14_window(self):
        self.new_window = Toplevel(self.root)
        self.app = doctor_login(self.new_window)

    # def new15_window(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = user_login(self.new_window)

    def new16_window(self):
        self.new_window = Toplevel(self.root)
        self.app = admin_login(self.new_window)
    def pic_window(self):
        self.new_window = Toplevel(self.root)
        self.app = pic_page(self.new_window)

    def back_window(self):
        self.new_window = Toplevel(self.root)
        self.app = login(self.new_window)

    def log_fun(self):
        if self.email.get() == "" or self.pasw.get() == "":
             messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="project")
                cur = con.cursor()
                cur.execute("select * from pat_reg where email=%s and password=%s",(self.email.get(), self.pasw.get()))
                row = cur.fetchone()
                if row == None:
                        messagebox.showerror("Error", "Invalid username & password", parent=self.root)
                else:
                    open_main = messagebox.askyesno("Success", "Welcome yes to continue",parent=self.root)
                    if open_main > 0:
                        self.new_window = Toplevel(self.root)
                        self.app = pat_page(self.new_window)
                    else:
                        if not open_main:
                            return
                con.commit()
                con.close()
            except Exception as es:
                  messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

    def reg_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def email_frgt(self):
        if self.email.get()=="":
            messagebox.showerror("Error","Enter email address to reset password",parent=self.root)
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="project")
            cur = con.cursor()
            query=("select * from pat_reg where email=%s")
            value=(self.email.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Enter the valid email-id",parent=self.root)
            else:
                con.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x400+400+150")
                self.root2.focus_force()
                self.root2.grab_set()
                self.root2.config(bg="white")

                Frame_login = Frame(self.root2, bg="#E3E3E3",bd=5,relief=RIDGE)
                Frame_login.place(x=12, y=20, height=350, width=376)

                title = Label(self.root2, text="  Forgot Password  ",bd=2,relief=RIDGE, font=("Goudy old style", 23, "bold", "underline"),
                              fg="black", bg="#EAEAEA")
                title.place(x=82, y=30)

                question = Label(self.root2, text="Security question", font=("times new roam", 15, "bold"), bg="#E3E3E3",
                                 fg="black").place(x=20, y=100)
                self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 15), state='readonly', justify=CENTER)
                self.cmb_quest['value'] = ("Select", "Year of born", "Pet dog name", "Birth place", "Favourite Actor")
                self.cmb_quest.place(x=20, y=130, width=300)
                self.cmb_quest.current(0)

                ans = Label(self.root2, text="Answer", font=("times new roam", 15, "bold"), bg="#E3E3E3",
                            fg="black").place(x=20, y=180)
                self.ans = Entry(self.root2, font=("times new roman", 15), bg="white")
                self.ans.place(x=20, y=210, width=300)

                new_pass = Label(self.root2, text="New password", font=("times new roam", 15, "bold"), bg="#E3E3E3",
                                 fg="black").place(x=20, y=260)
                self.new_pass = Entry(self.root2, font=("times new roman", 15), bg="white")
                self.new_pass.place(x=20, y=290, width=300)

                Login_btn = Button(self.root2, text="Reset password", bg="white", fg="red", font=("times new roman", 17),
                                   cursor='hand2',command=self.done_reset).place(x=120, y=340)

    def done_reset(self):
          if self.cmb_quest.get()=="Select":
              messagebox.showerror("Error","Select security question",parent=self.root2)
          elif self.ans.get()=="" or self.new_pass.get()=="":
              messagebox.showerror("Error","All fields are required",parent=self.root2)
          else:
              con = pymysql.connect(host="localhost", user="root", password="", database="project")
              cur = con.cursor()
              qury = ("select * from pat_reg where email=%s and cmb_sque=%s and answer=%s")
              value=(self.email.get(),self.cmb_quest.get(),self.ans.get())
              cur.execute(qury,value)
              row=cur.fetchone()
              if row==None:
                  messagebox.showerror("Error","Enter the correct answer")
              else:
                  query=("update pat_reg set password=%s where email=%s")
                  value=(self.new_pass.get(),self.email.get())
                  cur.execute(query,value)
                  con.commit()
                  con.close()
                  messagebox.showinfo("Info","Your password as been rested,\n"
                                             "please enter the new password to login",parent=self.root2)
                  self.root2.destroy()


############################                                        ################################################
                    #       REgister page    go down for final page
#################################3                                      ###################

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Regiseration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # Bg_image
        self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\bgg.jpg')
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # bg_left
        self.left = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\reg_left.jpg')
        left = Label(self.root, image=self.left).place(x=120, y=100, width=400, height=500)

        # ===framing===
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        banner= Label(self.root, text="  ---------------------  \nStart each day\nwith a\ngreatful heart\n  ---------------------  \n\n\n\n",
                      font=("Helvetica 25 italic bold"), bg="#E3E3E3", fg="black").place(x=160, y=180)

        title = Label(frame1, text="Register Here", font=("times new roam", 20, "bold"), bg="white", fg="green").place(
            x=50, y=10)

        f_name = Label(frame1, text="First Name", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(
            x=50, y=70)
        self.fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.fname.place(x=50, y=100, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(
            x=370, y=70)
        self.lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.lname.place(x=370, y=100, width=250)

        #####

        contact = Label(frame1, text="Contact No", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(
            x=50, y=140)
        self.contactno = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.contactno.place(x=50, y=170, width=250)

        email = Label(frame1, text="Email", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(x=370,y=140)
        self.email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.email.place(x=370, y=170, width=250)

        ####
        state = Label(frame1, text="State", font=("times new roam", 15, "bold"), bg="white",
                         fg="grey").place(x=50, y=210)
        self.state = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.state['value'] = ("Select", "Andra Pradesh", "Assam", "Bihar","Chattisgarh","Gujarat","Haryana","Jharkhand","Karnataka","Kerala","Maharastra","Odisha","Punjab","Rajasthan","Tamil Nadu","Telagana","Uttar Pradesh","West Bengal")
        self.state.place(x=50, y=240, width=250)
        self.state.current(0)

        dob = Label(frame1, text="Date Of Birth", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(x=370,y=210)
        self.dob = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.dob.place(x=370, y=240, width=250)

        question = Label(frame1, text="Security Question", font=("times new roam", 15, "bold"), bg="white",
                         fg="grey").place(x=50, y=275)
        self.cmb_sque = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_sque['value'] = ("Select", "Pet dog name","Born place","Best friend name")
        self.cmb_sque.place(x=50, y=310, width=250)
        self.cmb_sque.current(0)

        answer = Label(frame1, text="Answer", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(
            x=370, y=275)
        self.answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.answer.place(x=370, y=310, width=250)

        ###
        password = Label(frame1, text="Password", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(
            x=50, y=340)
        self.password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.password.place(x=50, y=370, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roam", 15, "bold"), bg="white",
                          fg="grey").place(x=370, y=340)
        self.cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.cpassword.place(x=370, y=370, width=250)

        self.var_chk=IntVar()
        chk = Checkbutton(frame1, text='I agree the terms & conditions', onvalue=1, offvalue=0, bg='white',
                          font=('times new roam', 12),variable=self.var_chk).place(x=50, y=410)

        btn_button = Button(self.root, text='Sign In', font=("times new roam", 20), bd=5,relief=RIDGE, cursor='hand2',
                            command=self.return_login,bg="#FCFCFC",fg="black").place(x=215,y=460,width=180)

        btn = Button(frame1,text="- Register now -",font=("times new roam", 20),fg="white",bg="green", cursor='hand2',
                     command=self.login_function).place(x=250,y=440)

    def clear(self):
        self.fname.delete(0,END)
        self.lname.delete(0, END)
        self.contactno.delete(0, END)
        self.email.delete(0, END)
        self.state.delete(0, END)
        self.dob.delete(0, END)
        self.answer.delete(0, END)
        self.password.delete(0, END)
        self.cpassword.delete(0,END)
        self.cmb_sque.current(0)

    def login_function(self):
        if self.fname.get()=="" or self.lname.get()=="" or self.email.get() == "" or self.password.get() == ""or \
                self.cpassword.get() == "" or self.answer.get() == ""or self.contactno.get()==""\
                or self.cmb_sque.get()=="Select" or self.state.get()=="" or self.dob.get()=="" :
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.password.get()!=self.cpassword.get():
            messagebox.showerror("Error","Password and Conform Password are not same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Agree the terms and condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="project")
                cur=con.cursor()
                cur.execute("Select * from pat_reg where email=%s",self.email.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error"," User already exits,please try with another email",parent=self.root)
                else:
                     cur.execute("insert into pat_reg (fname,lname,contactno,email,state,dob,cmb_sque,answer,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.fname.get(),
                         self.lname.get(),
                         self.contactno.get(),
                         self.email.get(),
                         self.state.get(),
                         self.dob.get(),
                         self.cmb_sque.get(),
                         self.answer.get(),
                         self.password.get(),
                         ))
                     con.commit()
                     con.close()
                     messagebox.showinfo("Success","Registered", parent=self.root)
                     self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

    def return_login(self):
        self.root.destroy()

class pat_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Patient Window")
        self.root.geometry("1600x900+0+0")

        self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\patient.png')
        bg= Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Login=Label(self.root, text=" Sun Shine Speciality Hospital ", bg="white", fg="black", font=("times new roman", 30,"underline"),
                           cursor='hand2').place(x=0,y=0,width=1290)

        pat=Label(self.root, text=" Patient Area ", bg="white", fg="black", font=("times new roman", 25,"underline"),
                           cursor='hand2').place(x=0,y=47,width=1290)

        home_btn = Button(self.root, text="Book Appointment", bg="white", fg="black", font=("times new roman", 17),
                        cursor='hand2',bd=2,command=self.pat01).place(x=0, y=90,width=215)

        admin_btn = Button(self.root, text="Doctor availability", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pat02).place(x=215, y=90, width=215)

        doctor_btn = Button(self.root, text="Hospital View", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pic).place(x=430, y=90, width=215)

        patient_btn = Button(self.root, text="Developed By", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pat04).place(x=645, y=90, width=215)

        abt_btn = Button(self.root, text="Logut", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.logout).place(x=860, y=90, width=215)

        cnt_btn = Button(self.root, text="Back", bg="white", fg="black", font=("times new roman", 17),
                          cursor='hand2', bd=2,command=self.pat0).place(x=1075, y=90, width=215)

    def pat0(self):
        self.new_window = Toplevel(self.root)
        self.app = user_login(self.new_window)

    def pat01(self):
        self.new_window = Toplevel(self.root)
        self.app = pat01_page(self.new_window)

    def pat02(self):
        self.new_window = Toplevel(self.root)
        self.app = pat02_page(self.new_window)

    def logout(self):
        self.new_window = Toplevel(self.root)
        self.app = user_login(self.new_window)

    def pat04(self):
        self.new_window = Toplevel(self.root)
        self.app = pat04_page(self.new_window)

    def pic(self):
        self.new_window = Toplevel(self.root)
        self.app = pat03_page(self.new_window)


class pat01_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Appointment Area")
        self.root.geometry("1600x900+0+0")

        #self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\d3.png')
        #bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Login=Label(self.root, text=" Sun Shine Speciality Hospital ", bg="white", fg="black", font=("times new roman", 30,"underline"),
                           cursor='hand2').place(x=0,y=0,width=1290)

        pat=Label(self.root, text=" Appointment Area ", bg="white", fg="black", font=("times new roman", 25,"underline"),
                           cursor='hand2').place(x=0,y=47,width=1290)

        appo_btn = Button(self.root, text="Book Appointment", bg="white", fg="black", font=("times new roman", 17),
                        cursor='hand2',bd=2).place(x=0, y=90,width=215)

        avb_btn = Button(self.root, text="Doctor availability", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pat02).place(x=215, y=90, width=215)

        view_btn = Button(self.root, text="Hospital View", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pic).place(x=430, y=90, width=215)

        patient_btn = Button(self.root, text="Developed By", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pat04).place(x=645, y=90, width=215)

        bck_btn = Button(self.root, text="Logut", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.logut).place(x=860, y=90, width=215)

        cnt_btn = Button(self.root, text="Back", bg="white", fg="black", font=("times new roman", 17),
                          cursor='hand2', bd=2,command=self.back).place(x=1075, y=90, width=215)

        ###################################################################################################
        #####################################################################################################
        #####################           #####################                ##############################

        self.pat_name = StringVar()
        self.gender = StringVar()
        self.age = StringVar()
        self.cno = StringVar()
        self.address = StringVar()
        self.symptoms = StringVar()
        self.date = StringVar()
        self.doctor = StringVar()

        DataFrame=Frame(self.root,bd=16,padx=16,relief=RIDGE)
        DataFrame.place(x=0,y=135,width=1280,height=350)

        DataFrameLeft = LabelFrame(DataFrame, bd=8,padx=16,relief=RIDGE,font=("times new roman", 13),text="Patient Information")
        DataFrameLeft.place(x=0,y=0,width=800,height=310)

        DataFrameRight = LabelFrame(DataFrame, bd=8,padx=16,relief=RIDGE,font=("times new roman", 13),text="Over_view")
        DataFrameRight.place(x=805,y=0,width=410,height=310)

#            Btn_Frames
        BtnFrame=Frame(self.root,bd=16,padx=16,relief=RIDGE,bg="green")
        BtnFrame.place(x=0,y=483,width=1280,height=70)

#############
        DetailsFrame=Frame(self.root,bd=16,padx=16,relief=RIDGE)
        DetailsFrame.place(x=0,y=550,width=1280,height=140)
###########
        pat_name=Label(DataFrameLeft,text="Patient Name",font=("times new roman", 17,"bold"),padx=2,pady=2)
        pat_name.place(x=0,y=5)
        pat_name = Entry(DataFrameLeft, textvariable=self.pat_name,font=("times new roman", 15), bg="white")
        pat_name.place(x=0, y=37, width=320)

        gender = Label(DataFrameLeft, text="Gender", font=("times new roman", 17,"bold"))
        gender.place(x=0, y=72)
        cmb_gender = ttk.Combobox(DataFrameLeft, textvariable=self.gender,font=("times new roman", 15), state='readonly', justify=CENTER)
        cmb_gender['value'] = ("- Select -", "Male","Female")
        cmb_gender.place(x=0, y=104, width=320)
        cmb_gender.current(0)

        age = Label(DataFrameLeft, text="Age", font=("times new roman", 17,"bold"))
        age.place(x=0, y=139)
        age = Entry(DataFrameLeft,textvariable=self.age, font=("times new roman", 15), bg="white")
        age.place(x=0, y=171, width=320)

        cno = Label(DataFrameLeft, text="Contact Number", font=("times new roman", 17,"bold"))
        cno.place(x=0, y=206)
        cno = Entry(DataFrameLeft,textvariable=self.cno, font=("times new roman", 15), bg="white")
        cno.place(x=0, y=238, width=320)

        address = Label(DataFrameLeft, text="Address", font=("times new roman", 17,"bold"))
        address.place(x=400, y=5)
        address = Entry(DataFrameLeft,textvariable=self.address, font=("times new roman", 15), bg="white")
        address.place(x=400, y=37, width=320)

        symptoms = Label(DataFrameLeft, text="Symptoms", font=("times new roman", 17,"bold"))
        symptoms.place(x=400, y=72)
        symptoms = Entry(DataFrameLeft, textvariable=self.symptoms,font=("times new roman", 15), bg="white")
        symptoms.place(x=400, y=104, width=320)

        date = Label(DataFrameLeft, text="Enter Appointment Date", font=("times new roman", 17,"bold"))
        date.place(x=400, y=139)
        date = Entry(DataFrameLeft, textvariable=self.date,font=("times new roman", 15), bg="white")
        date.place(x=400, y=171, width=320)

        doctor = Label(DataFrameLeft, text="Select To Appoint Doctor", font=("times new roman", 17,"bold"))
        doctor.place(x=400, y=206)
        doctor = ttk.Combobox(DataFrameLeft, textvariable=self.doctor,font=("times new roman", 16), state='readonly', justify=CENTER)
        doctor['value'] = ("- Select -", "Dr.Bugga ","Dr.Srujs ")
        doctor.place(x=400, y=238, width=320)
        doctor.current(0)

##########################--- DataFrameRight
        self.view=Text(DataFrameRight,font=("arial",12,"bold"),width=40,height=14)
        self.view.place(x=0,y=0)
#############

        btn_reg=Button(BtnFrame,text="--------",bg="white",fg="black",font=("arial",14,"bold"),width=19,)
                       #command=self.pat_data)
        btn_reg.place(x=0,y=0)
        btn_view=Button(BtnFrame,text="Register",bg="white",fg="black",font=("arial",14,"bold"),width=19,command=self.pat_data)
                        #command=self.over_view)
        btn_view.place(x=240,y=0)
        btn_update=Button(BtnFrame,text="Over-View",bg="white",fg="black",font=("arial",14,"bold"),width=19,command=self.over_view)
                          #command=self.update_pat)
        btn_update.place(x=480,y=0)
        btn_del=Button(BtnFrame,text="Reset",bg="white",fg="black",font=("arial",14,"bold"),width=19,command=self.clear)
        btn_del.place(x=720,y=0)
        btn_reset=Button(BtnFrame,text="--------",bg="white",fg="black",font=("arial",14,"bold"),width=20,)
                         #command=self.clear)
        btn_reset.place(x=960,y=0)

###########      TABLE  + scrolbar

        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)

        self.hospital_table=ttk.Treeview(DetailsFrame,columns=("pat_name","gender","age","cno","address","symptoms",
                                "date","doctor"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.hospital_table.heading("pat_name",text="Patient Name")
        self.hospital_table.heading("gender", text="Gender")
        self.hospital_table.heading("age", text="Age")
        self.hospital_table.heading("cno", text="Contact Number")
        self.hospital_table.heading("address", text="Address")
        self.hospital_table.heading("symptoms", text="Symptoms")
        self.hospital_table.heading("date", text="Appointment Date")
        self.hospital_table.heading("doctor", text="Appointed Doctor")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("pat_name",width=100)
        self.hospital_table.column("gender", width=100)
        self.hospital_table.column("age", width=100)
        self.hospital_table.column("cno", width=100)
        self.hospital_table.column("address",width=100)
        self.hospital_table.column("symptoms", width=100)
        self.hospital_table.column("date", width=100)
        self.hospital_table.column("doctor", width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()

#######################################################################################################################
    def pat_data(self):
        if self.pat_name.get() == "" or self.age.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="project")
            cur=con.cursor()
            cur.execute("insert into appointment values(%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.pat_name.get(),
                         self.gender.get(),
                         self.age.get(),
                         self.cno.get(),
                         self.address.get(),
                         self.symptoms.get(),
                         self.date.get(),
                         self.doctor.get()
                         ))
            con.commit()
            self.fatch_data()
            con.close()
            messagebox.showinfo("Success","Registered", parent=self.root)

    # def update_pat(self):
    #     con = pymysql.connect(host="localhost", user="root", password="", database="project")
    #     cur = con.cursor()
    #     cur.execute("update appointment set gender=%s,age=%s,cno=%s,address=%s,symptoms=%s,date=%s,doctor=%s where pat_name=%s",
    #                 (
    #                     self.gender.get(),
    #                     self.age.get(),
    #                     self.cno.get(),
    #                     self.address.get(),
    #                     self.symptoms.get(),
    #                     self.date.get(),
    #                     self.doctor.get(),
    #                     self.pat_name.get()))

    def fatch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="project")
        cur = con.cursor()
        cur.execute("select * from appointment")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            con.commit()
        con.close()
    def get_cursor(self, event="" ):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.pat_name.set(row[0])
        self.gender.set(row[1])
        self.age.set(row[2])
        self.cno.set(row[3])
        self.address.set(row[4])
        self.symptoms.set(row[5])
        self.date.set(row[6])
        self.doctor.set(row[7])

    def over_view(self):
        self.view.insert(END, "Patient Name: \t\t\t" + self.pat_name.get() + "\n")
        self.view.insert(END, "Gender: \t\t\t" + self.gender.get() + "\n")
        self.view.insert(END, "Age: \t\t\t" + self.age.get() + "\n")
        self.view.insert(END, "Contact Number: \t\t\t" + self.cno.get() + "\n")
        self.view.insert(END, "Address: \t\t\t" + self.address.get() + "\n")
        self.view.insert(END, "Symptoms: \t\t\t" + self.symptoms.get() + "\n")
        self.view.insert(END, "Appointment Date: \t\t\t" + self.date.get() + "\n")
        self.view.insert(END, "Appointed Doctor: \t\t\t" + self.doctor.get() + "\n\n")

    # def pat_delete(self):
    #     con = pymysql.connect(host="localhost", user="root", password="", database="project")
    #     cur = con.cursor()
    #     query="delete from appointment where pat_name=%s"
    #     value=(self.pat_name.get(),)
    #     cur.execute(query,value)
    #     con.commit()
    #     con.close()
    #     self.fatch_data()
    #     messagebox.showinfo("Delete","Patient details has been deleted ")

    def clear(self):
        self.pat_name.set("")
        self.gender.set("")
        self.age.set("")
        self.cno.set("")
        self.address.set("")
        self.symptoms.set("")
        self.date.set("")
        self.doctor.set("")
        self.view.delete("1.0",END)

    def back(self):
        self.new_window = Toplevel(self.root)
        self.app = pat_page(self.new_window)

    def pat02(self):
        self.new_window = Toplevel(self.root)
        self.app = pat02_page(self.new_window)

    def logut(self):
        self.new_window = Toplevel(self.root)
        self.app = user_login(self.new_window)

    def pat04(self):
        self.new_window = Toplevel(self.root)
        self.app = pat04_page(self.new_window)

    def pic(self):
        self.new_window = Toplevel(self.root)
        self.app = pat03_page(self.new_window)


class pat02_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Patient Area")
        self.root.geometry("1600x900+0+0")
        self.root.config(bg="#C1CDC1")

        Login=Label(self.root, text=" Sun Shine Speciality Hospital ", bg="white", fg="black", font=("times new roman", 30,"underline"),
                           cursor='hand2').place(x=0,y=0,width=1290)

        pat=Label(self.root, text=" Patient Area ", bg="white", fg="black", font=("times new roman", 25,"underline"),
                           cursor='hand2').place(x=0,y=47,width=1290)

        home_btn = Button(self.root, text="Book Appointment", bg="white", fg="black", font=("times new roman", 17),
                        cursor='hand2',bd=2,command=self.pat01).place(x=0, y=90,width=215)

        admin_btn = Button(self.root, text="Doctor availability", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2).place(x=215, y=90, width=215)

        doctor_btn = Button(self.root, text="Hospital View", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pat03).place(x=430, y=90, width=215)

        patient_btn = Button(self.root, text="Develpoed By", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pat04).place(x=645, y=90, width=215)

        abt_btn = Button(self.root, text="Logut", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.logout).place(x=860, y=90, width=215)

        cnt_btn = Button(self.root, text="Back", bg="white", fg="black", font=("times new roman", 17),
                          cursor='hand2', bd=2,command=self.back).place(x=1075, y=90, width=215)

        DataFrameLeft = LabelFrame(self.root, bd=12,padx=16,relief=RIDGE,font=("times new roman", 17),
                                   bg="#FFEFDB",text="Genral Doctors")
        DataFrameLeft.place(x=30,y=180,width=360,height=440)

        dct1_name = Label(DataFrameLeft, text="- Dr.Bugga", font=("times new roman", 16, "bold"),bg="#FFEFDB", padx=2, pady=2)
        dct1_name.place(x=30, y=5)
        spc1 = Label(DataFrameLeft, text="MBBS,MS(General Surgeon)", font=("times new roman", 11),bg="#FFEFDB", padx=2, pady=2)
        spc1.place(x=80, y=32)
        spc01 = Label(DataFrameLeft, text="Mon-Thu (9AM-7PM)", font=("times new roman", 11),bg="#FFEFDB", padx=2, pady=2)
        spc01.place(x=80, y=51)

        dct2_name = Label(DataFrameLeft, text="- Dr.Srujs", font=("times new roman", 16, "bold"), bg="#FFEFDB",padx=2, pady=2)
        dct2_name.place(x=30, y=79)
        spc2 = Label(DataFrameLeft, text="MBBS,MS(General Surgeon)", font=("times new roman", 11),bg="#FFEFDB", padx=2, pady=2)
        spc2.place(x=80, y=107)
        spc02 = Label(DataFrameLeft, text="Fri-Sun (9AM-7PM)", font=("times new roman", 11),bg="#FFEFDB", padx=2, pady=2)
        spc02.place(x=80, y=126)

        dct3_name = Label(DataFrameLeft, text="- Dr.Sonu", font=("times new roman", 16, "bold"), bg="#FFEFDB",padx=2, pady=2)
        dct3_name.place(x=30, y=154)
        spc3 = Label(DataFrameLeft, text="MBBS,MS(General Surgeon)", font=("times new roman", 11),bg="#FFEFDB", padx=2, pady=2)
        spc3.place(x=80, y=181)
        spc03 = Label(DataFrameLeft, text="Wed (9AM-7PM)", font=("times new roman", 11),bg="#FFEFDB", padx=2, pady=2)
        spc03.place(x=80, y=200)


        dct4_name = Label(DataFrameLeft, text="- Dr.Deva", font=("times new roman", 16, "bold"),bg="#FFEFDB", padx=2, pady=2)
        dct4_name.place(x=30, y=228)
        spc4 = Label(DataFrameLeft, text="MBBS,MS(General Surgeon)", font=("times new roman", 11),bg="#FFEFDB", padx=2, pady=2)
        spc4.place(x=80, y=255)
        spc04 = Label(DataFrameLeft, text="Thu (7PM-5AM)", font=("times new roman", 11),bg="#FFEFDB", padx=2, pady=2)
        spc04.place(x=80, y=274)

        dct5_name = Label(DataFrameLeft, text="- Dr.Seema", font=("times new roman", 16, "bold"),bg="#FFEFDB", padx=2, pady=2)
        dct5_name.place(x=30, y=302)
        spc5 = Label(DataFrameLeft, text="MBBS,MS(General Surgeon)", font=("times new roman", 11),bg="#FFEFDB", padx=2, pady=2)
        spc5.place(x=80, y=329)
        spc05 = Label(DataFrameLeft, text="Sat (9AM-7PM)", font=("times new roman", 11), bg="#FFEFDB",padx=2, pady=2)
        spc05.place(x=80, y=348)

####################################

        DataFrameMiddle = LabelFrame(self.root, bd=12,padx=16,relief=RIDGE,bg="#BBFFFF",font=("times new roman", 17),text="Cardiologist")
        DataFrameMiddle.place(x=450,y=180,width=360,height=310)

        dct1_name = Label(DataFrameMiddle, text="- Dr.Sandeep", font=("times new roman", 16, "bold"), bg="#BBFFFF",padx=2, pady=2)
        dct1_name.place(x=30, y=5)
        spc1 = Label(DataFrameMiddle, text="MBBS,MS(MBBS,MD,DM,MRCP)", font=("times new roman", 11),bg="#BBFFFF", padx=2, pady=2)
        spc1.place(x=80, y=32)
        spc01 = Label(DataFrameMiddle, text="Mon (9AM-7PM)", font=("times new roman", 11),bg="#BBFFFF", padx=2, pady=2)
        spc01.place(x=80, y=51)

        dct2_name = Label(DataFrameMiddle, text="- Dr.Harsha", font=("times new roman", 16, "bold"),bg="#BBFFFF", padx=2, pady=2)
        dct2_name.place(x=30, y=79)
        spc2 = Label(DataFrameMiddle, text="MBBS,MS(DNB,MCh,MS,MBBS)", font=("times new roman", 11),bg="#BBFFFF", padx=2, pady=2)
        spc2.place(x=80, y=107)
        spc02 = Label(DataFrameMiddle, text="Sun (11AM-6PM)", font=("times new roman", 11),bg="#BBFFFF" ,padx=2, pady=2)
        spc02.place(x=80, y=126)

        dct3_name = Label(DataFrameMiddle, text="- Dr.Rani", font=("times new roman", 16, "bold"),bg="#BBFFFF", padx=2, pady=2)
        dct3_name.place(x=30, y=154)
        spc3 = Label(DataFrameMiddle, text="MBBS,MS(MCh,MS,MBBS)", font=("times new roman", 11),bg="#BBFFFF", padx=2, pady=2)
        spc3.place(x=80, y=181)
        spc03 = Label(DataFrameMiddle, text="Mon (9AM-4PM)", font=("times new roman", 11),bg="#BBFFFF" ,padx=2, pady=2)
        spc03.place(x=80, y=200)
############################################
        ############################


        DataFrameRight = LabelFrame(self.root, bd=12,padx=16,relief=RIDGE,font=("times new roman", 17),
                                  bg="#FFE4E1",text="Specialist Doctors")
        DataFrameRight.place(x=850,y=380,width=360,height=280)

        dct1_name = Label(DataFrameRight, text="- Dr.Jahnavi", font=("times new roman", 16, "bold"),bg="#FFE4E1", padx=2, pady=2)
        dct1_name.place(x=30, y=5)
        spc1 = Label(DataFrameRight, text="MBBS,DCH,MRCPCH", font=("times new roman", 11),bg="#FFE4E1", padx=2, pady=2)
        spc1.place(x=80, y=32)
        spc01 = Label(DataFrameRight, text="Mon (9AM-7PM)", font=("times new roman", 11), bg="#FFE4E1",padx=2, pady=2)
        spc01.place(x=80, y=51)

        dct2_name = Label(DataFrameRight, text="-Dr.Mehataj", font=("times new roman", 16, "bold"),bg="#FFE4E1", padx=2, pady=2)
        dct2_name.place(x=30, y=79)
        spc2 = Label(DataFrameRight, text="MBBS,MD(Ped),DNB(Ped)", font=("times new roman", 11),bg="#FFE4E1", padx=2, pady=2)
        spc2.place(x=80, y=107)
        spc02 = Label(DataFrameRight, text="Sun (11AM-6PM)", font=("times new roman", 11), padx=2,bg="#FFE4E1", pady=2)
        spc02.place(x=80, y=126)

        dct3_name = Label(DataFrameRight, text="- Dr.Rani", font=("times new roman", 16, "bold"),bg="#FFE4E1", padx=2, pady=2)
        dct3_name.place(x=30, y=154)
        spc3 = Label(DataFrameRight, text="MBBS,DCH(CAL)", font=("times new roman", 11), padx=2,bg="#FFE4E1", pady=2)
        spc3.place(x=80, y=181)
        spc03 = Label(DataFrameRight, text="Mon (9AM-4PM)", font=("times new roman", 11), padx=2,bg="#FFE4E1", pady=2)
        spc03.place(x=80, y=200)


        DataFrameTopRight = LabelFrame(self.root, bd=12,padx=16,relief=RIDGE,font=("times new roman", 17),bg="#FFEFD5",text="Psychiatrist")
        DataFrameTopRight.place(x=880,y=150,width=360,height=200)

        dct3_name = Label(DataFrameTopRight, text="- Dr.Sai Sunny", font=("times new roman", 16, "bold"),bg="#FFEFD5", padx=2, pady=2)
        dct3_name.place(x=20, y=5)
        spc3 = Label(DataFrameTopRight, text="Psychiatrist", font=("times new roman", 11),bg="#FFEFD5", padx=2, pady=2)
        spc3.place(x=70, y=33)
        spc03 = Label(DataFrameTopRight, text="Sat (1PM-4PM)", font=("times new roman", 11), bg="#FFEFD5",padx=2, pady=2)
        spc03.place(x=70, y=52)

        dct3_name = Label(DataFrameTopRight, text="- Dr.Sandy Kumar", font=("times new roman", 16, "bold"),bg="#FFEFD5", padx=2, pady=2)
        dct3_name.place(x=20, y=80)
        spc3 = Label(DataFrameTopRight, text="Psychiatrist", font=("times new roman", 11), bg="#FFEFD5",padx=2, pady=2)
        spc3.place(x=70, y=107)
        spc03 = Label(DataFrameTopRight, text="Mon (12PM-4PM)", font=("times new roman", 11),bg="#FFEFD5", padx=2, pady=2)
        spc03.place(x=70, y=126)

        DataFrameDown= LabelFrame(self.root, bd=12,padx=16,relief=RIDGE,font=("times new roman", 17),bg="#F0E68C",text="Neurologist")
        DataFrameDown.place(x=440,y=525,width=360,height=150)

        dct3_name = Label(DataFrameDown, text="- Dr.Sadiya", font=("times new roman", 16, "bold"),bg="#F0E68C", padx=2, pady=2)
        dct3_name.place(x=10, y=10)
        spc3 = Label(DataFrameDown, text="MD,DM(Neurology)", font=("times new roman", 11), bg="#F0E68C",padx=2, pady=2)
        spc3.place(x=60, y=38)
        spc03 = Label(DataFrameDown, text="Mon (12PM-4PM)", font=("times new roman", 11),bg="#F0E68C", padx=2, pady=2)
        spc03.place(x=60, y=57)

    def pat01(self):
        self.new_window = Toplevel(self.root)
        self.app = pat01_page(self.new_window)


    def pat03(self):
        self.new_window=Toplevel(self.root)
        self.app=pat03_page(self.new_window)

    def pat04(self):
        self.new_window = Toplevel(self.root)
        self.app = pat04_page(self.new_window)

    def logout(self):
        self.new_window = Toplevel(self.root)
        self.app = user_login(self.new_window)

    def back(self):
        self.new_window = Toplevel(self.root)
        self.app = pat_page(self.new_window)

class pat03_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Patient Area")
        self.root.geometry("1600x900+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\hospital.png')
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        Login=Label(self.root, text=" Sun Shine Speciality Hospital ", bg="white", fg="black", font=("times new roman", 30,"underline"),
                           cursor='hand2').place(x=0,y=0,width=1290)

        pat=Label(self.root, text=" Patient Area ", bg="white", fg="black", font=("times new roman", 25,"underline"),
                           cursor='hand2').place(x=0,y=47,width=1290)

        home_btn = Button(self.root, text="Book Appointment", bg="white", fg="black", font=("times new roman", 17),
                        cursor='hand2',bd=2,command=self.pat01).place(x=0, y=90,width=215)

        admin_btn = Button(self.root, text="Doctor availability", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pat02).place(x=215, y=90, width=215)

        doctor_btn = Button(self.root, text="Hospital View", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2).place(x=430, y=90, width=215)

        patient_btn = Button(self.root, text="Developed By", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pat04).place(x=645, y=90, width=215)

        abt_btn = Button(self.root, text="Logut", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.logut).place(x=860, y=90, width=215)

        cnt_btn = Button(self.root, text="Back", bg="white", fg="black", font=("times new roman", 17),
                          cursor='hand2', bd=2,command=self.back).place(x=1075, y=90, width=215)

    def pat01(self):
        self.new_window = Toplevel(self.root)
        self.app = pat01_page(self.new_window)

    def pat02(self):
        self.new_window = Toplevel(self.root)
        self.app = pat02_page(self.new_window)

    def pat04(self):
        self.new_window = Toplevel(self.root)
        self.app = pat04_page(self.new_window)

    def logut(self):
        self.new_window = Toplevel(self.root)
        self.app = user_login(self.new_window)

    def back(self):
        self.new_window = Toplevel(self.root)
        self.app = pat_page(self.new_window)


class pat04_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Doctors List")
        self.root.geometry("1600x900+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\developedby.png')
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        Login=Label(self.root, text=" Sun Shine Speciality Hospital ", bg="white", fg="black", font=("times new roman", 30,"underline"),
                           cursor='hand2').place(x=0,y=0,width=1290)

        pat=Label(self.root, text=" Patient Area ", bg="white", fg="black", font=("times new roman", 25,"underline"),
                           cursor='hand2').place(x=0,y=47,width=1290)

        home_btn = Button(self.root, text="Book Appointment", bg="white", fg="black", font=("times new roman", 17),
                        cursor='hand2',bd=2,command=self.pat01).place(x=0, y=90,width=215)

        admin_btn = Button(self.root, text="Doctor availability", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pat02).place(x=215, y=90, width=215)

        doctor_btn = Button(self.root, text="Hospital View", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.pat03).place(x=430, y=90, width=215)

        patient_btn = Button(self.root, text="Developed By", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2).place(x=645, y=90, width=215)

        abt_btn = Button(self.root, text="Logout", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.logut).place(x=860, y=90, width=215)

        cnt_btn = Button(self.root, text="Back", bg="white", fg="black", font=("times new roman", 17),
                          cursor='hand2', bd=2,command=self.pat00).place(x=1075, y=90, width=215)

        DataFrameTop = Frame(self.root, bd=2,bg="#FFBEDB",relief=RIDGE)
        DataFrameTop.place(x=467, y=205,width=536,height=97)
        Login=Label(DataFrameTop, text="Thukaram Rao A.N.V", bg="#FFBEDB", fg="black", font=("times new roman",30),
                           cursor='hand2').place(x=0,y=10,width=400)
        Login=Label(DataFrameTop, text="( 1RL19CS001 )", bg="#FFBEDB", fg="black", font=("times new roman",15),
                           cursor='hand2').place(x=220,y=50,width=200)

        DataFrameMiddle = Frame(self.root, bd=2,bg="#FFBEDB",relief=RIDGE)
        DataFrameMiddle.place(x=467, y=380,width=536,height=97)
        Login = Label(DataFrameMiddle, text="Harsha Vardhan.S", bg="#FFBEDB", fg="black", font=("times new roman", 30),
                      cursor='hand2').place(x=0, y=10, width=400)
        Login = Label(DataFrameMiddle, text="( 1RL19CS031 )", bg="#FFBEDB", fg="black", font=("times new roman", 15),
                      cursor='hand2').place(x=220, y=50, width=200)

        DataFrameBottom= Frame(self.root, bd=2,bg="#FFBEDB",relief=RIDGE)
        DataFrameBottom.place(x=467, y=555,width=536,height=97)
        Login = Label(DataFrameBottom, text="Harshith Babu.K", bg="#FFBEDB", fg="black", font=("times new roman", 30),
                      cursor='hand2').place(x=0, y=10, width=400)
        Login = Label(DataFrameBottom, text="( 1RL19CS035 )", bg="#FFBEDB", fg="black", font=("times new roman", 15),
                      cursor='hand2').place(x=220, y=50, width=200)

    def pat00(self):
        self.new_window = Toplevel(self.root)
        self.app = pat_page(self.new_window)

    def pat01(self):
        self.new_window = Toplevel(self.root)
        self.app = pat01_page(self.new_window)

    def pat02(self):
        self.new_window = Toplevel(self.root)
        self.app = pat02_page(self.new_window)

    def pat03(self):
        self.new_window = Toplevel(self.root)
        self.app = pat03_page(self.new_window)

    def pat04(self):
        self.new_window = Toplevel(self.root)
        self.app = pat04_page(self.new_window)

    def logut(self):
        self.new_window = Toplevel(self.root)
        self.app = user_login(self.new_window)


#################                FINSH     PATIENT      PAGE             ##############################################
###############################################################
####################################################################################################
#                                       page 3
###############################################################################################

###############################################################
###############################################################

class admin_login:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Area")
        self.root.geometry("1350x700+0+0")
        #self.root.resizable(False,False)

        #bg
        self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\p3.jpg')
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #frame
        Frame_login=Frame (self.root,bg="white")
        Frame_login.place(x=730,y=85,height=520,width=450)

        title=Label(self.root,text="Admin Login ",font=("Impact",35,"bold","underline"),fg="orange",bg="white")
        title.place(x=833,y=125)
        desc=Label(self.root,text="Admin Login Area",font=("Goudy old style",15,"bold","underline"),fg="orange",bg="white").place(x=875,y=195)

        email=Label( self.root,text="Email ", font=("times new roam", 20, "bold"), bg="white", fg="black").place(x=750, y=260)
        self.email= Entry(self.root, font=("times new roman", 15),bg="lightgray")
        self.email.place(x=750, y=305, width=350,height=40)

        self.pasw = Label(self.root,text="Password ", font=("times new roam", 20, "bold"), bg="white", fg="black").place(x=755, y=360)
        self.pasw= Entry(self.root,font=("times new roman", 15),bg="lightgray",show="*")
        self.pasw.place(x=750, y=405, width=350,height=40)

        forget_btn = Button(self.root,text="Forgot Password?",bg="white",fg="red",bd=0,font=("times new roman",13),
                            command=self.email_frgt,).place(x=1020,y=455)

        Login_btn = Button( self.root,text="Submit ", bg="white", fg="red",font=("times new roman", 20),cursor='hand2',
                           command=self.log_fun).place(x=895, y=505)
#################################################################################
        #######################################################################################################3#
        home_btn = Button(self.root, text="Home", bg="white", fg="black", font=("times new roman", 17),
                          cursor='hand2', bd=2,command=self.new013_window).place(x=0, y=0, width=215)
        admin_btn = Button(self.root, text="Doctor", bg="white", fg="black", font=("times new roman", 17),
                           cursor='hand2', bd=2,command=self.new014_window).place(x=215, y=0, width=215)
        doctor_btn = Button(self.root, text="patient", bg="white", fg="black", font=("times new roman", 17),
                            cursor='hand2', bd=2,command=self.new015_window).place(x=430, y=0, width=215)
        patient_btn = Button(self.root, text="Admin", bg="white", fg="black", font=("times new roman", 17),
                             cursor='hand2', bd=2).place(x=645, y=0, width=215)
        abt_btn = Button(self.root, text="Developed By", bg="white", fg="black", font=("times new roman", 17),
                         cursor='hand2', bd=2,command=self.pic_window).place(x=860, y=0, width=215)
        cnt_btn = Button(self.root, text="Back", bg="white", fg="black", font=("times new roman", 17),
                         cursor='hand2', bd=2,command=self.back_window).place(x=1075, y=0, width=215)

    def new013_window(self):
        self.new_window = Toplevel(self.root)
        self.app = login(self.new_window)

    def new014_window(self):
        self.new_window = Toplevel(self.root)
        self.app = doctor_login(self.new_window)

    def new015_window(self):
        self.new_window = Toplevel(self.root)
        self.app = user_login(self.new_window)

    def pic_window(self):
        self.new_window = Toplevel(self.root)
        self.app = pic_page(self.new_window)

    def back_window(self):
        self.new_window = Toplevel(self.root)
        self.app = login(self.new_window)

    # def new016_window(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = admin_login(self.new_window)

    # def new17_window(self):
    #    self.new_window = Toplevel(self.root)
    #   self.app = (self.new_window)
    # def new18_window(self):
    #   self.new_window = Toplevel(self.root)
    #   self.app = frgt(self.new_window)

    def log_fun(self):
        if self.email.get() == "" or self.pasw.get() == "":
             messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="project")
                cur = con.cursor()
                cur.execute("select * from adm_reg where email=%s and password=%s",(self.email.get(), self.pasw.get()))
                row = cur.fetchone()
                if row == None:
                        messagebox.showerror("Error", "Invalid username & password", parent=self.root)
                else:
                    open_main = messagebox.askyesno("Error", "Welcome yes to continue",parent=self.root)
                    if open_main > 0:
                        self.new_window = Toplevel(self.root)
                        self.app = admin_final_page(self.new_window)
                    else:
                        if not open_main:
                            return
                con.commit()
                con.close()
            except Exception as es:
                  messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)


    def email_frgt(self):
        if self.email.get()=="":
            messagebox.showerror("Error","Enter email address to reset password",parent=self.root)
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="project")
            cur = con.cursor()
            query=("select * from adm_reg where email=%s")
            value=(self.email.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Enter the valid email-id",parent=self.root)
            else:
                con.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x400+400+150")
                self.root2.focus_force()
                self.root2.grab_set()
                self.root2.config(bg="white")

                Frame_login = Frame(self.root2, bg="#E3E3E3",bd=5,relief=RIDGE)
                Frame_login.place(x=12, y=20, height=350, width=376)

                title = Label(self.root2, text="  Forgot Password  ", font=("Goudy old style", 23, "bold", "underline"),
                              fg="black", bg="#EAEAEA",bd=2,relief=RIDGE)
                title.place(x=82, y=30)

                question = Label(self.root2, text="Security question", font=("times new roam", 15, "bold"), bg="#E3E3E3",
                                 fg="black").place(x=20, y=100)
                self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 15), state='readonly', justify=CENTER)
                self.cmb_quest['value'] = ("Select", "Year of born", "Pet dog name", "Birth place", "Favourite Actor","Best friend name")
                self.cmb_quest.place(x=20, y=130, width=300)
                self.cmb_quest.current(0)

                ans = Label(self.root2, text="Answer", font=("times new roam", 15, "bold"), bg="#E3E3E3",
                            fg="black").place(x=20, y=180)
                self.ans = Entry(self.root2, font=("times new roman", 15), bg="white")
                self.ans.place(x=20, y=210, width=300)

                new_pass = Label(self.root2, text="New password", font=("times new roam", 15, "bold"), bg="#E3E3E3",
                                 fg="black").place(x=20, y=260)
                self.new_pass = Entry(self.root2, font=("times new roman", 15), bg="white")
                self.new_pass.place(x=20, y=290, width=300)

                Login_btn = Button(self.root2, text="Reset password", bg="white", fg="red", font=("times new roman", 17),
                                   cursor='hand2',command=self.done_reset).place(x=120, y=340)

    def done_reset(self):
          if self.cmb_quest.get()=="Select":
              messagebox.showerror("Error","Select security question",parent=self.root2)
          elif self.ans.get()=="" or self.new_pass.get()=="":
              messagebox.showerror("Error","All fields are required",parent=self.root2)
          else:
              con = pymysql.connect(host="localhost", user="root", password="", database="project")
              cur = con.cursor()
              qury = ("select * from adm_reg where email=%s and cmb_quest=%s and answer=%s")
              value=(self.email.get(),self.cmb_quest.get(),self.ans.get())
              cur.execute(qury,value)
              row=cur.fetchone()
              if row==None:
                  messagebox.showerror("Error","Wrong Answer or Question",parent=self.root2)
              else:
                  query=("update adm_reg set password=%s where email=%s")
                  value=(self.new_pass.get(),self.email.get())
                  cur.execute(query,value)
                  messagebox.showinfo("Info","Your password as been rested,\n"
                                             "please enter the new password to login",parent=self.root2)

              con.commit()
              con.close()
              self.root2.destroy()


#     def new_window(self):
#         self.new_window = Toplevel(self.root)
#         self.app = frgt(self.new_window)
#
# class frgt:
#     def __init__(self,root):
#          #   self.root = Toplevel()
#             self.root=root
#             self.root.title("Forgot Password")
#             self.root.geometry("400x400+400+150")
#             self.root.focus_force()
#             self.root.grab_set()
#             self.root.config(bg="white")
#
#
#             Frame_login=Frame (self.root,bg="#E3E3E3")
#             Frame_login.place(x=12,y=20,height=350,width=376)
#
#             title = Label(self.root, text="  Forgot Password  ", font=("Goudy old style", 23 ,"bold","underline"), fg="black", bg="white")
#             title.place(x=82, y=30)
#
#             question = Label(self.root, text="Security question", font=("times new roam", 15, "bold"), bg="#E3E3E3",
#                          fg="black").place(x=20, y=100)
#             cmb_quest = ttk.Combobox(self.root, font=("times new roman", 15), state='readonly', justify=CENTER)
#             cmb_quest['value'] = ("Select", "Year of born", "Pet dog name", "Birth place","Favourite Actor")
#             cmb_quest.place(x=20, y=130, width=300)
#             cmb_quest.current(0)
#
#             ans = Label(self.root, text="Answer", font=("times new roam", 15, "bold"), bg="#E3E3E3",
#                          fg="black").place(x=20, y=180)
#             self.ans = Entry(self.root, font=("times new roman", 15), bg="white")
#             self.ans.place(x=20, y=210, width=300)
#
#             new_pass = Label(self.root, text="New password", font=("times new roam", 15, "bold"), bg="#E3E3E3",
#                          fg="black").place(x=20, y=260)
#
#             self.new_pass = Entry(self.root, font=("times new roman", 15), bg="white")
#             self.new_pass.place(x=20, y=290, width=300)
#
#             Login_btn = Button(self.root, text="Reset password", bg="white", fg="red", font=("times new roman", 17),cursor='hand2',
#                            command=self.frgt_fun,).place(x=120, y=340)
#
#
#     def frgt_fun(self):
#         if self.ans.get()=="" or self.new_pass.get()=="":
#              messagebox.showerror("Error","All fields are required",parent=self.root)

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

class admin_final_page:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin page")
        self.root.geometry("1350x700+0+0")
        # self.root.resizable(False,False)
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\admin.png')
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Login=Label(self.root, text=" Sun Shine Speciality Hospital ", bg="white", fg="black", font=("times new roman", 30,"underline"),
                           cursor='hand2').place(x=420,y=0,width=480)

        pat=Label(self.root, text=" Admin Area ", bg="white", fg="black", font=("times new roman", 25,"underline"),
                           cursor='hand2').place(x=560,y=47,width=220)

        ################################################################3

        home_btn = Button(self.root, text="Manage Doctors", bg="white", fg="black", font=("times new roman", 17),
                          cursor='hand2', bd=2,command=self.dct_chk_dct_chk).place(x=0, y=100, width=260)
        admin_btn = Button(self.root, text="Manage patient", bg="white", fg="black", font=("times new roman", 17),
                           cursor='hand2', bd=2,command=self.dct_chk_pat).place(x=260, y=100, width=260)
        doctor_btn = Button(self.root, text="Add New Admin", bg="white", fg="black", font=("times new roman", 17),
                            cursor='hand2', bd=2,command=self.adm_chk_newadm).place(x=520, y=100, width=255)
        patient_btn = Button(self.root, text="Developed By", bg="white", fg="black", font=("times new roman", 17),
                             cursor='hand2', bd=2,command=self.pic).place(x=775, y=100, width=255)
        cnt_btn = Button(self.root, text="Back", bg="white", fg="black", font=("times new roman", 17),
                         cursor='hand2', bd=2,command=self.back).place(x=1030, y=100, width=250)

    def dct_chk_dct_chk(self):
        self.new_window=Toplevel(self.root)
        self.app=dct_chk(self.new_window)

    def dct_chk_pat(self):
        self.new_window=Toplevel(self.root)
        self.app=mng_pat(self.new_window)

    def adm_chk_newadm(self):
        self.new_window = Toplevel(self.root)
        self.app = add_adm(self.new_window)

    def back(self):
        self.new_window = Toplevel(self.root)
        self.app = admin_login(self.new_window)

    def pic(self):
        self.new_window = Toplevel(self.root)
        self.app = pic_page(self.new_window)


#####################################################################################

class dct_chk:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Doctor")
        self.root.geometry("950x400+150+180")
        self.root.focus_force()
        self.root.resizable(False,False)

        #self.root.config(bg="white")
        # self.root.resizable(False,False)

        DataFrame = LabelFrame(self.root, bd=8,padx=16,bg="#FFEFDB",relief=RIDGE,font=("times new roman", 13),text="Registerd Doctors")
        DataFrame.place(x=10,y=20,width=930,height=350)


        add_dctlab = Label(DataFrame, text="To Add New Doctor", fg="black", bg="#FFEFDB", bd=0, font=("times new roman",15),
                         cursor='hand2').place(x=10, y=235)

        view_appolab = Label(DataFrame, text="To View Patient Appointment", bg="#FFEFDB", fg="black", font=("times new roman", 15),
                           cursor='hand2').place(x=10, y=280)

        add_dct = Button(DataFrame, text="Click here!", fg="red", bg="#FFEFDB", bd=0, font=("times new roman",12),
                         cursor='hand2',command=self.dct_chk_add_dct).place(x=180, y=235)

        view_appo = Button(DataFrame, text="Click here!", bg="#FFEFDB", fg="red", font=("times new roman", 12),bd=0,
                           cursor='hand2',command=self.dct_chk_dct_app).place(x=265, y=280)

        connect= pymysql.connect(host="localhost", user="root", password="", database="project",port=3306)
        con = connect.cursor()
        con.execute("select * from dct_reg")
        tree=ttk.Treeview(DataFrame)
        tree['show']='headings'
        s=ttk.Style(DataFrame)
        s.theme_use("clam")
        tree["columns"]=("fname","lname","contact","email","state","dob","cmb_quest","answer","spcl","qualif","password")
        tree.column("fname", width=130, minwidth=50, anchor=tkinter.CENTER)
        tree.column( "lname",width=100,minwidth=50,anchor=tkinter.CENTER)
        tree.column("contact", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("email", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("state", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("dob", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("cmb_quest", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("answer", width=130, minwidth=50, anchor=tkinter.CENTER)
        tree.column("spcl",width=130,minwidth=50,anchor=tkinter.CENTER)
        tree.column("qualif", width=130, minwidth=50, anchor=tkinter.CENTER)
        tree.column("password", width=130, minwidth=50, anchor=tkinter.CENTER)

        tree.heading("fname",text="First Name",anchor=tkinter.CENTER)
        tree.heading("lname", text="Last Name", anchor=tkinter.CENTER)
        tree.heading("contact", text="Contact No", anchor=tkinter.CENTER)
        tree.heading("email", text="email", anchor=tkinter.CENTER)
        tree.heading("state", text="state", anchor=tkinter.CENTER)
        tree.heading("dob", text="date of birth", anchor=tkinter.CENTER)
        tree.heading("cmb_quest", text="Security Question", anchor=tkinter.CENTER)
        tree.heading("answer", text="Answer", anchor=tkinter.CENTER)
        tree.heading("spcl", text="Specilization", anchor=tkinter.CENTER)
        tree.heading("qualif", text="Qualification", anchor=tkinter.CENTER)
        tree.heading("password", text="Password", anchor=tkinter.CENTER)

        i=0
        for rows in con:
            tree.insert('',i,text="",values=(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9],rows[10]))
            i=i+1
        tree.pack()


    def dct_chk_add_dct(self):
        self.new_window = Toplevel(self.root)
        self.app = add_dct(self.new_window)

    def dct_chk_dct_app(self):
        self.new_window = Toplevel(self.root)
        self.app = dct_app(self.new_window)



class add_dct:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin page")
        self.root.geometry("720x530+250+100")
        # self.root.resizable(False,False)
        self.root.config(bg="white")

        DataFrametop = LabelFrame(self.root, bd=8,padx=16,bg="white",relief=RIDGE,font=("times new roman", 15),text="Fill Doctor Details")
        DataFrametop.place(x=19,y=20,width=680,height=480)


        fname = Label(DataFrametop, text="Doctor First Name", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(
            x=30, y=20)
        self.fname = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.fname.place(x=30, y=50, width=250)

        lname = Label(DataFrametop, text="Last Name", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(
            x=340, y=20)
        self.lname = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.lname.place(x=340, y=50, width=250)

        contact = Label(DataFrametop, text="Contact No", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(
            x=30, y=85)
        self.contact = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.contact.place(x=30, y=115, width=250)

        email = Label(DataFrametop, text="Email", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(x=340,y=85)
        self.email = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.email.place(x=340, y=115, width=250)

        ####
        state = Label(DataFrametop, text="State", font=("times new roam", 15, "bold"), bg="white",
                         fg="grey").place(x=30, y=150)
        self.state = ttk.Combobox(DataFrametop, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.state['value'] = ("Select", "Andra Pradesh", "Assam", "Bihar","Chattisgarh","Gujarat","Haryana","Jharkhand","Karnataka","Kerala","Maharastra","Odisha","Punjab","Rajasthan","Tamil Nadu","Telagana","Uttar Pradesh","West Bengal")
        self.state.place(x=30, y=180, width=250)
        self.state.current(0)

        dob = Label(DataFrametop, text="Date Of Birth", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(x=340,y=150)
        self.dob = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.dob.place(x=340, y=180, width=250)

        question = Label(DataFrametop, text="Security Question", font=("times new roam", 15, "bold"), bg="white",
                         fg="grey").place(x=30, y=215)
        self.cmb_quest = ttk.Combobox(DataFrametop, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_quest['value'] = ("Select", "Pet dog name","Birtn place","Best friend name")
        self.cmb_quest.place(x=30, y=245, width=250)
        self.cmb_quest.current(0)

        answer = Label(DataFrametop, text="Answer", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(
            x=340, y=215)
        self.answer = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.answer.place(x=340, y=245, width=250)

        ###
        spcl = Label(DataFrametop, text="Specialization", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(
            x=30, y=280)
        self.spcl = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.spcl.place(x=30, y=315, width=250)

        qualif = Label(DataFrametop, text="Qualification", font=("times new roam", 15, "bold"), bg="white",
                          fg="grey").place(x=340, y=280)
        self.qualif = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.qualif.place(x=340, y=315, width=250)

        password = Label(DataFrametop, text="Password", font=("times new roam", 15, "bold"), bg="white", fg="grey").place(
            x=30, y=350)
        self.password = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.password.place(x=30, y=380, width=250)

        cpassword = Label(DataFrametop, text="Confirm Password", font=("times new roam", 15, "bold"), bg="white",
                          fg="grey").place(x=340, y=350)
        self.cpassword = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.cpassword.place(x=340, y=380, width=250)

        reg = Button(self.root, text="  Register  ", font=("times new roam", 17, "bold"), bg="green",
                          fg="white",command=self.login_function).place(x=300, y=470)


    def clear(self):
        self.fname.delete(0,END)
        self.lname.delete(0, END)
        self.contact.delete(0, END)
        self.email.delete(0, END)
        self.state.delete(0, END)
        self.dob.delete(0, END)
        self.spcl.delete(0,END)
        self.qualif.delete(0,END)
        self.answer.delete(0, END)
        self.password.delete(0, END)
        self.cpassword.delete(0,END)
        self.cmb_quest.current(0)


    def login_function(self):
        if self.fname.get()=="" or self.lname.get()=="" or self.email.get() == "" or self.password.get() == ""or \
                self.cpassword.get() == "" or self.answer.get() == ""or self.contact.get()==""\
                or self.cmb_quest.get()=="Select" or self.state.get()=="Select" or self.dob.get()=="" \
                or self.spcl.get() == ""or self.qualif.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.password.get()!=self.cpassword.get():
            messagebox.showerror("Error","Password and Confirm Password are not same",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="project")
                cur=con.cursor()
                cur.execute("Select * from dct_reg where email=%s",self.email.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error"," User already exits,please try with another email",parent=self.root)
                else:
                     cur.execute("insert into dct_reg (fname,lname,contact,email,state,dob,cmb_quest,answer,spcl,qualif,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.fname.get(),
                         self.lname.get(),
                         self.contact.get(),
                         self.email.get(),
                         self.state.get(),
                         self.dob.get(),
                         self.cmb_quest.get(),
                         self.answer.get(),
                         self.spcl.get(),
                         self.qualif.get(),
                         self.password.get(),
                         ))
                     con.commit()
                     con.close()
                     messagebox.showinfo("Success","Registered", parent=self.root)
                     self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

class dct_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Doctor")
        self.root.geometry("950x400+150+180")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)

        DataFrameapp = LabelFrame(self.root, bd=8,padx=16,bg="#EAEAEA",relief=RIDGE,font=("times new roman", 13),text="Appointments")
        DataFrameapp.place(x=10,y=20,width=930,height=350)


        connect= pymysql.connect(host="localhost", user="root", password="", database="project",port=3306)
        con = connect.cursor()
        con.execute("select * from appointment")
        tree=ttk.Treeview(DataFrameapp)
        tree['show']='headings'
        s=ttk.Style(DataFrameapp)
        s.theme_use("clam")
        tree["columns"]=("pat_name","gender","age","cno","address","symptoms","date","doctor")
        tree.column( "pat_name",width=100,minwidth=50,anchor=tkinter.CENTER)
        tree.column("gender", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("age", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("cno", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("address", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("symptoms", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("date", width=130, minwidth=50, anchor=tkinter.CENTER)
        tree.column( "doctor",width=130,minwidth=50,anchor=tkinter.CENTER)

        tree.heading("pat_name",text="Patient name",anchor=tkinter.CENTER)
        tree.heading("gender", text="Gender", anchor=tkinter.CENTER)
        tree.heading("age", text="Age", anchor=tkinter.CENTER)
        tree.heading("cno", text="Contact Number", anchor=tkinter.CENTER)
        tree.heading("address", text="Address", anchor=tkinter.CENTER)
        tree.heading("symptoms", text="Symptoms", anchor=tkinter.CENTER)
        tree.heading("date", text="Appointment Date", anchor=tkinter.CENTER)
        tree.heading("doctor", text="Appointed Doctor", anchor=tkinter.CENTER)

        i=0
        for rows in con:
            tree.insert('',i,text="",values=(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7]))
            i=i+1
        tree.pack()


###############################################################################################
#                                        Manage Patients
            #############################################################################################################


class mng_pat:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Patient")
        self.root.geometry("950x350+150+180")
        self.root.config(bg="white")
        self.root.resizable(False,False)
        self.root.focus_force()
        DataFrameapp = LabelFrame(self.root, bd=8,padx=16,bg="#EAEAEA",relief=RIDGE,font=("times new roman", 13),text="Patient Details")
        DataFrameapp.place(x=10,y=20,width=930,height=300)

        add_reg = Button(self.root, text=" Register New Patient ", fg="black", bg="white", bd=5, font=("times new roman",17),
                         cursor='hand2',command=self.adm_Register).place(x=200, y=290)

        view_appo = Button(self.root, text=" Book Appointment ", bg="white", fg="black",font=("times new roman", 17),bd=5,
                           cursor='hand2',command=self.adm_appointment).place(x=550, y=290)


        connect= pymysql.connect(host="localhost", user="root", password="", database="project",port=3306)
        con = connect.cursor()
        con.execute("select * from appointment")
        tree=ttk.Treeview(DataFrameapp)
        tree['show']='headings'
        s=ttk.Style(DataFrameapp)
        s.theme_use("clam")
        tree["columns"]=("pat_name","gender","age","cno","address","symptoms","date","doctor")
        tree.column( "pat_name",width=100,minwidth=50,anchor=tkinter.CENTER)
        tree.column("gender", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("age", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("cno", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("address", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("symptoms", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("date", width=130, minwidth=50, anchor=tkinter.CENTER)
        tree.column( "doctor",width=130,minwidth=50,anchor=tkinter.CENTER)

        tree.heading("pat_name",text="Patient name",anchor=tkinter.CENTER)
        tree.heading("gender", text="Gender", anchor=tkinter.CENTER)
        tree.heading("age", text="Age", anchor=tkinter.CENTER)
        tree.heading("cno", text="Contact Number", anchor=tkinter.CENTER)
        tree.heading("address", text="Address", anchor=tkinter.CENTER)
        tree.heading("symptoms", text="Symptoms", anchor=tkinter.CENTER)
        tree.heading("date", text="Appointment Date", anchor=tkinter.CENTER)
        tree.heading("doctor", text="Appointed Doctor", anchor=tkinter.CENTER)

        i=0
        for rows in con:
            tree.insert('',i,text="",values=(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7]))
            i=i+1
        tree.pack()


    def adm_Register(self):
        self.new_widow=Toplevel(self.root)
        self.app=Register(self.new_widow)

    def adm_appointment(self):
        self.new_widow=Toplevel(self.root)
        self.app=pat01_page(self.new_widow)

##########################################################################@@@@@@@@@@@
####################################                                                    #######################3


# #######################3
#######################################@@@@@@@@@@@
####################################                                                    #######################3


class add_adm:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin page")
        self.root.geometry("720x560+250+100")
        self.root.resizable(False,False)
        self.root.config(bg="white")
        self.root.focus_force()

        DataFrametop = LabelFrame(self.root, bd=8,padx=16,bg="#FFFFF0",relief=RIDGE,font=("times new roman", 15),text="Fill Admin Details")
        DataFrametop.place(x=19,y=20,width=680,height=510)


        fname = Label(DataFrametop, text="First Name", font=("times new roam", 15, "bold"), bg="#FFFFF0", fg="grey").place(
            x=30, y=20)
        self.fname = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.fname.place(x=30, y=50, width=250)

        lname = Label(DataFrametop, text="Last Name", font=("times new roam", 15, "bold"), bg="#FFFFF0", fg="grey").place(
            x=340, y=20)
        self.lname = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.lname.place(x=340, y=50, width=250)

        contact = Label(DataFrametop, text="Contact No", font=("times new roam", 15, "bold"), bg="#FFFFF0", fg="grey").place(
            x=30, y=85)
        self.contact = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.contact.place(x=30, y=115, width=250)

        email = Label(DataFrametop, text="Email", font=("times new roam", 15, "bold"), bg="#FFFFF0", fg="grey").place(x=340,y=85)
        self.email = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.email.place(x=340, y=115, width=250)#FFFFF0

        ####
        state = Label(DataFrametop, text="State", font=("times new roam", 15, "bold"), bg="#FFFFF0",
                         fg="grey").place(x=30, y=150)
        self.state = ttk.Combobox(DataFrametop, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.state['value'] = ("Select", "Andra Pradesh", "Assam", "Bihar","Chattisgarh","Gujarat","Haryana","Jharkhand","Karnataka","Kerala","Maharastra","Odisha","Punjab","Rajasthan","Tamil Nadu","Telagana","Uttar Pradesh","West Bengal")
        self.state.place(x=30, y=180, width=250)
        self.state.current(0)

        dob = Label(DataFrametop, text="Date Of Birth", font=("times new roam", 15, "bold"), bg="#FFFFF0", fg="grey").place(x=340,y=150)
        self.dob = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.dob.place(x=340, y=180, width=250)

        question = Label(DataFrametop, text="Security Question", font=("times new roam", 15, "bold"), bg="#FFFFF0",
                         fg="grey").place(x=30, y=215)
        self.cmb_quest = ttk.Combobox(DataFrametop, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_quest['value'] = ("Select", "Pet dog name","Birtn place","Best friend name")
        self.cmb_quest.place(x=30, y=245, width=250)
        self.cmb_quest.current(0)

        answer = Label(DataFrametop, text="Answer", font=("times new roam", 15, "bold"), bg="#FFFFF0", fg="grey").place(
            x=340, y=215)
        self.answer = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.answer.place(x=340, y=245, width=250)

        ###
        jdate = Label(DataFrametop, text="Joining Date", font=("times new roam", 15, "bold"), bg="#FFFFF0", fg="grey").place(
            x=30, y=280)
        self.jdate = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.jdate.place(x=30, y=315, width=250)

        qualif = Label(DataFrametop, text="Qualification", font=("times new roam", 15, "bold"), bg="#FFFFF0",
                          fg="grey").place(x=340, y=280)
        self.qualif = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.qualif.place(x=340, y=315, width=250)

        password = Label(DataFrametop, text="Password", font=("times new roam", 15, "bold"), bg="#FFFFF0", fg="grey").place(
            x=30, y=350)
        self.password = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.password.place(x=30, y=380, width=250)

        cpassword = Label(DataFrametop, text="Confirm Password", font=("times new roam", 15, "bold"), bg="#FFFFF0",
                          fg="grey").place(x=340, y=350)
        self.cpassword = Entry(DataFrametop, font=("times new roman", 15), bg="lightgray")
        self.cpassword.place(x=340, y=380, width=250)

        reg = Button(self.root, text="  Register  ", font=("times new roam", 13, "bold"), bg="green",
                         fg="white",command=self.login_function,bd=3).place(x=530, y=460)

        reg_view = Button(self.root, text=" View Registered Admins ", font=("times new roam", 18, "bold"), bg="white",
                          fg="black",bd=5,command=self.adm_chk_admview).place(x=185, y=500)


    def adm_chk_admview(self):
        self.new_window = Toplevel(self.root)
        self.app = adm_pat(self.new_window)


    def clear(self):
        self.fname.delete(0,END)
        self.lname.delete(0, END)
        self.contact.delete(0, END)
        self.email.delete(0, END)
        self.state.delete(0, END)
        self.dob.delete(0, END)
        self.jdate.delete(0,END)
        self.qualif.delete(0,END)
        self.answer.delete(0, END)
        self.password.delete(0, END)
        self.cpassword.delete(0,END)
        self.cmb_quest.current(0)


    def login_function(self):
        if self.fname.get()=="" or self.lname.get()=="" or self.email.get() == "" or self.password.get() == ""or \
                self.cpassword.get() == "" or self.answer.get() == ""or self.contact.get()==""\
                or self.cmb_quest.get()=="Select" or self.state.get()=="Select" or self.dob.get()=="" \
                or self.jdate.get() == ""or self.qualif.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.password.get()!=self.cpassword.get():
            messagebox.showerror("Error","Password and Confirm Password are not same",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="project")
                cur=con.cursor()
                cur.execute("Select * from adm_reg where email=%s",self.email.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error"," User already exits,please try with another email",parent=self.root)
                else:
                     cur.execute("insert into adm_reg (fname,lname,contact,email,state,dob,cmb_quest,answer,jdate,qualif,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.fname.get(),
                         self.lname.get(),
                         self.contact.get(),
                         self.email.get(),
                         self.state.get(),
                         self.dob.get(),
                         self.cmb_quest.get(),
                         self.answer.get(),
                         self.jdate.get(),
                         self.qualif.get(),
                         self.password.get(),
                         ))
                     con.commit()
                     con.close()
                     messagebox.showinfo("Success","Registered", parent=self.root)
                     self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)


class adm_pat:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin View")
        self.root.geometry("950x350+150+180")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)

        DataFrameapp = LabelFrame(self.root, bd=8,padx=16,bg="#EAEAEA",relief=RIDGE,font=("times new roman", 15),text="Admin List")
        DataFrameapp.place(x=10,y=20,width=930,height=310)


        connect= pymysql.connect(host="localhost", user="root", password="", database="project",port=3306)
        con = connect.cursor()
        con.execute("select * from adm_reg")
        tree=ttk.Treeview(DataFrameapp)
        tree['show']='headings'
        s=ttk.Style(DataFrameapp)
        s.theme_use("clam")
        tree["columns"]=("fname","lname","contact","email","state","dob","cmb_quest","answer","jdate","qualif","password")
        tree.column( "fname",width=100,minwidth=50,anchor=tkinter.CENTER)
        tree.column("lname", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("contact", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("email", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("state", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("dob", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("cmb_quest", width=130, minwidth=50, anchor=tkinter.CENTER)
        tree.column( "answer",width=130,minwidth=50,anchor=tkinter.CENTER)
        tree.column("jdate", width=100, minwidth=50, anchor=tkinter.CENTER)
        tree.column("qualif", width=130, minwidth=50, anchor=tkinter.CENTER)
        tree.column( "password",width=130,minwidth=50,anchor=tkinter.CENTER)

        tree.heading("fname",text="First Name",anchor=tkinter.CENTER)
        tree.heading("lname", text="Last Name", anchor=tkinter.CENTER)
        tree.heading("contact", text="Contact Number", anchor=tkinter.CENTER)
        tree.heading("email", text="Email", anchor=tkinter.CENTER)
        tree.heading("state", text="State", anchor=tkinter.CENTER)
        tree.heading("dob", text="Date of Birth", anchor=tkinter.CENTER)
        tree.heading("cmb_quest", text="Security Question", anchor=tkinter.CENTER)
        tree.heading("answer", text="Answer", anchor=tkinter.CENTER)
        tree.heading("jdate", text="joining Date", anchor=tkinter.CENTER)
        tree.heading("qualif", text="Qualification", anchor=tkinter.CENTER)
        tree.heading("password", text="Password", anchor=tkinter.CENTER)

        i=0
        for rows in con:
            tree.insert('',i,text="",values=(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9],rows[10]))
            i=i+1
        tree.pack()

class pic_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Sign Up")
        self.root.geometry("1600x900+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file='C:\\Users\\thuku\\OneDrive\\Desktop\\Mini_Project\\developedby.png')
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        Login=Label(self.root, text=" Sun Shine Speciality Hospital ", bg="white", fg="black", font=("times new roman", 30,"underline"),
                           cursor='hand2').place(x=0,y=0,width=1290)

        pat=Label(self.root, text=" Developed by ", bg="white", fg="black", font=("times new roman", 25,"underline"),
                           cursor='hand2').place(x=0,y=47,width=1290)

        home_btn = Button(self.root, text="Home", bg="white", fg="black", font=("times new roman", 17),
                        cursor='hand2',bd=2,command=self.home1).place(x=0, y=90,width=215)

        admin_btn = Button(self.root, text="Doctor", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.home2).place(x=215, y=90, width=215)

        doctor_btn = Button(self.root, text="Patient", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.home3).place(x=430, y=90, width=215)

        patient_btn = Button(self.root, text="Admin", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2,command=self.home4).place(x=645, y=90, width=215)

        abt_btn = Button(self.root, text="Develped By", bg="white", fg="black", font=("times new roman", 17),
                      cursor='hand2', bd=2).place(x=860, y=90, width=215)

        cnt_btn = Button(self.root, text="Back", bg="white", fg="black", font=("times new roman", 17),
                          cursor='hand2', bd=2,command=self.home5).place(x=1075, y=90, width=215)

        DataFrameTop = Frame(self.root, bd=2,bg="#FFBEDB",relief=RIDGE)
        DataFrameTop.place(x=467, y=205,width=536,height=97)
        Login=Label(DataFrameTop, text="Thukaram Rao A.N.V", bg="#FFBEDB", fg="black", font=("times new roman",30),
                           cursor='hand2').place(x=0,y=10,width=400)
        Login=Label(DataFrameTop, text="( 1RL19CS001 )", bg="#FFBEDB", fg="black", font=("times new roman",15),
                           cursor='hand2').place(x=220,y=50,width=200)

        DataFrameMiddle = Frame(self.root, bd=2,bg="#FFBEDB",relief=RIDGE)
        DataFrameMiddle.place(x=467, y=380,width=536,height=97)
        Login = Label(DataFrameMiddle, text="Harsha Vardhan.S", bg="#FFBEDB", fg="black", font=("times new roman", 30),
                      cursor='hand2').place(x=0, y=10, width=400)
        Login = Label(DataFrameMiddle, text="( 1RL19CS031 )", bg="#FFBEDB", fg="black", font=("times new roman", 15),
                      cursor='hand2').place(x=220, y=50, width=200)

        DataFrameBottom= Frame(self.root, bd=2,bg="#FFBEDB",relief=RIDGE)
        DataFrameBottom.place(x=467, y=555,width=536,height=97)
        Login = Label(DataFrameBottom, text="Harshith Babu.K", bg="#FFBEDB", fg="black", font=("times new roman", 30),
                      cursor='hand2').place(x=0, y=10, width=400)
        Login = Label(DataFrameBottom, text="( 1RL19CS035 )", bg="#FFBEDB", fg="black", font=("times new roman", 15),
                      cursor='hand2').place(x=220, y=50, width=200)

    def home1(self):
        self.new_window = Toplevel(self.root)
        self.app = login(self.new_window)

    def home2(self):
        self.new_window = Toplevel(self.root)
        self.app = doctor_login(self.new_window)

    def home3(self):
        self.new_window = Toplevel(self.root)
        self.app = user_login(self.new_window)

    def home4(self):
        self.new_window = Toplevel(self.root)
        self.app = admin_login(self.new_window)

    def home5(self):
        self.new_window = Toplevel(self.root)
        self.app =login(self.new_window)


if __name__== "__main__":
    main()