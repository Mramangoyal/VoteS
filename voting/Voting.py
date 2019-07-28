from tkinter import *
import PhoneLib
import time
import threading
ph=PhoneLib.Phone()
ph.open('COM7')
ph.SetParameter()

def votecount(L2,L3,L4):
 V1 = 0
 V2 = 0
 V3 = 0
 while True:
   print('x')
   data=ph.ReadLine()
   if(data.startswith("+CMT")):
    i=data.index(' ');
    L=data[i+1:].split('\"')

    print(L)
    msg=ph.ReadLine()
    print(len(msg))
    if(msg[0]=='A'):
        V1=V1+1
        L2.config(text=V1)
    elif(msg[0] == 'B'):
        V2 = V2 + 1
        L3.config(text=V2)
    elif (msg[0] == 'C'):
        V3 = V3 + 1
        L4.config(text=V3)
    msg=''


window=Tk()

window.geometry("1100x300");
L1=Label(text='Live Voting')
L1.place(x=600,y=20)



P1=PhotoImage(file='rr.gif')
B1 = Button(window, image=P1,text ="RR")
B1.place(x=50,y=50)
L2=Label(text='A')
L2.place(x=200,y=250)


P2=PhotoImage(file='rk.gif')
B2 = Button(window, text ="RK",image=P2)
B2.place(x=400,y=50)
L3=Label(text='B')
L3.place(x=550,y=250)

P3=PhotoImage(file='sk.gif')
B3 = Button(window, text ="SK" ,image=P3)
B3.place(x=750,y=50)
L4=Label(text='C')
L4.place(x=900,y=250)
thread = threading.Thread(target = votecount, args = (L2,L3,L4))
thread.start()
window.mainloop()
