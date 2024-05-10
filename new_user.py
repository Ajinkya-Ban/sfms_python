from tkinter import *
from tkinter.ttk import *
import pymysql as pysq
from tkinter import messagebox

myconn =pysq.connect(host="localhost", user="root",passwd="admin123", database="sfms")
cursor = myconn.cursor()

def center_content(tree):
    for col in tree["columns"]:
        tree.heading(col, anchor=CENTER)
        tree.column(col, anchor=CENTER)
def updateData(rows_afftected):
    trv.delete(*trv.get_children())
    for row in rows_afftected:
        trv.insert("", "end", values=row)

def searchdata():
    key2 = key.get()
    query="select * from tbl_studreg where sname LIKE '%"+key2+"%'"
    cursor.execute(query)
    rows_afftected = cursor.fetchall()
    updateData(rows_afftected)

def clearData():
    query="select * from tbl_studreg order by ID asc"
    cursor.execute(query)
    rows_afftected =cursor.fetchall()
    updateData(rows_afftected)
    entsearch.delete(0, END)
    entsearch.focus()

def getdataFromTreeView(event):
    row_id = trv.identify_row(event.y)
    items =trv.item(trv.focus())
    t1.set(items['values'][0])
    t2.set(items['values'][1])
    t3.set(items['values'][2])
    t4.set(items['values'][3])

def clearTextBoxes():
    entid.delete(0, END)
    entName.delete(0, END)
    entMob.delete(0, END)
    entAdd.delete(0,END)
    entid.focus() #focus cursor into ID entry.

# code for deleteing data from database.
def deleteStud():
    stud_id = t1.get()
    if messagebox.askyesno("Confirm Delete?","Do you want to delete this record?"):
        delquery="delete from tbl_studreg where ID="+stud_id
        cursor.execute(delquery)
        myconn.commit()
        clearTextBoxes()
        clearData()
    else:
        return True

def Insert_stud():
    sname = t2.get()
    smob= t3.get()
    sadd= t4.get()
    insert_query="insert into tbl_studreg(ID,sname,smob,sadd) values(NULL, %s,%s,%s)"
    cursor.execute(insert_query,(sname,smob,sadd))
    myconn.commit()
    messagebox.showinfo("Success","One record has been inserted.")
    clearData()
    clearTextBoxes()

def update_stud():
    sname = t2.get()
    smob= t3.get()
    sadd= t4.get()
    sid= t1.get()
    if messagebox.askyesno("Update","Do you want to update the record?"):
        update_query="update tbl_studreg set sname=%s, smob=%s,sadd=%s where ID=%s"
        cursor.execute(update_query,(sname,smob,sadd,sid))
        myconn.commit()
        clearData()
        clearTextBoxes()
    else:
        return True

window =Tk()

key=StringVar()
t1=StringVar() #Get ID from entry.
t2=StringVar() #Get Name from entry.
t3=StringVar() # Get mobile number from entry.
t4=StringVar() # get address from entry.

#Create 3 LabelFrames
f1 =LabelFrame(window, text="Display Student Information")
f2=LabelFrame(window, text="Insert Data")
f3=LabelFrame(window, text="Search Student Record")
f1.pack(fill="both", padx=10, pady=10, expand="yes")
f2.pack(fill="both", padx=10, pady=10, expand="no")
f3.pack(fill="both", padx=10, pady=10)

#creating treeview to display data from database
trv =Treeview(f1, columns=(1,2,3,4), height="10")
trv.pack(side=LEFT)
trv.place(x=0, y=0)

#creating heading of treeview

trv.heading("#1", text="ID")
trv.heading("#2", text="Student Name")
trv.heading("#3", text="Mobile")
trv.heading("#4", text="Address")

trv.column("#1", width=100, minwidth=50,anchor=CENTER)
trv.column("#2", width=100, minwidth=200)
trv.column("#3", width=100, minwidth=100)
trv.column("#4", width=100, minwidth=200)
center_content(trv)

#Create vertical scrollbars
yscrall = Scrollbar(f1, orient="vertical", command=trv.yview)
yscrall.pack(side=RIGHT, fill="y")

#Create horizontal scrollbars
xscrall = Scrollbar(f1, orient="horizontal", command=trv.xview)
xscrall.pack(side=BOTTOM, fill="x")

#Attach scrollbars to the window using configure
trv.configure(yscrollcommand=yscrall.set, xscrollcommand=xscrall.set)

#bind the event with treeview
trv.bind('<Double 1>', getdataFromTreeView)

#query for display data
query = "select * from tbl_studreg order by ID asc"
cursor.execute(query)
rows_afftected = cursor.fetchall()
updateData(rows_afftected)

#Search student record
lblsearch = Label(f3, text="Enter Name:")
lblsearch.pack(side=LEFT, padx=10)
entsearch=Entry(f3, textvariable=key)
entsearch.pack(side=LEFT, padx=6)

btnsearch=Button(f3, text="Search Data", command=searchdata)
btnsearch.pack(side=LEFT, padx=6)
btnclr = Button(f3, text="ClearData", command=clearData)
btnclr.pack(side=LEFT, padx=6)

#Insert Data Design Code

lblid=Label(f2, text="Enter Id")
lblid.grid(row=0, column=0,padx=5, pady=3)
entid = Entry(f2, width=20, textvariable=t1)
entid.grid(row=0, column=1, padx=5, pady=3)

lblname=Label(f2, text="Enter Name:")
lblname.grid(row=1, column=0, padx=5,pady=3)
entName=Entry(f2,  textvariable=t2)
entName.grid(row=1, column=1, padx=5,pady=3)

lblmob=Label(f2, text="Enter Mobile:")
lblmob.grid(row=2, column=0, padx=5,pady=3)
entMob=Entry(f2,  textvariable=t3)
entMob.grid(row=2, column=1, padx=5, pady=3)

lbladd=Label(f2, text="Enter address")
lbladd.grid(row=3, column=0, padx=5, pady=3)
entAdd=Entry(f2,  textvariable=t4)
entAdd.grid(row=3, column=1, padx=5, pady=3)

btn_add =Button(f2, text="Insert Data", command=Insert_stud)
btn_add.grid(row=4, column=0, padx=2,pady=3)
btn_update=Button(f2, text="Update Data", command=update_stud)
btn_update.grid(row=4, column=1, padx=2,pady=3)
btn_del =Button(f2, text="Delete Data", command=deleteStud)
btn_del.grid(row=5, column=1, padx=2, pady=3)
btn_clear=Button(f2, text="Clear Data", command=clearTextBoxes)
btn_clear.grid(row=5, column=0, padx=2, pady=2)

#set width of window
window.geometry("600x600")
window.title("Student Information System")
window.resizable(False, False)
window.mainloop()

