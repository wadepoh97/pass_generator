import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


import random
import pyperclip
import os

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Password Generator', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))

passLabel = tk.Label(root, text='Password Lenght: ', bg = 'lightsteelblue2')
passLabel.config(font=('helvetica', 14))
passLength = tk.Entry(root) 

canvas1.create_window(150, 60, window=label1)
canvas1.create_window(150, 100, window=passLabel)
canvas1.create_window(150, 130, window=passLength)

def getPass ():
    length = passLength.get()

    symbol = 0
    lower = 0
    upper = 0
    number = 0
    count = 0
    password = []
    length = 128 if length == '' else int(length)
    while count < length:
        rand = random.randint (0,3)
        if rand == 0:
            lower += 1
            b = int(random.randint (97,123))
            password.append(b)
        elif rand == 1:
            upper += 1
            b = random.randint (65,91)
            password.append(b)
        elif rand == 2:
            number += 1
            b = random.randint (48,58)
            password.append(b)
        elif rand == 3:
            r = random.randint(0,2)
            symbol += 1
            if r == 0:
                b = random.randint (33,48)
                password.append(b)
            elif r == 1:
                b = random.randint (91,97)
                password.append(b)
            elif r == 2:
                b = random.randint (123,126)
                password.append(b)
        count += 1
    #convert ascii code to characters
    word = "".join([chr(c) for c in password])
    #copy pass to clipboard
    pyperclip.copy(word)
    tk.messagebox.showinfo('Password Here !', 'Your password already copied to clipboard. Length is:'+ str(length) + '\n' + word)

generateButton = tk.Button(text="      Generate Password     ", command=getPass, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=generateButton)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()