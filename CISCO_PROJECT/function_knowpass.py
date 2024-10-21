import json
from tkinter import messagebox
'''display forgot password'''
def password(Email: str):
    file = open('record.json','r')
    record = file.read()
    final = json.loads(record)
    if Email in final:
        return final[f'{Email}']
    else:
        messagebox.showerror('Email','does not exist')
print(password('eesh'))