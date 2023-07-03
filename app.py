from tkinter import *
from random import randint

App =Tk()
App.title('Random Generator')
App.geometry('350x100')

# Display = Label(App, text='Application Window')
# Display.pack()

def show_msg():
    msg = Label(App, text=randint(1,100))
    msg.pack()
B = Button(App, text='Generate', command=show_msg)
B.pack()

App.mainloop()
