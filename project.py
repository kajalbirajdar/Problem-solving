from tkinter import *

root=Tk()
root.title("Quick Fix")
f=Frame(root,height=1000,width=1000,cursor="cross")
f.propagate(0)
f.pack()

#create a label for title of project
lb=Label(f,text="QUICK FIX",width=10,height=5,font=('Times',60,'bold italic'),fg='pink')
lb.grid(row=4,column=4)

def category():
    rt=Tk()
    rt.title("Categories")
    f3=Frame(rt,width=900,height=700)
    f3.propagate()
    f3.pack()



    l1=Label(f3,text="Welcome to Quick Fix",font=("Times",40,'bold italic'),fg='maroon')
    l2=Label(f3,text="Choose your category",fg='pink',font=("Times",30,'bold italic '))
    l1.place(x=2,y=5)
    l2.place(x=10,y=70)

    b1=Button(f3,text='Travel',height=2,width=15,bg='blue',fg='white',command=travel)
    b1.place(x=100,y=150)
    b2=Button(f3,text='Education',height=2,width=15,bg='blue',fg='white',command=education)
    b2.place(x=300,y=150)
    b3=Button(f3,text='Hygiene',height=2,width=15,bg='blue',fg='white',command=hygiene)
    b3.place(x=100,y=200)
    b4=Button(f3,text='Women Safety',height=2,width=15,bg='blue',fg='white',command=womensafety)
    b4.place(x=300,y=200)
    b5=Button(f3,text='Health',height=2,width=15,bg='blue',fg='white',command=health)
    b5.place(x=100,y=250)
    b6=Button(f3,text='Abusement',height=2,width=15,bg='blue',fg='white',command=abusement)
    b6.place(x=300,y=250)

def travel():
    rt=Tk()
    rt.title("Travel")
    f4=Frame(rt,width=400,height=300,bg='gray')
    f4.propagate()
    f4.pack()

    lb1=Label(f4,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f4,width=60,fg="black")
    en1.place(x=140,y=5)

    b1=Button(f4,text='Post',height=2,width=15,bg='blue',fg='white')
    b1.place(x=100,y=110)

    
    
    

def education():
    rt=Tk()
    rt.title("Education")
    f5=Frame(rt,width=400,height=300)
    f5.propagate()
    f5.pack()

    lb1=Label(f5,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f5,width=60,fg="black")
    en1.place(x=140,y=5)

    b1=Button(f5,text='Post',height=2,width=15,bg='blue',fg='white')
    b1.place(x=100,y=110)

def hygiene():
    rt=Tk()
    rt.title("Hygiene")
    f6=Frame(rt,width=400,height=300)
    f6.propagate()
    f6.pack()

    lb1=Label(f6,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f6,width=60,fg="black")
    en1.place(x=140,y=5)

    b1=Button(f6,text='Post',height=2,width=15,bg='blue',fg='white')
    b1.place(x=100,y=110)

def womensafety():
    rt=Tk()
    rt.title("Womensefety")
    f7=Frame(rt,width=400,height=300)
    f7.propagate()
    f7.pack()

    lb1=Label(f7,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f7,width=60,fg="black")
    en1.place(x=140,y=5)

    b1=Button(f4,text='Post',height=2,width=15,bg='blue',fg='white')
    b1.place(x=100,y=110)
    
def health():
    rt=Tk()
    rt.title("Health")
    f8=Frame(rt,width=400,height=300)
    f8.propagate()
    f8.pack()

    lb1=Label(f8,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f8,width=60,fg="black")
    en1.place(x=140,y=5)

    b1=Button(f8,text='Post',height=2,width=15,bg='blue',fg='white')
    b1.place(x=100,y=110)

def abusement():
    rt=Tk()
    rt.title("Abusement")
    f9=Frame(rt,width=400,height=300)
    f9.propagate()
    f9.pack()

    lb1=Label(f9,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f9,width=60,fg="black")
    en1.place(x=140,y=5)

    b1=Button(f9,text='Post',height=2,width=15,bg='blue',fg='white')
    b1.place(x=100,y=110)


    
def LoginClick():
    r1=Tk()
    r1.title("login")
    f1=Frame(r1,width=300,height=200)
    f1.propagate(1)
    f1.pack()

    #create label for username and password
    l1=Label(f1,text="Username:",fg='black')
    l2=Label(f1,text="Password:",fg='black')
    l1.place(x=1,y=5)
    l2.place(x=1,y=60)

    e1=Entry(f1,width=25,fg='blue',bg='white')
    e1.place(x=80,y=5)
    e2=Entry(f1,width=25,fg='blue',bg='white',show='*')
    e2.place(x=80,y=60)

    b3=Button(f1,text='Log in',height=2,width=15,bg='blue',fg='white',command=category)
    b3.place(x=100,y=120)
    r1.mainloop()
    

def SignupClick():
    r2=Tk()
    r2.title("Signup")
    f2=Frame(r2,width=400,height=500,bg="gray")
    f2.pack()
    #create label for registreation
    lb1=Label(f2,text="First name:",fg="black",bg='gray')
    lb2=Label(f2,text="Last Name:",fg="black",bg='gray')
    lb3=Label(f2,text="Email id:",fg="black",bg='gray')
    lb4=Label(f2,text="Mobile No:",fg="black",bg='gray')
    lb5=Label(f2,text="Create Password:",fg="black",bg='gray')
    lb6=Label(f2,text="Confirm Password:",fg="black",bg='gray')
    lb7=Label(f2,text="Gender",fg="black",bg='gray')
    lb1.place(x=1,y=5)
    lb2.place(x=1,y=55)
    lb3.place(x=1,y=105)
    lb4.place(x=1,y=155)
    lb5.place(x=1,y=205)
    lb6.place(x=1,y=255)
    lb7.place(x=1,y=305)
    
    
    #create entry box for registration fields
    en1=Entry(f2,width=25,fg="black")
    en2=Entry(f2,width=25,fg="black")
    en3=Entry(f2,width=25,fg="black")
    en4=Entry(f2,width=25,fg="black")
    en5=Entry(f2,width=25,fg="black",show='*')
    en6=Entry(f2,width=25,fg="black",show='*')
    en1.place(x=120,y=5)
    en2.place(x=120,y=55)
    en3.place(x=120,y=105)
    en4.place(x=120,y=155)
    en5.place(x=120,y=205)
    en6.place(x=120,y=255)

    #create radio buttons for Genders

    rb1=Radiobutton(f2,text="Female",value=1,bg='gray')
    rb2=Radiobutton(f2,text="Male",value=2,bg='gray')
    rb3=Radiobutton(f2,text="others",value=3,bg='gray')
    rb1.place(x=120,y=305)
    rb2.place(x=200,y=305)
    rb3.place(x=280,y=305)

    #create button for register
    bt=Button(f2,text="Register",width=15,height=2,bg='black',fg='white',command=LoginClick)
    bt.place(x=150,y=355)
    r2.mainloop()
    
#create buttons for login and sign up
b1=Button(f,text='Login',width=15,height=2,bg='Blue',fg='white',command=LoginClick)
b2=Button(f,text='sign up',width=15,height=2,bg='green',fg='white',command=SignupClick)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)


root.mainloop()

