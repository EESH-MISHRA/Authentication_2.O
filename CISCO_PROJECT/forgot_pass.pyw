'''tkinter program :- login portal '''
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import json
#redirect window
def login_window():
    root.destroy()
    import login_main #type: ignore
    if __name__=='__main__':
        login_window
#display forgot password
'''display forgot password'''
def get_password():
    try:
        Email = user_input.get()
        file = open('record.json','r')
        record = file.read()
        final = json.loads(record)
        if Email in final:
            pass_output.set(final[Email])
        elif not Email.strip():
            messagebox.showerror("Email","Email cannot be empty")
        else:
            messagebox.showerror('Email','does not exist')
    except:
        messagebox.showerror('file error',"File not exist")


root = Tk()
# Bitmap icon
root.iconbitmap(r'icon.ico')
#title
root.title('FORGOT PASSWORD ')
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
forgot_window = Frame(root,background='white',highlightbackground='black',highlightthickness=1)
forgot_window.place(relx=0.5,rely=0.5,anchor='center',height=650,width=540)  # Centered placement
#Email label
Email_label = Label(forgot_window,text='Email',font='arial 10 bold',foreground='black',background='white')
Email_label.place(x=50,y=300)
#password label
pasword_label = Label(forgot_window,text='Password',font='arial 10 bold',foreground='black',background='white')
pasword_label.place(x=50,y=340)


#Cisco logo in login_frame
new_logo = PhotoImage(file=r'logo.png').subsample(10)  # Adjust the subsample factor as needed
# Use the file parameter
logo_login = Label(forgot_window, image=new_logo,background='white')
logo_login.place(x=20, y=60)
logo_name = Label(forgot_window,text="CISCO",font="arial 15 bold",foreground="#14A6FF",background="white")
logo_name.place(x=65,y=105)

#additional text
Label(forgot_window,text='FORGOT PASSWORD',font='arial 15 bold',foreground='black',background='white').place(x=40,y=140)
Label(forgot_window,text='of your Cisco account',font='arial 10 ',foreground='black',background='white').place(x=40,y=170)
#user input values

user_input = StringVar()
pass_output = StringVar()
user_entry = Entry(forgot_window,textvariable=user_input)
user_entry.place(x=200,y=300)
#refresh
def refresh(event):
    pass_output.set('')  # Assuming `pass_output` is a StringVar or similar

# Bind the refresh function to the button click event
user_entry.bind('<Button-1>', refresh)
#button know password
button_1 = Button(forgot_window,text='know your password',font='arial 10',foreground='white',background='#5780d3',relief='flat',command =get_password)
button_1.place(x=300,y=400)
Label(forgot_window,textvariable=pass_output,font='arial 10',foreground='black',background='white').place(x=200,y=340)
#sign redirect page 
Button(forgot_window,text="Log in",foreground="#5780d3",font="arial 10 underline",relief='flat',background='white',command=login_window).place(x=50,y=405)
root.mainloop()