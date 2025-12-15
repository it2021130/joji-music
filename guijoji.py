from tkinter import *
from logging import root

#widgets = gui elements :buttons,textboxes,labels
#windows = serves as a container to hold or contain widgets

#instaintiate a window
jwindow = Tk()
jwindow.geometry('500x700')
jwindow.title('ε> joji-a confession of love for frimpa <3 ')


#adding icon to my project
jicon =PhotoImage(file='Gimme_Love.png')
jwindow.iconphoto(True ,jicon)

#change backgroud color
jwindow.configure(background='#C20202')

##################################################widgets

jolabel= Label(jwindow,image = jicon,compound='top')
jolabel.pack()

jlabel = Label(jwindow,text='joji text',font=('Arial',20,'bold'),bg='#C20202',fg='black',relief=RAISED,bd=5)
jlabel.place(relx=0.5,rely=0.5,anchor=CENTER)














jwindow.mainloop()  #place a window on a computer screen .listen for events

