from tkinter import *
from tkinter import messagebox
import subprocess
def openNewUser():
    subprocess.Popen(["python", "new_user.py"])

window = Tk()

user_menu_img = PhotoImage(file="user_reg.png")
exit_img = PhotoImage(file="exit.png")

window.title("Main Form")
window.geometry("600x300")
window.iconbitmap("login.ico")
window.eval("tk::PlaceWindow . center")

#window.state('zoomed')
window.resizable(0,0)
#window.config(bg='#acb6e5')

menubar = Menu(window)
window.config(menu=menubar)

user_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="New User", menu=user_menu)
user_menu.add_command(label="New User Registration",command=openNewUser, accelerator="Ctrl+N", image=user_menu_img, compound=LEFT,underline=0)
user_menu.add_separator()
user_menu.add_command(label="Exit", accelerator="Ctrl+x", image=exit_img, compound=LEFT)

new_stud = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Student Registration", menu=new_stud)
new_stud.add_command(label="New Student Add", accelerator="Ctrl+N", image=user_menu_img, compound=LEFT,underline=0)
new_stud.add_command(label="Add Fees", accelerator="Ctrl+x", image=exit_img, compound=LEFT)
new_stud.add_command(label="Add Class", accelerator="Ctrl+x", image=exit_img, compound=LEFT)
new_stud.add_command(label="Add division", accelerator="Ctrl+x", image=exit_img, compound=LEFT)


window.mainloop()