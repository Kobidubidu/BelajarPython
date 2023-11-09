from tkinter import *

root = Tk()
root.title("Hangout")
root.geometry("400x320")  # set starting size of window
root.maxsize(400, 320)  # width x height
root.config(bg="white")  # set background color of root window


# login image
Image = PhotoImage(file='hangoutt.png')
img_resize = Image.subsample(5,5)
Label(root, image=img_resize,bg='white').pack(pady=5)

def checkInput():
    '''check that the username and password match'''
    usernm = "y"
    pswrd = "p"
    entered_usernm = username_entry.get()  # get username from Entry widget
    entered_pswrd = password_entry.get()  # get password from Entry widget

    if (usernm == entered_usernm) and (pswrd == entered_pswrd):
        root = Tk()
        root.title("Login UI using Pack")
        root.geometry("400x320")  # set starting size of window
        root.maxsize(400, 320)  # width x height
        root.config(bg="#6FAFE7")
        Label(root, text="Have Fun", bg="#6FAFE7").pack(side='left', padx=7)

    else:
        print("Login failed: Invalid username or password.")

def toggled():
    '''display a message to the terminal every time the check button
    is clicked'''
    print("The check button works.")

# Username Entry
username_frame = Frame(root, bg="white")
username_frame.pack()

Label(username_frame, text="Username", bg="white").pack(side='left', padx=5)

username_entry = Entry(username_frame, bd=3)
username_entry.pack(side='right')

# Password entry
password_frame = Frame(root, bg="white")
password_frame.pack()

Label(password_frame, text="Password", bg="white").pack(side='left', padx=7)

password_entry = Entry(password_frame, bd=3)
password_entry.pack(side='right')

# Create Go! Button

go_button = Button(root, text="GO!", command=checkInput, bg="#00BFFF", width=15)

go_button.pack(pady=5)

# Remember me and forgot password
bottom_frame = Frame(root, bg="white")
bottom_frame.pack()

var = IntVar()

remember_me = Checkbutton(bottom_frame, text="Remember me", bg="white", command=toggled, variable=var)
remember_me.pack(side='left', padx=19)

# The forgot password Label is just a placeholder, has no function currently
forgot_pswrd = Label(bottom_frame, text="Forgot password?", bg="white")
forgot_pswrd.pack(side="right", padx=19)

root.mainloop()
