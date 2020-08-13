import pygame as p
import time as t
import random as r
from tkinter import *
import pyttsx3

global jaldi
global first
global second
global third
global full
global lay
global num
global f1,f2,f3,f4,f5


jaldi=False
first=False
second=False
third=False
full=False

engine = pyttsx3.init()
voiceid = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',voiceid)
engine.setProperty('rate',120)

window=Tk()

#key=StringVar(window)
num1=IntVar(window)
lab = Label(window,text='WELCOME TO THE THAMBOLA GAME',font=("Helvetica",30),fg='RED').pack()
lab = Label(window,text='BY:PRANAY TEJA',font=("Helvetica",20),fg='GOLD').pack()
#rd1 = Radiobutton(window,text="0.5X",variable=key,value='0.5').pack()
#rd2 = Radiobutton(window,text="1X",variable=key,value='1').pack()
#rd2 = Radiobutton(window,text="1.5X",variable=key,value='1.5').pack()
e1 = Entry(window,textvariable=num1).pack()
bu = Button(window,text='generate tickets',font=("Helvetica",20),fg='RED',bg='BLACK',command=lambda:gen(num1.get())).pack()

p.init()
l=1200
w=600
dis=p.display.set_mode((l,w))
p.display.update()
p.display.set_caption("THAMBOLA")
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)

font = p.font.Font('freesansbold.ttf',30)
font1 = p.font.Font('freesansbold.ttf',100)

lis1=[]
for i in range(1,91):
    lis1.append(i)

def speech(text):
    engine.say(text)
    engine.runAndWait()

def gen(num1):
    lay=[]
    window.destroy()
    for i in range(num1):
        l111=[]
        l2=[]
        for k in range(1,91):
            l2.append(k)
        for j in range(15):
            junk=r.choice(l2)
            l111.append(junk)
            l2.remove(junk)
        key1=str(l111[0])+','+str(l111[1])+','+str(l111[2])+','+str(l111[3])+','+str(l111[4])
        key2=str(l111[5])+','+str(l111[6])+','+str(l111[7])+','+str(l111[8])+','+str(l111[9])
        key3=str(l111[10])+','+str(l111[11])+','+str(l111[12])+','+str(l111[13])+','+str(l111[14])
        text4='   TICKET-'+str(i+1)
        lq=[text4,key1,key2,key3]
        lay.append(lq)
    value1(lay,num1)

def value1(lay,count):
        dis.fill(white)
        text34=font1.render('THAMBOLA GAME',True,black,white)
        dis.blit(text34,(200,250))
        pause()
        speech('WELCOME TO THE THAM BOLA GAME')
        speech('You have to note down your ticket numbers on a paper')
        speech('once you are done game begins')
        speech('here are your tickets comes')
        h=0
        dis.fill(white)
        for i in range(3):
            for j in range(4):
                if(count==0):
                    break
                else:
                    text4=font.render(lay[h][0],True,red,white)
                    text1= font.render(lay[h][1],True,red,white)
                    text2= font.render(lay[h][2],True,red,white)
                    text3= font.render(lay[h][3],True,red,white)
                    dis.blit(text4,(300*j,200*i))
                    dis.blit(text1,(300*j,40+(200*i)))
                    dis.blit(text2,(300*j,80+(200*i)))
                    dis.blit(text3,(300*j,120+(200*i)))
                    count-=1
                    h+=1
        p.display.update()
        start()

        

def pause():
    global win
    paused = True

    while paused:
        for event1 in p.event.get():
            if event1.type == p.QUIT:
                p.quit()
                quit()
            if event1.type==p.KEYDOWN :
                if event1.key == p.K_SPACE:
                    paused=False
                elif event1.key==p.K_F5:
                    p.quit()
                    quit()
                if event1.key == p.K_TAB:
                    win = Tk()
                    num = StringVar(win)
                    tin = StringVar(win)
                    name = StringVar(win)
                    lab11 = Label(win,text='ENTER NUMBERS TO VERIFY',font=("Helvetica",30),fg='RED').pack()
                    e = Entry(win,textvariable=num).pack()
                    lab11 = Label(win,text='NAME:',font=("Helvetica",30),fg='RED').pack()
                    e = Entry(win,textvariable=name).pack()
                    if(len(lis)>5):
                        rd1 = Radiobutton(win,text='JALDI 5',variable=tin,value='one').pack()
                        rd1 = Radiobutton(win,text='FIRST LINE',variable=tin,value='first').pack()
                        rd1 = Radiobutton(win,text='SECOND LINE',variable=tin,value='second').pack()
                        rd1 = Radiobutton(win,text='THIRD LINE',variable=tin,value='third').pack()
                    if(len(lis)>15):
                        rd1 = Radiobutton(win,text='FULL HOUSIE',variable=tin,value='full').pack()
                    
                    b  = Button(win,text='CHECK',command=lambda :check(num.get(),tin.get(),name.get())).pack()
                    win.mainloop()
        text2= font.render('PAUSED',True,red,white)
        dis.blit(text2,(550,550))
        p.display.update()

def check(sink,keyfactor,A1):
    global jaldi
    global first
    global second
    global third
    global full
    global ans
    win.destroy()
#    print(sink,keyfactor)
    king=list(map(int,sink.split(',')))
    flag,count=0,0
    ans=A1
#    print(ans)
    for i in range(len(king)):
        if(king[i] in lis):
            flag=1
            count+=1
    if(flag==1 and count==len(king)):
        
        if(keyfactor=='one'):
            jaldi=True
        elif(keyfactor=='first'):
            first=True
        elif(keyfactor=='second'):
            second=True
        elif(keyfactor=='third'):
            third=True
        elif(keyfactor=='full'):
            full=True

def display1(lis,val,f1,f2,f3,f4,f5):
    dis.fill(white)
    for i in range(9):
        for j in range(10):
            key=(i*10)+j+1
            if(key in lis):
                text= font.render(str(key),True,red,white)
            else:
                text= font.render(str(key),True,black,white)
            
            dis.blit(text,(j*50,i*50))

    if(len(lis)>5):
        pr=str(lis[len(lis)-5])+','+str(lis[len(lis)-4]) + ','+ str(lis[len(lis)-3]) +','+str(lis[len(lis)-2])
    else:
        pr=''
        for i in range(len(lis)):
            pr+=str(lis[i])+','
        #pr+=str(len(lis))
    text1= font1.render(pr,True,black,white)
    dis.blit(text1,(500,0))
    text1= font1.render(str(lis[len(lis)-1]),True,red,white) 
    dis.blit(text1,(675,150))
    if(jaldi==False):
        t1='NOT COMPLETED'
    else:
        t1='COMPLETED'+' by '+ans
        if(f1==0):
            speech('congratulations'+ ans +' for your completion of jaldi 5')
            f1=1

    if(first==False):
        t2='NOT COMPLETED'
    else:
        t2='COMPLETED'+' by '+ans
        if(f2==0):
            speech('congratulations'+ ans +' for your completion of first line')
            f2=1
    if(second==False):
        t3='NOT COMPLETED'
    else:
        t3='COMPLETED'+' by '+ans
        if(f3==0):
            speech('congratulations'+ ans +' for your completion of second line')
            f3=1
    if(third==False):
        t4='NOT COMPLETED'
    else:
        t4='COMPLETED'+' by '+ans
        if(f4==0):
            speech('congratulations'+ ans +' for your completion of third line')
            f4=1
    if(full==False):
        text2= font.render('JALDI-5 IS '+t1,True,red,white)
        text3= font.render('FIRST LINE IS '+t2,True,red,white)
        text4= font.render('SECOND LINE IS '+t3,True,red,white) 
        text5= font.render('THIRD LINE IS '+t4,True,red,white) 
        text6= font.render('FULL HOUSIE IS NOT COMPLETED',True,red,white) 
        dis.blit(text2,(530,250))
        dis.blit(text3,(530,290))
        dis.blit(text4,(530,330))
        dis.blit(text5,(530,370))
        dis.blit(text6,(530,410))
        p.display.update()
    else:
        text7= font1.render('FULL HOUSIE..!',True,red,white)
        dis.blit(text7,(530,250))
        text7= font1.render(ans,True,red,white)
        dis.blit(text7,(530,400))
        p.display.update()
        if(f5==0):
            speech('winner is '+ans)
            speech('congratulations'+ ans +' for your full housie')
            f5=1
        pause()
    text41= font.render('CREATED BY PRANAY TEJA',True,black,white)
    dis.blit(text41,(750,550))
    p.display.update()
    speech(str(lis[len(lis)-1]))
    t.sleep(int(val))
    for i in p.event.get():
        if i.type == p.QUIT:
            p.quit()
            quit()
        if i.type==p.KEYDOWN :    
            if i.key == p.K_SPACE:
                pause()
    return [f1,f2,f3,f4,f5]
    
def start():
    pause()
    speech('game begins in 3')
    speech('2')
    speech('1')
    speech('start')
    val='1'
    global lis,f1,f2,f3,f4,f5
    f1,f2,f3,f4,f5=0,0,0,0,0
    lis=[]
    while (len(lis1)!=0):
        key=r.choice(lis1)
        lis1.remove(key)
        lis.append(key)
        f1,f2,f3,f4,f5=display1(lis,val,f1,f2,f3,f4,f5)
window.mainloop()