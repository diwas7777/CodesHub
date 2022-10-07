#make sure that your device has Python3 and tkinter installed
from tkinter import *
import random 
import string 

root = Tk()

def generate():
    char = list(string.ascii_letters + string.digits + string.punctuation)


    for i in range (25):
        if i == 0:
            password = char[random.randint(0,len(char)-1)]
        else:
            password = password + char[random.randint(0,len(char)-1)]

    l_output = Label(root, text="password")
    l_output.pack()

    output= Entry(root)
    output.insert(10,password)
    output.pack()

button = Button(root, text="Generate", command=generate)
button.pack()

root.mainloop()
