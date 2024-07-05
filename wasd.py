from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog


def W():
    messagebox.showinfo(title="show info", message="You moved up!")

def A():
    messagebox.showinfo(title="show info", message="You moved left!")


def S():
    messagebox.showinfo(title="show info", message="You moved down!")

def D():
    messagebox.showinfo(title="show info", message="You moved right!")

window = Tk()
window.title("WASD")

frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)
frame.pack()

Button(frame, text="W", font=("Consolas", 25), width=3, command=W).pack(side=TOP)
Button(frame, text="A", font=("Consolas", 25), width=3, command=A).pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 25), width=3, command=S).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 25), width=3, command=D).pack(side=LEFT)

window.mainloop()
