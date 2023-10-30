from tkinter import*
root = Tk()

frame = Frame()
frame.pack()

buttonFrame =Frame(root)
buttonFrame.pack(side=BOTTOM)
redbutton = Button(frame,text='i love u',fg='red')
redbutton.pack(side=LEFT)
greenbutton = Button(frame,text='3000', fg='green')
greenbutton.pack(side=RIGHT)
btownbutton = Button(frame,text='hanafi', fg='brown')
btownbutton.pack(side=LEFT)

mainloop()
