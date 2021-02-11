from tkinter import *
import pymysql
import os,sys



top=Tk()
top.title("Einstein")
first=Frame(top,height=1500,width=1500,bg='black')
first.propagate(0)
first.pack()

top2=Tk()
top2.title("Register")
f2=Frame(top2,width=400,height=550)
f2.pack()
   
en1=Entry(f2,width=25,fg="black")
en2=Entry(f2,width=25,fg="black")
en3=Entry(f2,width=25,fg="black")
en4=Entry(f2,width=25,fg="black")
en5=Entry(f2,width=25,fg="black",show='*')
en6=Entry(f2,width=25,fg="black")

top3=Tk()
top3.title("login")
f3=Frame(top3,width=300,height=250)
f3.propagate(1)

e1=Entry(f3,width=25,fg='blue',bg='white')
e2=Entry(f3,width=25,fg='blue',bg='white',show='*')
    
#========================================================================================================================================
#aregistraion form

def RegisterClick():


    #create label for registreation
    lb=Label(f2,text="Registration Form",font=('Times',20,'bold'),fg='black')
    lb1=Label(f2,text="First name:",fg="black")
    lb2=Label(f2,text="Last Name:",fg='black')
    lb3=Label(f2,text="Email id:",fg='black')
    lb4=Label(f2,text="Mobile No:",fg='black')
    lb5=Label(f2,text="Create Password:",fg='black')
    lb6=Label(f2,text="Gender:",fg='black')
    lb.place(x=100,y=30)
    lb1.place(x=1,y=105)
    lb2.place(x=1,y=155)
    lb3.place(x=1,y=205)
    lb4.place(x=1,y=255)
    lb5.place(x=1,y=305)
    lb6.place(x=1,y=355)
    
    
    #create entry box for registration fields
   
    en1.place(x=120,y=105)
    en2.place(x=120,y=155)
    en3.place(x=120,y=205)
    en4.place(x=120,y=255)
    en5.place(x=120,y=305)
    en6.place(x=120,y=355)


    #create button for register
    bt=Button(f2,text="Register",width=15,height=2,bg='green',fg='white',command=RegisterComplete)
    bt.place(x=70,y=405)
    bt1=Button(f2,text="Login",width=15,height=2,bg='blue',fg='white',command=Loginclick)
    bt1.place(x=200,y=405)
    top2.mainloop()
#==========================================================================================================================================================
    #database storage for registration
def RegisterComplete():

    name1=en1.get()
    name2=en2.get()
    email1=en3.get()
    mobile1=en4.get()
    passwd=en5.get()
    gender1=en6.get()
    connection=pymysql.connect('localhost','root','kajal123','einstein')
    cursor=connection.cursor();
    
    sql="""insert into registration(firstname,lastname,email_id,mobileno,password,gender) values('%s','%s','%s','%s','%s','%s')""" %(name1,name2,email1,mobile1,passwd,gender1)

    try:
       
        cursor.execute(sql)
        connection.commit();
        print("successfully inserted!!")

    except Exception as e:
        connection.rollback()
        print("Exception occured:",e)

#close db connection
    connection.close()
#====================================================================================================================================================
def travelpost():
    
    rt1=Tk()
    rt1.title("railway solution")
    fm=Frame(rt1,width=350,height=200,bg='gray')
    fm.pack()
    lb1=Label(fm,text="helpline number",fg='black',bg='gray',font=("Times",20,"bold"))
    lb1.place(x=100,y=50)
    lb2=Label(fm,text="1800-111-321",fg='black',bg='gray',font=("Times",20,"bold"))
    lb2.place(x=100,y=80)
    

    rt1.mainloop()

def edupost():
    
    rt1=Tk()
    rt1.title("education solution")
    fm=Frame(rt1,width=350,height=200,bg='gray')
    fm.pack()
    lb1=Label(fm,text="helpline number",fg='black',bg='gray',font=("Times",20,"bold"))
    lb1.place(x=100,y=50)
    lb2=Label(fm,text="1800-11-8004",fg='black',bg='gray',font=("Times",20,"bold"))
    lb2.place(x=100,y=80)
    

    rt1.mainloop()


def hygienepost():
    
    rt1=Tk()
    rt1.title("hygiene solution")
    fm=Frame(rt1,width=350,height=200,bg='gray')
    fm.pack()
    lb1=Label(fm,text="helpline number",fg='black',bg='gray',font=("Times",20,"bold"))
    lb1.place(x=100,y=50)
    lb2=Label(fm,text="1800-11-4000",fg='black',bg='gray',font=("Times",20,"bold"))
    lb2.place(x=100,y=80)
    

    rt1.mainloop()

def womenspost():
    
    rt1=Tk()
    rt1.title("womens solution")
    fm=Frame(rt1,width=350,height=200,bg='gray')
    fm.pack()
    lb1=Label(fm,text="helpline number",fg='black',bg='gray',font=("Times",20,"bold"))
    lb1.place(x=100,y=50)
    lb2=Label(fm,text="1091",fg='black',bg='gray',font=("Times",20,"bold"))
    lb2.place(x=100,y=80)
    

    rt1.mainloop()

def healthpost():
    
    rt1=Tk()
    rt1.title("health solution")
    fm=Frame(rt1,width=350,height=200,bg='gray')
    fm.pack()
    lb1=Label(fm,text="helpline number",fg='black',bg='gray',font=("Times",20,"bold"))
    lb1.place(x=100,y=50)
    lb2=Label(fm,text="1800-180-1104",fg='black',bg='gray',font=("Times",20,"bold"))
    lb2.place(x=100,y=80)
    

    rt1.mainloop()

def abusepost():
    
    rt1=Tk()
    rt1.title("abusement solution")
    fm=Frame(rt1,width=350,height=200,bg='gray')
    fm.pack()
    lb1=Label(fm,text="helpline number",fg='black',bg='gray',font=("Times",20,"bold"))
    lb1.place(x=100,y=50)
    lb2=Label(fm,text="9833092463",fg='black',bg='gray',font=("Times",20,"bold"))
    lb2.place(x=100,y=80)
    

    rt1.mainloop()
    



    
#====================================================================================================================================================
def travel():
    rt=Tk()
    rt.title("Railway")
    f4=Frame(rt,width=350,height=200,bg='gray')
    f4.propagate()
    f4.pack()

    lb1=Label(f4,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f4,width=50,fg="black")
    en1.place(x=120,y=5)

    b1=Button(f4,text='Post',height=2,width=15,bg='blue',fg='white',command=travelpost)
    b1.place(x=100,y=100)

    rt.mainloop()

    
    
    

def education():
    rt=Tk()
    rt.title("Education")
    f5=Frame(rt,width=350,height=200,bg="gray")
    f5.propagate()
    f5.pack()

    lb1=Label(f5,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f5,width=60,fg="black")
    en1.place(x=120,y=5)

    b1=Button(f5,text='Post',height=2,width=15,bg='blue',fg='white',command=edupost)
    b1.place(x=100,y=100)

    rt.mainloop()

def hygiene():
    rt=Tk()
    rt.title("Hygiene")
    f6=Frame(rt,width=350,height=200,bg="gray")
    f6.propagate()
    f6.pack()

    lb1=Label(f6,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f6,width=60,fg="black")
    en1.place(x=120,y=5)

    b1=Button(f6,text='Post',height=2,width=15,bg='blue',fg='white',command=hygienepost)
    b1.place(x=100,y=100)

def womensafety():
    rt=Tk()
    rt.title("Womensefety")
    f7=Frame(rt,width=350,height=200,bg="gray")
    f7.propagate()
    f7.pack()

    lb1=Label(f7,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f7,width=60,fg="black")
    en1.place(x=120,y=5)

    b1=Button(f7,text='Post',height=2,width=15,bg='blue',fg='white',command=womenspost)
    b1.place(x=100,y=100)
    rt.mainloop()
    
def health():
    rt=Tk()
    rt.title("Health")
    f8=Frame(rt,width=350,height=200,bg="gray")
    f8.propagate()
    f8.pack()

    lb1=Label(f8,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f8,width=60,fg="black")
    en1.place(x=120,y=5)

    b1=Button(f8,text='Post',height=2,width=15,bg='blue',fg='white',command=healthpost)
    b1.place(x=100,y=100)
    rt.mainloop()

def abusement():
    rt=Tk()
    rt.title("Abusement")
    f9=Frame(rt,width=350,height=300,bg="gray")
    f9.propagate()
    f9.pack()

    lb1=Label(f9,text="Problem Statement",fg='black',bg='gray')
    lb1.place(x=1,y=5)
    en1=Entry(f9,width=60,fg="black")
    en1.place(x=120,y=5)

    b1=Button(f9,text='Post',height=2,width=15,bg='blue',fg='white',command=abusepost)
    b1.place(x=100,y=100)
    rt.mainloop()


#====================================================================================================================================================
def sections():
    rt=Tk()
    rt.title("Sections")
    f4=Frame(rt,width=600,height=400,bg="black")
    f4.propagate()
    f4.pack()



    l1=Label(f4,text="Right to Speak",font=("Times",40,'bold italic'),fg='white',bg="black")
    l1.place(x=2,y=5)


    b1=Button(f4,text='Travel',height=2,width=15,bg='blue',fg='white',command=travel)
    b1.place(x=100,y=150)
    b2=Button(f4,text='Education',height=2,width=15,bg='blue',fg='white',command=education)
    b2.place(x=300,y=150)
    b3=Button(f4,text='Hygiene',height=2,width=15,bg='blue',fg='white',command=hygiene)
    b3.place(x=100,y=200)
    b4=Button(f4,text='Women Safety',height=2,width=15,bg='blue',fg='white',command=womensafety)
    b4.place(x=300,y=200)
    b5=Button(f4,text='Health',height=2,width=15,bg='blue',fg='white',command=health)
    b5.place(x=100,y=250)
    b6=Button(f4,text='Abusement',height=2,width=15,bg='blue',fg='white',command=abusement)
    b6.place(x=300,y=250)

    rt.mainloop()

#======================================================================================================================================================
def Logincomplete():

    user=e1.get()
    passwd=e2.get()

    if(user=="admin"):
        fname=open("logininfo.txt",'a+')
        fname.write("\n")
        fname.write(user)
        fname.write('\t')
        fname.write(passwd)
        fname.write('\n')
        fname.close()
        print("correct username and password!!!")
        sections()
       
    else:
        print("wrong username and password!!!!")

        
    
#create login form
def Loginclick():
    f3.pack()
    #create label for username and password
    lb=Label(f3,text="Login Form",fg="black",font=("Times",20,"bold"))
    l1=Label(f3,text="Username:",fg='black')
    l2=Label(f3,text="Password:",fg='black')
    lb.place(x=70,y=15)
    l1.place(x=30,y=70)
    l2.place(x=30,y=130)

    e1.place(x=100,y=70)
    e2.place(x=100,y=130)

    b3=Button(f3,text='Log in',height=2,width=15,bg='blue',fg='white',command=Logincomplete)
    b3.place(x=70,y=190)
    b4=Button(f3,text='New Account',height=2,width=13,bg='green',fg='white',command=RegisterClick)
    b4.place(x=190,y=190)
    top3.mainloop()
    
#=========#=================================================================================================================

#create a label for title og project
title1=Label(first,text="Einstein",height=1,width=7,font=('Times',80,'bold italic'),fg='white',bg='black')
title1.place(x=500,y=300)

b1=Button(first,text='Login',font=('Times',15),width=15,height=2,bg='Blue',fg='white',command=Loginclick)
b2=Button(first,text='Register',font=('Times',15),width=15,height=2,bg='green',fg='white',command=RegisterClick)
b2.place(x=5,y=5)
b1.place(x=180,y=5)

#============================================================================================================================


top.mainloop()
