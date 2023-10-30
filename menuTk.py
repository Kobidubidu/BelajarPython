from tkinter import*
from tkinter import filedialog
import webbrowser

def open_browser():
    webbrowser.open('www.youtube.com/watch?v=dQw4w9WgXcQ')

root =Tk()
root.title('Menu')
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)

import os

menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='new', command=open_browser)
def open_file_manager():
    file_path = filedialog.askdirectory()
    if folder_path:
        os.startfile(file_path)
filemenu.add_command(label='Open...',command=open_file_manager)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(menu)

def about_canvas():
    aboutcanvas = Tk()
    helpcanvas = Menu(aboutcanvas)
    aboutcanvas.config(menu=menu)
    helpcanvas.add_command
    return



menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='about',command=about_canvas)

viewmenu = Menu(menu)
toolmenu = Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_cascade(label='Tool Windows',menu=toolmenu)
toolmenu.add_command(label='commit')
viewmenu.add_command(label='Appearance')
viewmenu.add_separator()
viewmenu.add_command(label='Quick Definiton')
viewmenu.add_command(label='Quick Type Definition')
viewmenu.add_command(label='Parameter Info')
viewmenu.add_command(label='Type Info')
viewmenu.add_command(label='Context Info')
viewmenu.add_separator()
mainloop()
