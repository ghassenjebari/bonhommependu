from tkinter import *
from tkinter import ttk
import tkinter as ttk
import random

def drawback(root):
    global backg
    canvas = Canvas(root, width = 800, height = 400)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0, anchor=NW, image=backg)





def randomword():
    global mot
    n=random.randrange(1000)+1
    f=open("list.txt")
    for i in range(n):
        mot=f.readline()
    f.close()
    mot = mot[:-1]
    print(mot)

wt=0
ft=0
playerName=''
cl = []
lose=0
l = []
mot =""
randomword()
for i in range(ord('a'), ord('z') + 1):
    cl.append(chr(i))

def drawwinframe(root,wt,ft,playerName,mot):
    global ref
    global wini
    global faili
    global img
    for widget in root.winfo_children():
        widget.destroy()



    winning=Frame(root)

    refr = ttk.Button(root, width=50, height=50)
    refr.config(image=ref, bg='black', relief="flat",command=lambda: drawmaingame(root,icon1,cl,clavier,mot,l))


    canvas = Canvas(winning, width = 800, height = 400)
    canvas.grid(column=0, row=0)
    canvas.create_image(0,0, anchor=NW, image=img)
    winning.place(x=0,y=0)
    refr.place(x=720, y=10)

    if wt>1:
        wintime=str(wt)+' wins !'
    else:
        wintime=str(wt)+' win !'

    if wt>1:
        failtime=str(ft)+' fails !'
    else:
        failtime=str(ft)+' fail !'


    label =Label(root, text=wintime, image=wini, compound='left',bg='black',fg='white')
    label.place(x=10,y=10)

    label2 =Label(root, text=failtime, image=faili, compound='left',bg='black',fg='white')
    label2.place(x=15,y=340)

    gm='Congratulation \n'+playerName+', \n The word was \n'+ mot


    canvas.create_text(500,200,text=gm,font=('neuton', 20, 'italic'),fill='white')


def drawfailframe(root,wt,ft,playerName,mot):
    global ref
    global wini
    global faili
    global img1
    for widget in root.winfo_children():
        widget.destroy()



    winning=Frame(root)
    refr = ttk.Button(root, width=50, height=50)
    refr.config(image=ref, bg='black', relief="flat",command=lambda: drawmaingame(root,icon1,cl,clavier,mot,l))


    canvas = Canvas(winning, width = 800, height = 400)
    canvas.grid(column=0, row=0)
    canvas.create_image(0,0, anchor=NW, image=img1)
    winning.place(x=0,y=0)
    refr.place(x=720, y=10)

    if wt>1:
        wintime=str(wt)+' wins !'
    else:
        wintime=str(wt)+' win !'

    if wt>1:
        failtime=str(ft)+' fails !'
    else:
        failtime=str(ft)+' fail !'


    label =Label(root, text=wintime, image=wini, compound='left',bg='black',fg='white')
    label.place(x=10,y=10)

    label2 =Label(root, text=failtime, image=faili, compound='left',bg='black',fg='white')
    label2.place(x=15,y=340)

    gm='Sorry '+playerName+', \n The word was \n    '+ mot


    canvas.create_text(400,280,text=gm,font=('neuton', 20, 'italic'),fill='white')



def drawIcon():
    indice = ttk.Button(root)
    indice.config(bg='#65ccf5', font=('DerpIcons', 40), relief="flat",text='&',foreground='white',activeforeground='black',activebackground='#65ccf5',command= lambda :switch())
    indice.place(x=5,y=5)


def switch():
    global root,icon1,cl,clavier,mot,l
    reset()
    drawmaingame(root,icon1,cl,clavier,mot,l)





def reset():
    global cl
    global lose
    global l
    global mot
    cl = []
    lose=0
    l = []
    mot = ' '
    lis=[]
    for i in range(ord('a'), ord('z') + 1):
        cl.append(chr(i))
    randomword()
    drawkey(cl, clavier)
    affmsg(l, root)



def countm(ch):
    global l
    lis=[]
    for i in ch:
        if not (i in lis) :
            lis.append(i)
    return len(l)==len(lis)



def drawkey(cl, clavier):




    clavier.destroy()


    clavier = Frame(root)

    x = -1
    t = 0
    a = len(cl)
    while (a % 7 > 0):
        a = a - 1

    for i in range(4):

        for j in range(7):
            x = x + 1
            if x > len(cl) - 1:
                continue
            if x == a and t < ((a + 7 - len(cl)) // 2):

                x = x - 1
                t = t + 1
            else:

                ttk.Button(clavier, text=cl[x].upper(), font='futurist-fixed-width', bg='white', relief="flat",
                           activebackground='#888888', width=1, height=1, command=lambda x=x: readkey(mot, cl[x])).grid(
                    column=j, row=i, ipadx=10, ipady=2, padx=1, pady=1)
    clavier.grid(column=1, row=1)
    clavier.configure(bg='#F0F0F0')



def affmsg(l, hidden):
    global mot
    res = ' '
    for i in mot:
        if i in l:
            res = res + i.upper() + " "
        else:
            res = res + '_ '
    mes = Message(hidden, text=res)
    mes.config(bg='#65ccf5', font=('futurist-fixed-width', 24), anchor="center", width=500, foreground="black")
    mes.grid(row=0, column=1, sticky="snew", ipadx=10, ipady=10, padx=100, pady=50)



def readkey(mot, c):
    global l
    global cl
    global lose
    global wt
    global ft
    w=len(l)
    for widget in root.winfo_children():
        widget.destroy()
    for i in mot:
        if i == c:
            if not (i in l) :
                l.append(c)
    cl.remove(c)
    if w==len(l):
        lose=lose+1
    drawmaingame(root,icon1,cl,clavier,mot,l)
    if lose>5 :
        reset()
        ft=ft+1
        drawfailframe(root,wt,ft,playerName,mot)
    if countm(mot):
        reset()
        wt=wt+1
        drawwinframe(root,wt,ft,playerName,mot)




def drawmaingame(root,icon1,cl,clavier,mot,l):
    for widget in root.winfo_children():
        widget.destroy()
    drawback(root)
    drawkey(cl, clavier)
    pendu(root)
    affmsg(l, root)
    if lose==0:
        drawIcon()



def check(ch):
        return len(ch)>0

def getname():
    global icon1,cl,clavier,mot,l,playerName,enrtry1
    playerName=entry1.get()
    if check(playerName):
        drawmaingame(root,icon1,cl,clavier,mot,l)


def namemenu(root):
    global entry1
    global icon1,cl,clavier,mot,l,playerName
    canvas = Canvas(root, width = 800, height = 400,bg='white')
    canvas.grid(column=0, row=0)
    canvas.create_image(350,50, anchor=NW, image=img3)
    root.geometry("800x400")
    button=Button(root)
    button.config(bg='#f5a31a', font=('futurist-fixed-width', 20), foreground="white",text="done",relief="flat",width=5, height=0,command= lambda :getname())
    button.place(x=120,y=150)
    canvas.create_text(130,50,text='enter your name :',font=('futurist-fixed-width', 20),fill="#6c63ff")
    entry1 =Entry (root)
    entry1.config(bd=1,insertwidth=0, font=('futurist-fixed-width', 20),relief="ridge",bg="#fdfdfd")
    canvas.create_window(170, 100, window=entry1)


def pendu(root):
    global lp,lose
    canvas = Canvas(root, width = 173, height = 197)
    canvas.place(x=500,y=100)
    if lose>=0 and lose < 6 :
        canvas.create_image(0,0, anchor=NW, image=lp[lose])








root = Tk()






ref = PhotoImage(file="ref.png")
wini= PhotoImage(file="true.png")
faili= PhotoImage(file="false.png")
img = PhotoImage(file="back.gif")
icon1 = PhotoImage(file="light-bulb.png")
img1= PhotoImage(file="fail.png")
img3=PhotoImage(file="welcome.png")
p1=PhotoImage(file="p1.gif")
p2=PhotoImage(file="p2.gif")
p3=PhotoImage(file="p3.gif")
p4=PhotoImage(file="p4.gif")
p5=PhotoImage(file="p5.gif")
p6=PhotoImage(file="p6.gif")
lp=[p1,p2,p3,p4,p5,p6]
backg=PhotoImage(file="background.png")
root.title('pendu')
root.configure(bg='#FFE8DF')
root.geometry("800x400")
clavier = Frame(root)
namemenu(root)


mainloop()
