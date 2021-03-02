from tkinter import *
root=Tk()
root.title("Registartion Form")

label1=Label(text="Registration Form", width=50,font=("bold",20) ).pack()   

name1 = Label(root, text = "Name ").pack()
name1= Entry(root)
name1.pack()

email=Label(root,text="E-mail").pack()
email=Entry(root)
email.pack()

num=Label(root,text="Enter Phone Number").pack()
num=Entry(root)
num.pack()

password=Label(root,text="Enter Password").pack()
password=Entry(root,show="*")
password.pack()

cnic=Label(root,text="Enter CNIC Number").pack()
cnic=Entry(root)
cnic.pack() 


def click():
   name=name1.get()
   s= name.capitalize()
   print(s) 

   number=num.get()  
   print(number)
   
   password1=password.get()
   print(password1)
   
   cnic1=cnic.get()
   print(cnic1)
   
   l1=Label(root,text=name).pack()
   l2=Label(root,text=number).pack()
   l3=Label(root,text=password1).pack()
   l4=Label(root,text=cnic1).pack()
   
btn=Button(root,text="Submit",command=click).pack()



root.mainloop()

