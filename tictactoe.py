import tkinter.messagebox as mb
def mode():
    return mb.askyesno("TIC-TAC-TOE","GAME COMPLETED do you want to continue")
def win(lis,sym,sym1):
    ans='0'
    if((lis[0]==sym and lis[1]==sym and lis[2]==sym) or (lis[0]==sym and lis[3]==sym and lis[6]==sym) or (lis[0]==sym and lis[4]==sym and lis[8]==sym) or (lis[3]==sym and lis[4]==sym and lis[5]==sym) or (lis[6]==sym and lis[7]==sym and lis[8]==sym) or (lis[1]==sym and lis[4]==sym and lis[7]==sym) or (lis[2]==sym and lis[5]==sym and lis[8]==sym) or (lis[2]==sym and lis[4]==sym and lis[6]==sym)):
        ans='win'
    elif((lis[0]==sym1 and lis[1]==sym1 and lis[2]==sym1) or (lis[0]==sym1 and lis[3]==sym1 and lis[6]==sym1) or (lis[0]==sym1 and lis[4]==sym1 and lis[8]==sym1) or (lis[3]==sym1 and lis[4]==sym1 and lis[5]==sym1) or (lis[6]==sym1 and lis[7]==sym1 and lis[8]==sym1) or (lis[1]==sym1 and lis[4]==sym1 and lis[7]==sym1) or (lis[2]==sym1 and lis[5]==sym1 and lis[8]==sym1) or (lis[2]==sym1 and lis[4]==sym1 and lis[6]==sym1)):
        ans='lost'
    if(ans!='0'):
        print("YOU HAVE "+ans+" THE MATCH")
        return 0
def move(lis,sym,sym1):
    k=9
    if(lis[0]==sym):
        if(lis[1]==sym and lis[2]==' '):
            k=2
        elif(lis[3]==sym and lis[6]==' '):
            k=6
        elif(lis[4]==sym and lis[9]==' '):
            k=9
        elif(lis[2]==sym and lis[1]==' '):
            k=1
        elif(lis[6]==sym and lis[3]==' '):
            k=3
        elif(lis[8]==sym and lis[4]==' '):
            k=4
        if(k!=9):
            return k
    if(lis[1]==sym):
        if(lis[2]==sym and lis[0]==' '):
            k=0
        elif(lis[4]==sym and lis[7]==' '):
            k=7
        elif(lis[7]==sym and lis[4]==' '):
            k=4
        if(k!=9):
            return k
    if(lis[2]==sym):
        if(lis[4]==sym and lis[6]==' '):
            k=6
        elif(lis[5]==sym and lis[8]==' '):
            k=8
        elif(lis[8]==sym and lis[5]==' '):
            k=5
        elif(lis[6]==sym and lis[4]==' '):
            k=4
        if(k!=9):
            return k
    if(lis[3]==sym):
        if(lis[4]==sym and lis[5]==' '):
            k=5
        elif(lis[5]==sym and lis[4]==' '):
            k=4
        elif(lis[6]==sym and lis[0]==' '):
            k=0
        if(k!=9):
            return k
    if(lis[4]==sym):
        if(lis[5]==sym and lis[3]==' '):
            k=3
        elif(lis[7]==sym and lis[1]==' '):
            k=1
        elif(lis[6]==sym and lis[2]==' '):
            k=2
        elif(lis[8]==sym and lis[0]==' '):
            k=0
        if(k!=9):
            return k
    if(lis[5]==sym):
        if(lis[8]==sym and lis[2]==' '):
            k=2
        elif(lis[3]==sym and lis[4]==' '):
            k=4
        if(k!=9):
            return k
    if(lis[6]==sym):
        if(lis[7]==sym and lis[8]==' '):
            k=8
        elif(lis[8]==sym and lis[7]==' '):
            k=7
        if(k!=9):
            return k
    if(lis[7]==sym):
        if(lis[8]==sym and lis[6]==' '):
            k=6
        if(k!=9):
            return k
    if(lis[4]==' '):
        k=4
        if(k!=9):
            return k
    else:
        for i in range(9):
            if(lis[i]==' '):
                k=i
                break
        return k
def drawboard(lis):
    print("    |       |    ")
    print(lis[0],"  |   ",lis[1]," |   ",lis[2])
    print("    |       |    ")
    print("-----------------")
    print("    |       |    ")
    print(lis[3],"  |   ",lis[4]," |   ",lis[5])
    print("    |       |    ")
    print("-----------------")
    print("    |       |    ")
    print(lis[6],"  |   ",lis[7]," |   ",lis[8])
    print("    |       |    ")
    print("//////////////////////////")
h=True
while h:
    print("TIC-TAC-TOE")
    print("board looks like this")
    lis=[1,2,3,4,5,6,7,8,9]
    drawboard(lis)
    lis=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    sym=input("press the symbol u want O||X::")
    if(sym=='X'):
        sym1='O'
    else:
        sym1='X'
    print("your symbol is",sym,"and you have to enter position number to place your symbol")
    count=9
    clue=input("do u want to play first type yes:")
    drawboard(lis)
    n=[]
    if(clue=="yes"):
        while(count!=0):
            p=(int(input("your position:")))-1
            count-=1
            lis[p]=sym
            drawboard(lis)
            l=win(lis,sym,sym1)
            if(l==0 or count==0):
                break
            s=move(lis,sym,sym1)
            print(">>>>>>>>>>>",s)
            count-=1
            lis[s]=sym1
            drawboard(lis)
            l=win(lis,sym,sym1)
            if(l==0 or count==0):
                break
    else:
        while(count!=0):
            s=move(lis,sym,sym1)
            print(">>>>>>>>>>>",s)
            count-=1
            lis[s]=sym1
            drawboard(lis)
            l=win(lis,sym,sym1)
            if(l==0 or count==0):
                count=0
                break
            else:
                p=(int(input("your position:")))-1
                count-=1
                lis[p]=sym
                drawboard(lis)
                l=win(lis,sym,sym1)
                if(l==0 or count==0):
                    count=0
                    break
    h=mode()
    print("GAME COMPLETED")
