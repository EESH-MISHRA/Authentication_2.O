from tkinter import *
from tkinter import PhotoImage
from function_login import *

def signin_page():
    root.destroy()
    import Signin # type: ignore
def forgot_page():
    root.destroy()
    import forgot_pass #type: ignore
'''tkinter program :- login portal '''
root = Tk()
# Bitmap icon
root.iconbitmap(r'icon.ico')
#title
root.title('Cisco Log in ')
#window size
canvas_height = 1080
canvas_width = 720
root.geometry(f'{canvas_height}x{canvas_width}')
root.minsize(canvas_height,canvas_width)
root.maxsize(canvas_height,canvas_width)
#base window
base_window = Canvas(root,height=1080,width=720)
base_window.pack(fill=BOTH)

#base window :- Trinalges 1/2
base_window.create_polygon((0,0,0,720,1080,720),fill='#57409f') 
base_window.create_polygon((0,0,1080,0,1080,720),fill='#aaaaff')

#Create a new frame above the login_window
login_window = Frame(root,background='white',highlightbackground='black',highlightthickness=1)
login_window.place(relx=0.5,rely=0.5,anchor='center',height=650,width=540)  # Centered placement

#Email label
Email_label = Label(login_window,text='Email',font='arial 10 bold',foreground='black',background='white')
Email_label.place(x=50,y=300)

#password label
pasword_label = Label(login_window,text='Password',font='arial 10 bold',foreground='black',background='white')
pasword_label.place(x=50,y=340)

#Cisco logo in login_frame
new_logo = PhotoImage(file=r'logo.png').subsample(10)  # Adjust the subsample factor as needed

# Use the file parameter
logo_login = Label(login_window, image=new_logo,background='white')
logo_login.place(x=20, y=60)
logo_name = Label(login_window,text="CISCO",font="arial 15 bold",foreground="#14A6FF",background="white")
logo_name.place(x=65,y=105)

#additional text
Label(login_window,text='Log in',font='arial 15 ',foreground='black',background='white').place(x=40,y=140)
Label(login_window,text='With your Cisco account',font='arial 10 ',foreground='black',background='white').place(x=40,y=170)

#user input values
user_input = StringVar()
pass_input = StringVar()
user_entry = Entry(login_window,textvariable=user_input)
user_entry.place(x=200,y=300)
pass_entry = Entry(login_window,textvariable=pass_input)
pass_entry.place(x=200,y=340)

#button sign in 
button_1 = Button(login_window,text='Log in',font='arial 12',foreground='white',background='#5780d3',relief='flat',command=lambda: check_record(user_input.get(),pass_input.get()))
button_1.place(x=300,y=400)
#check button 
#button_2 forgot password
button_2 = Button(login_window,text='Don\'t have an account..? Sign in ',font='arial 10 underline',foreground='#5780d3',background='white',relief='flat',command=signin_page)
button_2.place(x=50,y=410)
button_3 = Button(login_window,text="forgot password",font='arial 10 underline',foreground='#5780d3',background='white',relief='flat',command=forgot_page)
button_3.place(x=50,y=390)
#forgot pass button display 
def forgot_pass_display():
    forgot_diplay_input = StringVar()
root.mainloop()