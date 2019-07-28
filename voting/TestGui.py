from tkinter import *

window=Tk()
window.geometry("600x400")
def hello_CallBack():
  print( "Hello World")

B = Button(window, text ="Send", command = hello_CallBack)

B.place(x=10,y=10)

window.mainloop()