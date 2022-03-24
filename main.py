from os import popen
import tkinter as tk
from tkinter import ttk
from pyperclip import copy
from webbrowser import open

root = tk.Tk()
root.title('MBSN Copier')
root.geometry('300x150')
root.resizable(0, 0)
root.iconbitmap('icon.ico')

cmd = 'wmic bios get serialnumber'
cmd_sn = popen(cmd).read().replace('\n','').replace('SerialNumber','').replace(' ','')

sn_label = tk.Label(text= cmd_sn, font= ('round pop', 11)).pack(pady=25)
copy_btn = ttk.Button(text= 'Copy', command= lambda : copy(cmd_sn)).pack()
github_btn = ttk.Button(text= 'GitHub', command= lambda : open('https://github.com/erfannjz')).pack()

root.mainloop()