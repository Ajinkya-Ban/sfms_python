from tkinter import *
from tkinter import messagebox
import os
import subprocess
import pymysql

def loadCursor(event):
    txt_user.focus()

def openWindow():
    # to open another window
    subprocess.Popen(["python", "home.py"])
    # to close existing window
    window.destroy()

def clearFilds(event):
    txt_user.delete('0',END)
    txt_password.delete('0',END)
    txt_user.focus()

# this code is used for shortcut evenet
def clearFilds1():
    txt_user.delete('0',END)
    txt_password.delete('0',END)
    txt_user.focus()

def checkLogin():

    txtusername = txt_user.get()
    txtpassword = txt_password.get()
    check = 0
    if txtusername == "":
        messagebox.showinfo("Login","please enter username")
        txt_user.focus()
    elif txtpassword == "":
        messagebox.showinfo("Login", "please enter password")
        txt_password.focus()
    else:
        try:
            db = pymysql.connect(host="localhost",user="root",passwd="admin123",db="sfms")
            cur = db.cursor()
            sqlquery = "select * from tbl_login"
            cur.execute(sqlquery)
            result = cur.fetchall()
            for row in result:
                user_name_fromDB = row[1]
                user_pass_fromDB = row[2]
                if user_name_fromDB == txtusername and user_pass_fromDB == txtpassword:
                    check = 1
                    subprocess.Popen(["python", "home.py"])
                    window.destroy()
        except:
            messagebox.showinfo("Login","Unable to read data.")
        db.close()
        if check == 0:
            messagebox.showinfo("Login","please enter correct username and password")


# code shortcut keys

window = Tk()

# Change the size of window
window.geometry("400x160")
# change the title window
window.title("Login Form")
#change the icon of window
window.iconbitmap("")
#avoide the window resize
window.resizable(0,0)
#open the window at center of the screen
window.eval("tk::PlaceWindow . center")

#window.bind("<FocusIn>", loadCursor)

# code for the event binding for shortcut keys
window.bind_all("<Control-x>", clearFilds)


#window.configure(bg="lightgreen")

#icon for login button
btn_login_icon = PhotoImage(file="1.png")
btn_clear_icon = PhotoImage(file="2.png")

# create the title of application
lbl_title = Label(window,text="Login Form",font=("Roboto",15, "bold"), bg="Yellow", fg="red")
lbl_title.grid(row=0, column=1, pady=10, sticky="")

lbl_username = Label(window, text="Enter username", font="Arial 10 bold")
lbl_username.grid(row=1, column=0, padx=10)

txt_user = Entry(window, font="Arial 10", width=30)
txt_user.grid(row=1,column=1)


lbl_password = Label(window, text="Enter Password", font="Arial 10 bold")
lbl_password.grid(row=2, column=0, padx=10)

txt_password = Entry(window, font="Arial 10", width=30, show="*")
txt_password.grid(row=2,column=1,pady=10)

btn_login = Button(window, text="Login", font="Arial 10 bold", image=btn_login_icon, compound=RIGHT, command=checkLogin)
btn_login.grid(row=3, column=1, sticky="w")


btn_clear = Button(window, text="Clear", font="Arial 10 bold", image=btn_clear_icon, compound=LEFT, command=clearFilds1)
btn_clear.grid(row=3, column=1, sticky="e")


window.mainloop()