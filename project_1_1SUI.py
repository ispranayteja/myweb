from tkinter import *
from tkinter import messagebox

def login():
    global fr1
    f=open("usernames.txt","r+")
    g=open("password.txt","r+")
    flis = f.readlines()
    glis = g.readlines()
    u=username.get()
    p=password.get()
    for i in range(len(flis)):
        if(u+'\n'==flis[i]):
            key1=i
    if(p+'\n'==glis[key1]):
        frame=Frame(window,bg='gold')
        frame.place(x=0,y=0,width=700,height=300)
        frame.tkraise()
        if(u=='ispt' and p+'\n'==glis[key1]):
            txt='isptadmin441.txt'
        else:
            txt=u+p+'.txt'
        f=open(txt,'r+')
        s1=f.readlines()
        lan = Label(frame,text="WELCOME "+s1[3][5:],fg='gold').grid(row=0)
        if(s1[6][11:]=='STUDENT'+'\n'):
            lan = Label(frame,text="welcome "+s1[6][11:]).grid(row=1)
            pran=((s1[12])+'.txt')
        else:
            lan = Label(frame,text="welcome "+s1[6][11:]).grid(row=1)
            pran=((s1[12])+'.txt')
        g=open(pran,'r+')
        glines=g.readlines()
        lab = Label(frame,text='SUBJECTS').grid(row=2)
        for i in range(len(glines)):
            but11=Button(frame,text=glines[i]).grid(row=2,column=i+1)
    else:
        lab=Label(frame1,text="wrong entries").grid(row=4)
    if(u=="ispt"):
        btu1 = Button(frame,text="users",command=opennow).grid(row=4)
    btu = Button(frame,text="logout",command=logout).grid(row=3)
    f.close()
    g.close()
    
def logout():
    ans=messagebox.askyesno('WARNING','do you want to log out')
    if ans:
        opening()

def opennow():
    from files import users_1

def accept(a,b,c,d,e11,h):
    track1=Frame(window3)
    window3.geometry('700x400')
    track1.place(x=0,y=0,width=700,height=400)
    track1.tkraise()
    clg=StringVar(window3)
    dep=StringVar(window3)
    l4 = Label(track1,text="COLLEGE DETAILS").grid(row=0)
    l4 = Label(track1,text="COLLEGE NAME").grid(row=1)
    e = Entry(track1,textvariable=clg).grid(row=1,column=1)
    l4 = Label(track1,text="DEPARTMENT").grid(row=2)
    rd1 = Radiobutton(track1,text="CIVIL",variable=dep,value="CIVIL").grid(row=2,column=1)
    rd2 = Radiobutton(track1,text="CSE",variable=dep,value="CSE").grid(row=2,column=2)
    rd1 = Radiobutton(track1,text="ECE",variable=dep,value="ECE").grid(row=2,column=3)
    rd2 = Radiobutton(track1,text="EEE",variable=dep,value="EEE").grid(row=2,column=4)
    rd1 = Radiobutton(track1,text="IT",variable=dep,value="IT").grid(row=2,column=5)
    rd2 = Radiobutton(track1,text="MECH",variable=dep,value="MECH").grid(row=2,column=6)

    if(h=="STUDENT"):
        num=StringVar(window3)
        var2=StringVar(window3)
        year=StringVar(window3)
        sem=StringVar(window3)
        l4 = Label(track1,text="COLLEGE REGISTRATION NUMBER").grid(row=3)
        e = Entry(track1,textvariable=num).grid(row=3,column=1)
        l4 = Label(track1,text="YEAR OF STUDY").grid(row=4)
        rd1 = Radiobutton(track1,text="I",variable=year,value="I").grid(row=4,column=1)
        rd2 = Radiobutton(track1,text="II",variable=year,value="II").grid(row=4,column=2)
        rd1 = Radiobutton(track1,text="III",variable=year,value="III").grid(row=4,column=3)
        rd2 = Radiobutton(track1,text="IV",variable=year,value="IV").grid(row=4,column=4)
        l4 = Label(track1,text="SEMESTER").grid(row=5)
        rd1 = Radiobutton(track1,text="I",variable=sem,value="I").grid(row=5,column=1)
        rd2 = Radiobutton(track1,text="II",variable=sem,value="II").grid(row=5,column=2)
        bb = Button(track1,text="SUBMIT",command=lambda:verify(a,b,c,d,e11,h,num.get(),year.get(),sem.get(),clg.get(),dep.get())).grid(row=6)
    else:
        spec=StringVar(window3)
        qual=StringVar(window3)
        l4 = Label(track1,text="QUALIFICATION").grid(row=3)
        rd1 = Radiobutton(track1,text="B.TECH",variable=qual,value="B.TECH").grid(row=3,column=1)
        rd2 = Radiobutton(track1,text="M.TECH",variable=qual,value="M.TECH").grid(row=3,column=2)
        rd1 = Radiobutton(track1,text="PH.D",variable=qual,value="PH.D").grid(row=3,column=3)
        l4 = Label(track1,text="SPECIALISATION").grid(row=4)
        e = Entry(track1,textvariable=spec).grid(row=4,column=1)
        bb1 = Button(track1,text="SUBMIT",command=lambda:verify1(a,b,c,d,e11,h,clg.get(),dep.get(),qual.get(),spec.get())).grid(row=5)
#for students verification
def verify(a,b,c,d,e11,h,m,n,o,r,s):
    window3.destroy()
    window2=Tk()
    fr=Frame(window2)
    fr.pack()
    window2.geometry('400x400')
    lb1 = Label(fr,text="YOUR SUBMISSION DETAILS").pack()
    lb5 = Label(fr,text="USERNAME:"+a).pack()
    lb6 = Label(fr,text="PASSWORD:"+b).pack()
    lb1 = Label(fr,text="NAME:"+c).pack()
    lb2 = Label(fr,text="GENDER:"+d).pack()
    lb4 = Label(fr,text="MAIL ID:"+e11).pack()
    lb7 = Label(fr,text="YOU ARE A :"+h).pack()
    lb3 = Label(fr,text="COLLEGE NAME:"+r).pack()
    lb4 = Label(fr,text="DEPARTMENT:"+s).pack()
    lb1 = Label(fr,text="COLLEGE REGISTERED NUMBER:"+m).pack()
    lb1 = Label(fr,text="YEAR OF STUDY:"+n).pack()
    lb1 = Label(fr,text="SEMESTER:"+o).pack()
    buttt=Button(fr,text="CONFIRM",command=lambda:window2.destroy()).pack()
    ans="DETAILS"+"\n"+"USERNAME:"+a+"\n"+"PASSWORD:"+b+"\n"+"NAME:"+c+"\n"+"GENDER:"+d+"\n"+"MAIL ID:"+e11+"\n"+"YOU ARE A :"+h+"\n"+"COLLEGE NAME:"+r+"\n"+"DEPARTMENT:"+s+"\n"+"COLLEGE REGISTERED NUMBER:"+m+"\n"+"YEAR OF STUDY:"+n+"\n"+"SEMESTER:"+o+'\n'+s+n+'_'+o
    z=open((a+b)+'.txt','a+')
    f=open("usernames.txt","a+")
    g=open("password.txt","a+")
    f.write(a+'\n')
    g.write(b+'\n')
    z.write(ans)
    f.close()
    g.close()
    z.close()
#for teachers verification
def verify1(a,b,c,d,e11,h,r,s,p,q):
    window3.destroy()
    window2=Tk()
    fr=Frame(window2)
    fr.pack()
    window2.geometry('300x300')
    lb1 = Label(fr,text="YOUR SUBMISSION DETAILS").pack()
    lb5 = Label(fr,text="USERNAME:"+a).pack()
    lb6 = Label(fr,text="PASSWORD:"+b).pack()
    lb1 = Label(fr,text="NAME:"+c).pack()
    lb2 = Label(fr,text="GENDER:"+d).pack()
    lb4 = Label(fr,text="MAIL ID:"+e11).pack()
    lb7 = Label(fr,text="YOU ARE A :"+h).pack()
    lb3 = Label(fr,text="COLLEGE NAME:"+r).pack()
    lb4 = Label(fr,text="DEPARTMENT:"+s).pack()
    lb1 = Label(fr,text="QUALIFICATION"+p).pack()
    lb1 = Label(fr,text="SPECIALISATION"+q).pack()
    buttt=Button(fr,text="CONFIRM",command=lambda:window2.destroy()).pack()
    ans="DETAILS"+'\n'+"USERNAME:"+a+"\n"+"PASSWORD:"+b+"\n"+"NAME:"+c+"\n"+"GENDER:"+d+"\n"+"MAIL ID:"+e11+"\n"+"YOU ARE A :"+h+"\n"+"COLLEGE NAME:"+r+"\n"+"DEPARTMENT:"+s+"\n""QUALIFICATION"+p+"\n"+"SPECIALISATION"+q
    z=open((a+b)+'.txt',"a+")
    f=open("usernames.txt","a+")
    g=open("password.txt","a+")
    f.write(a+'\n')
    g.write(b+'\n')
    z.write(ans)
    f.close()
    g.close()
    z.close()


def newuser():
    global window3
    window3=Tk()
    track=Frame(window3)
    track.pack()
    window3.geometry('700x400')
    user=StringVar(window3)
    passw=StringVar(window3)
    name = StringVar(window3)
    var=StringVar(window3)
    var1=StringVar(window3)
    clg=StringVar(window3)
    mail = StringVar(window3)
    l = LabelFrame(text="NEW USER REGISTRATION")
    ll = Label(track,text="WELCOME NEW COMER TO THE STUDENT USER INTERFACE (SUI)").grid(row=0)
    l1=Label(track,text="USERNAME").grid(row=1)
    e1 = Entry(track,textvariable=user).grid(row=1,column=1)
    l2 = Label(track,text="PASSWORD").grid(row=2)
    e2 = Entry(track,textvariable=passw).grid(row=2,column=1)
    l2 = Label(track,text="NAME").grid(row=3)
    e = Entry(track,textvariable=name).grid(row=3,column=1)
    l3 = Label(track,text="GENDER").grid(row=4)
    rd1 = Radiobutton(track,text="MALE",variable=var,value="MALE").grid(row=4,column=1)
    rd2 = Radiobutton(track,text="FEMALE",variable=var,value="FEMALE").grid(row=4,column=2)
    l2 = Label(track,text="MAIL ID").grid(row=5)
    e1 = Entry(track,textvariable=mail).grid(row=5,column=1)
    l6 = Label(track,text="are you a ").grid(row=6)
    rd3 = Radiobutton(track,text="STUDENT",variable=var1,value="STUDENT").grid(row=6,column=1)
    rd3 = Radiobutton(track,text="TEACHER",variable=var1,value="TEACHER").grid(row=6,column=2)
    but = Button(track,text="CONTINUE",command= lambda :accept(user.get(),passw.get(),name.get(),var.get(),mail.get(),var1.get())).grid(row=7)

def opening():
    global username
    global password
    global frame1,frame2,frame3
    frame1=Frame(window)
    frame2=Frame(window,bg="grey")
    frame3=Frame(window,bg="green")
    frame1.place(x=0,y=0,width=700,height=300)
    frame2.place(x=0,y=300,width=700,height=100)
    frame3.place(x=700,y=0,width=100,height=400)
    username = StringVar(frame1)
    password = StringVar(frame1)
    label1=Label(frame1,text="STUDENT USER INTERFACE (SUI)",font=("Arial Bold",15),bg="black",fg="gold").grid(row=0,column=1)
    label2=Label(frame1,text="USER NAME").grid(row=1)
    entry1 = Entry(frame1,textvariable=username).grid(row=1,column=1)
    label3=Label(frame1,text="PASS WORD").grid(row=2)
    entry2 = Entry(frame1,textvariable=password,show='*').grid(row=2,column=1)
    button1 = Button(frame1,text="SUBMIT",command=login).grid(row=3)
    button2 = Button(frame1,text="NEW USER",command=newuser).grid(row=3,column=1)
    lab = Label(frame2,text="WELCOME USERS NOW YOU ARE VISITING THE APP DEVELOPED BY INAVOLU SAI PRANAY TEJA").pack()

window = Tk()
window.geometry('800x400')
window.title("SUI")
opening()
window.mainloop()
