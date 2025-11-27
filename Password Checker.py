import tkinter # for GUI
import re # for checking text
from time import sleep
# Screen 
# Attr
screen = tkinter.Tk()
screen.title("Passwrod Checker")
screen.configure(background="white")
screen.geometry("400x400")

isOpen = True
def close():
    global isOpen
    isOpen =False
    screen.destroy()
screen.protocol("WM_DELETE_WINDOW",close)
# Label Namec
program_name_label = tkinter.Label(
    screen,text="Password Checker",
    font=("Arial",16)
    ,background="white",pady=50
    )
program_name_label.pack()
# Password Entry Input
counter = 0
password_input = tkinter.Entry(screen,font=("Arial",12),background="white",border=0,relief="solid",highlightbackground="#f42a6c",highlightthickness=2,highlightcolor="#f42a6c",insertwidth=1,width=28,justify="center")
password_input.pack(ipady=2,pady=(0,20),)
def change_color(counter):
    if (counter == 5): password_input.configure(highlightbackground="#3af46c",highlightcolor="#3af46c")
    elif (counter >= 3): password_input.configure(highlightbackground="#f4b93a",highlightcolor="#f4b93a")
    else: password_input.configure(highlightbackground="#f42a6c",highlightcolor="#f42a6c")
# Guide Lables
values = [
    tkinter.Label(screen,text="• Password must be at least 8 characters."),
    tkinter.Label(screen,text="• Password contains lower characters."),
    tkinter.Label(screen,text="• Password contains capital characters."),
    tkinter.Label(screen,text="• Password contains number."),
    tkinter.Label(screen,text="• Password contains special character\n"+r"!@#$%^&*()_+-={}\[\]:;\"'<>,.?/\\.")
]

for _ in values:
    _.configure(anchor="w",background="white")
    _.pack(padx=78,fill="x")

def checker(text: str):
    global counter
    f0 , f1,f2,f3,f4 = True,True,True,True,True
    if (len(text) >= 8):
        values[0].configure(fg="#3af46c")
    else:
        values[0].configure(fg="#f42a6c")
        f0 = False
    if (re.search(r"[a-z]",text) == None):
        values[1].configure(fg="#f42a6c")
        f1 = False
    else:
        values[1].configure(fg="#3af46c")
    if (re.search(r"[A-Z]",text) == None):
        values[2].configure(fg="#f42a6c")
        f2 = False
    else:
        values[2].configure(fg="#3af46c")
    if (re.search(r"\d",text) == None):
        values[3].configure(fg="#f42a6c")
        f3 = False
    else:
        values[3].configure(fg="#3af46c")
    if (re.search(r"[!@#\$%\^&\*\(\)_\+\-=\{\}\[\]:;\"'<>,\./\\]",text) == None):
        values[4].configure(fg="#f42a6c")
        f4 = False
    else:
        values[4].configure(fg="#3af46c")
    counter = f0+f1+f2+f3+f4

while isOpen:
    checker(password_input.get())
    change_color(counter)
    sleep(0.01)
    screen.update()
    
