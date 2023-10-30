from tkinter import*

master = Tk()
w = Canvas(master, width=60, height=8200)
w.pack()
canvas_height = 40
canvas_width = 200
y = int(canvas_height/2)
y = int(canvas_width/2)
w.create_line(0,y,canvas_width,y)
w.mainloop()
