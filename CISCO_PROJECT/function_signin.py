'''Sign in portal'''
import json
import tkinter.messagebox

def user_register(Email,password):
    try:
        file  = open('record.json',"r")
        record = file.read()
        final_record  = json.loads(record)
        if Email in final_record:
            tkinter.messagebox.showerror('Already Exist','Email already exist')
            file.close()
        else:
            final_record[f'{Email}'] = f'{password}'
            file = open('record.json','w')
            file.write(json.dumps(final_record))
            file.close()
            tkinter.messagebox.showinfo("Registered","Your account has been created")

    except:
        '''if file does not exist it will create file and store data'''
        file  = open('record.json','w')
        record = {}
        record[f'{Email}'] = f'{password}'
        file.write(json.dumps(record))
        file.close()
        tkinter.messagebox.showinfo("Registered","Your account has been created")


def check_Email_symbol(user_id:str,pass_id:str):
    """check symbol exist in Email and password"""
    symbol =["!","@","#","$","%","&"]
    for i in symbol :
        if i in user_id:
            if i in pass_id:
                user_register(user_id,pass_id)
                break
    else:
        tkinter.messagebox.showerror("Error","Email & Password should consist symbol")

def check_input(Email, password):
        if not Email.strip() or not password.strip():
            tkinter.messagebox.showerror("Blank","Not be blank or empty")
        elif  len(password) < 6 :
            tkinter.messagebox.showerror('Invalid Input', "Password is too short")
        elif  len(password) > 18:
            tkinter.messagebox.showerror('Invalid Input', "Password is too long")
        else:
            check_Email_symbol(Email,password)