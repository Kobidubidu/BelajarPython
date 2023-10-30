from tkinter import*

main = Tk()
OurMessage = 'Tulis Pesan Disini'
MessageVar = Message(main, text= OurMessage)
MessageVar.config(bg='lightgreen')
MessageVar.pack()
mainloop()
