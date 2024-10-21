import json
import tkinter.messagebox


def check_record(Email,password):
    '''check Email and password if exist pass on to next window or raise error msg password is incorrect  '''
    try:
        file  = open('record.json',"r")
        record = file.read()
        final  = json.loads(record)
        if Email in final:
            if not password.strip():
                tkinter.messagebox.showerror('password',"password not be blank or empty")
            else:
                if final[f'{Email}'] == password :
                    tkinter.messagebox.showinfo("Thanks","Thanks for using Demo authentication page")
                else:
                    tkinter.messagebox.showerror('User',"Wrong password")
        elif not Email.strip():
            tkinter.messagebox.showerror('Email',"Email could not be empty")
        else:
            tkinter.messagebox.showerror('Email','Email does not exist')
        file.close()
    except Exception as e:
        print(e)
        tkinter.messagebox.showerror('file error','File data lost or file corrupt\nIf u are new pls sign in')

