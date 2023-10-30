from tkinter import*
Layout = Tk()
v = IntVar()

Radiobutton(Layout, text='Male', variable = v, value=1).pack(anchor=W)
Radiobutton(Layout, text='Female', variable = v, value=2).pack(anchor=W)
mainloop()

