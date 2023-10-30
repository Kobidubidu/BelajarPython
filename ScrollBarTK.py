from tkinter import*

layout = Tk()
scrollbar = Scrollbar(layout)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(layout,yscrollcommand=scrollbar.set)
for line in range(300):
    mylist.insert(END, 'list data ke'+str(line))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()
