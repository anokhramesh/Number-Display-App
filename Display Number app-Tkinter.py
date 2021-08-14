from tkinter import *
window =Tk()
window.title("Number Display App")
window.geometry('500x300')
label1= Label(window,text='Enter Your Name',fg='blue',font=('Arial',14))
label1.grid(row=0,column=0,padx=5,pady=10)
data = IntVar()
textbox1= Entry(window,textvariable=data,fg='blue',font=('Arial',14))
textbox1.grid(row=0,column=1)
def myfunction():
    emptylabel.config(text='The Number is:'+str(data.get()))

button1 = Button(window,command=myfunction,text='SAVE',fg='blue',font=('Arial',14))
button1.grid(row=1,column=1,sticky=W)
emptylabel=Label(window,fg='green',font=('Arial',14))
emptylabel.grid(row=2,column=1,sticky=W,pady=20)

window.mainloop()