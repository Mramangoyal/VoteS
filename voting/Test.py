from tkinter import *


# on change dropdown value

top = Tk()
top.geometry("350x500")


L1 = Label(text = "User Name:")
L1.place(x=10,y=10)
E1 = Entry(width=30)
E1.place(x=100,y=10)

L2 = Label(text = "Address:")
L2.place(x=10,y=50)
T1 = Text(width=20,height=3)
T1.place(x=100,y=50)

L3 = Label(text = "Gender:")
L3.place(x=10,y=130)
gender=IntVar()

Male = Radiobutton( top,value='1',text='Male' ,variable=gender)

Male.place(x=100,y=130)
Female = Radiobutton(top,value='0',text='Female',variable=gender)
Female.place(x=150,y=130)

choices = {'Pizza', 'Lasagne', 'Fries', 'Fish', 'Potatoe'}
tkvar=StringVar(top)
tkvar.set('Pizza')

popupMenu = OptionMenu(top,tkvar , *choices)
L2 = Label(text = "Food:")
L2.place(x=10,y=170)

popupMenu.place(x=100,y=170)
#Event
def change_dropdown(*args):
   print(tkvar.get())
# link function to change dropdown
tkvar.trace('w', change_dropdown)

L3= Label(text = "Interest:")
L3.place(x=10,y=250)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0)
C1.place(x=150,y=250)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0)
C2.place(x=250,y=250)



def btn_click(*args):
  g=['Female','Male']
  q="insert into employee values('{}','{}','{}','{}')".format(E1.get(),T1.get('1.0',END),g[gender.get()],tkvar.get())
  print(q)

P=PhotoImage(file='icon1.gif')

B = Button(top,image=P,text ="Set", command = btn_click)

B.place(x=10,y=340)

top.mainloop()