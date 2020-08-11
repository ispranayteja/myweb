import pyttsx3
import time
import speech_recognition as sr

mike = sr.Microphone()
r  = sr.Recognizer()
engine = pyttsx3.init()
voiceid = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',voiceid)
engine.setProperty('rate',140)

def listening():
    with mike as source:
        speech("sir")
        audio=r.listen(source)
        speech('done sir')
        try:
            text=r.recognize_google(audio)
            print(text)
            speech(text)
        except:
            speech("i could not hear you sir try again")
    return text
def closing():
    key1=time.localtime()
    h1=key1.tm_hour
    if(h1<=20):
        speech("have a good day sir see you soon!")
    else:
        speech("good night sir see you soon")
def plancreate():
    g=open("newaction.txt","w")
    speech("sir what are your plans")
    cons=listening()
    if(cons=='no plans'):
        speech("ok sir no plans today")
    else:
        speech('can i add them ')
        speech(cons)
        if(listening()=='yes beast'):
            lis=list(cons.split(" "))
            for i in range(len(lis)):
                g.write(lis[i]+"\n")
            g.close
def planofaction():
    f=open("newaction.txt","r")
    feel=f.readlines()
    if(feel!=[]):
        speech("sir you are planned to have these activities today sir")
        for i in range(len(feel)):
            speech(str(i+1))
            speech(feel[i])
        f.close
def greet():
    key=time.localtime()
    h=key.tm_hour
    if(h>=9 and h<12):
        ans="good morning"
    elif(h>=12 and h<16):
        ans="good afternoon"
    else:
        ans="good evening"
    speech(ans)
def speech(text):
    engine.say(text)
    engine.runAndWait()
def playsome():
#this plays some music and stops whenever i say beast
    print("eww")

def commands():
# every operations in beast
    f=open('command.txt','r+')
    flines=f.readlines()
    for i in range(len(flines)):
        speech(str(i+1))
        speech(flines[i])
        f.close()

def dedicate():
#designing the beast
    f=open('adding.txt','a+')
    flines=f.readlines()
    for i in range(len(flines)):
        print(flines[i])
        speech(flines[i])
    speech('which one do you want')
    t=listening()
    ans=t+'.txt'
    g=open(ans,'r+')
    glines=g.readlines()
    speech(glines)
    g.close()
    f.close()

def addnewthing(text):
# has to add new commands into a file
    f=open('adding.txt','a+')
    f.write(text+'\n')
    f.close()
    
speech("i am beast 3 point o with speech and interaction capability")
hell=listening()
def starting():
    speech("hello pranay sir welcome")
    greet()
    plancreate()
    planofaction()
    speech('what can i do')
    while(listening()=='beast'):
        text=listening()
        if(text=='replay the plan of action'):
            planofaction()
        elif(text=='play some music'):
            playsome()
        elif(text=='enter into design mode'):
            speech('entering design mode sir')
            dedicate()
        elif(text=='show me your operations'):
            commands()
        else:
            speech('sir you do not have this command do you want to add this thing ')
            txt=listening()
            if(txt=='yes beast'):
                speech('ok sir i am adding')
                addnewthing(text)
        if(text=='bye beast'):
            break

    closing()
if(hell=="Iron Man 441"):
    starting()
else:
    greet()
    speech("may i know who is here")
    if(listening()=='Iron Man 441'):
        starting()
