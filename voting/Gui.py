from tkinter import *
import  PhoneLib
window=Tk()
window.geometry("600x400");
L1=Label(text='Sms Tool')
L1.place(x=150,y=20)

L2=Label(text='Mobile Number:')
L2.place(x=20,y=50)

E1=Entry(width=20)
E1.place(x=200,y=50)

L3=Label(text='Message:')
L3.place(x=20,y=100)

TXT=Text(height=4,width=30)
TXT.place(x=200,y=100)

L4=Label(text='Message:')
L4.place(x=20,y=250)

L5=Label(text='See Here..')
L5.place(x=200,y=250)


def sms_click():
  phone=PhoneLib.Phone()
  phone.open("COM6")
  ph=E1.get()
  msg=TXT.get('1.0',END)
  phone.Sms(ph,msg)
  phone.close()
  L5.configure(text='Message Sent')

B = Button(window, text ="Send", command=sms_click)
B.place(x=20,y=300)


def dial_click():
  phone=PhoneLib.Phone()
  phone.open("COM6")
  ph=E1.get()
  phone.Dial(ph)

B1 = Button(window, text ="Dial", command=dial_click)
B1.place(x=150,y=300)

window.mainloop()