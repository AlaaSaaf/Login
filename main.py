from tkinter import *
from tkinter import messagebox

root = Tk() #Initiate a blank window
root.resizable('0','0') #disable widthxheight resize
root.title("LOGIN") #add a title to app
root.iconbitmap("login.ico") #import an icon to app
root.geometry("220x200") #fixe widthxheight
nm = StringVar() #initiate user variable
ps = StringVar() #initiate pass variable

def Sign():
    fu = open("AllUsers.txt","a+") #open&create txt file
    fp = open("AllPass.txt", "a+")
    fu.seek(0) #return always the cursor to the start position
    fp.seek(0)
    ra = fu.read() #read txt files
    rb = fp.read()
    a = ra.splitlines()#return a list that contain every line in txt file
    b = rb.splitlines()
    bo = True #initiate a boolean variable used later
    for i in range(len(a)):
        if ((a[i]==nm.get())and(b[i]!=ps.get())): #verify if the username already used
            messagebox._show(title="Info",message="UserName Already existe")#show a feedback window
            bo = False #no need to create another account
            break #break immediately from loop
        elif ((a[i]==nm.get())and(b[i]==ps.get())): #verify if the account already existe
            messagebox._show(title="Info", message="You Are In, Welcome Again")#a feedback messagebox
            bo = False
            break
    if bo : #if bo Still true that's mean we have a new user
        fu.write(nm.get() + "\n")#add Username
        fp.write(ps.get() + "\n")#add Password
        messagebox._show(title="Info", message="Done!,You Are in")#a feedback
    fu.close()#close txt file
    fp.close()

#------------------------------------------------Design-----------------------------------------------------------------
bg = PhotoImage(file="cover.png")#import our bg cover
lb = Label(root, image=bg)#put it on a label
Namelb = Label(root,text="UserName:", relief="solid", bd="1px", bg="#33658A",fg="white") #add UserName label
Name = Entry(root, textvariable=nm)#Entry of Username
Passlb = Label(root,text="Password:", relief="solid", bd="1px", bg="#33658A",fg="white")
Pass = Entry(root, textvariable=ps, show="*")
Log = Button(root, text="Enter", relief="solid", bd="1px", command=Sign)##button to login
Namelb.grid(row="0",column="0",ipadx="1px",sticky="E") #placement of element using grid method
Name.grid(row="0",column="1")
Passlb.grid(row="1",column="0",ipadx="2px",sticky="E")
Pass.grid(row="1",column="1")
Log.grid(row=2,column=1,ipadx="15px", pady="80px")
lb.place(x=0, y=0, relwidth=1, relheight=1)#another method to place our background
#-----------------------------------------------------------------------------------------------------------------------
root.mainloop()#run the app

