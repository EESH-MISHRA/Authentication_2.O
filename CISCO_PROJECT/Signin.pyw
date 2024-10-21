'''tkinter program :- login portal '''
from tkinter import *
from tkinter import PhotoImage
from function_signin import *
from tkinter.ttk import Progressbar,Style
import time

# Function to center the window
def center_window(window, width, height):
    """splash window height and width and all screen"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


def root_page_cisco():

    def login_page():
        root.destroy()
        import login_main # type: ignore
    root = Tk()
    # Bitmap icon
    root.iconbitmap(r'icon.ico')
    #title
    root.title('Cisco Sign in ')
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
    Label(login_window,text='Sign up',font='arial 15 ',foreground='black',background='white').place(x=40,y=140)
    Label(login_window,text='With your Cisco account',font='arial 10 ',foreground='black',background='white').place(x=40,y=170)

    #user input values

    user_input = StringVar()
    pass_input = StringVar()
    user_entry = Entry(login_window,textvariable=user_input)
    user_entry.place(x=200,y=300)
    pass_entry = Entry(login_window,textvariable=pass_input)
    pass_entry.place(x=200,y=340)

    #button sign in 
    button_1 = Button(login_window,text='Sign up',font='arial 12',foreground='white',background='#5780d3',relief='flat',command=lambda: check_input(user_input.get(),pass_input.get()))
    button_1.place(x=300,y=400)
    #check button 
    #button_2 forgot password
    button_2 = Button(login_window,text='Already a member..? Log in',font='arial 10 underline',foreground='#5780d3',background='white',relief='flat',command=login_page)
    button_2.place(x=40,y=400)
    root.mainloop()



    



# Create the splash screen window
splash = Tk()
splash.title("Loading...")
splash_width = 427
splash_height = 250
splash.iconbitmap(r'icon.ico')
center_window(splash, splash_width, splash_height)
splash.configure(bg="#aaaaff")
#cisco splash
splash_cisco = Canvas(splash, width=427, height=250,background="#aaaaff")
splash_cisco.pack()

# Add text to the Canvas
#Cisco logo in login_frame
cisco_logo = PhotoImage(file=r'logow.png').subsample(6)  # Adjust the subsample factor as needed
# Use the file parameter
splash_cisco.create_image(213.5,80, image=cisco_logo)

splash_cisco.create_text(213.5,150, text="CISCO", font=("arial bold", 30),fill="white")

# Create a style object
style = Style()
style.theme_use('default')
style.configure("Flat.Horizontal.TProgressbar",
                thickness=20,
                troughcolor='#aaaaff',
                background='white',
                relief='flat')

# Create a Progressbar widget with the custom style
progress = Progressbar(splash_cisco, orient=HORIZONTAL, length=400, mode='determinate', style="Flat.Horizontal.TProgressbar")
progress.place(anchor="center",relx=0.5,rely=0.9)

# Function to update the progress bar
def update_progress():
    """splash window which runs for around 5 sec where i = 0.5"""
    for i in range(101):
        progress['value'] = i
        splash.update_idletasks()
        time.sleep(0.05)
    splash.destroy()
    root_page_cisco()

# Start updating the progress bar
splash.after(100, update_progress)

# Run the splash screen
splash.mainloop()


