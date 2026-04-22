import tkinter as tk
from tkinter import *
import Vehicle
#append to a list, all vehicle parameters per tick as a list, use numpy.
#use a while loop.
#whats the best way to add parameters?
#what if we make an actual popup with sliders to control vehicle parameters
#
def saveOptions(w1,w2):
    print(w1.get(), w2.get())

def openNewWindow():
    new_window = Toplevel(master)  # Create a new window
    new_window.title("New Window")
    new_window.geometry("400x300") 
    Label(new_window, text="This is a new window").pack(pady=20)
    w1 = Scale(new_window, from_=0, to=42, orient=HORIZONTAL)
    w1.set(0)
    w1.pack()
    w2 = Scale(new_window, from_=0, to=200, orient=HORIZONTAL)
    w2.set(0)
    w2.pack()
    Button(new_window, text='Save', command=lambda:[saveOptions(w1, w2), new_window.destroy()]).pack()
        

master = Tk()
master.geometry("300x200")
master.title("Collision Simulator")
Label(master, text="Modify Vehicle Parameters").grid(row=0, column=4, pady=5, padx = 5)

Label(master, text="Lead").grid(row=1, column=3, pady=4, padx = 5)
Button(master, text="Open New Window", command=openNewWindow).grid(row=1, column=4, pady=4, padx = 5)

Label(master, text="Ego").grid(row=2, column=3, pady=4, padx = 5)
Button(master, text="Open New Window", command=openNewWindow).grid(row=2, column=4, pady=4, padx = 5)

Label(master, text="Follower").grid(row=3, column=3, pady=4, padx = 5)
Button(master, text="Open New Window", command=openNewWindow).grid(row=3, column=4, pady=4, padx = 5)

Button(master, text="Run", command=master.destroy).grid(row=4, column=4, pady=4, padx = 5)

master.mainloop()
