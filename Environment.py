import tkinter as tk
from tkinter import *
import Vehicle
import os
from PIL import ImageTk, Image
#append to a list, all vehicle parameters per tick as a list, use numpy.
#use a while loop.
#whats the best way to add parameters?
#what if we make an actual popup with sliders to control vehicle parameters
#


def saveOptions(w1,w2):
    print(w1.get(), w2.get())

def openNewWindow(vehicle):
    new_window = Toplevel(master)  # Create a new window
    new_window.title("New Window")
    new_window.geometry("400x300") 
    Label(new_window, text="Parameters for " + vehicle + "vehicle ").pack(pady=20)
    w1 = Scale(new_window, from_=0, to=42, orient=HORIZONTAL)
    w1.set(0)
    w1.pack()
    w2 = Scale(new_window, from_=0, to=200, orient=HORIZONTAL)
    w2.set(0)
    w2.pack()
    Button(new_window, text='Save', command= lambda:[saveOptions(w1, w2), new_window.destroy()]).pack()

def runSim(paramList):
    new_window = Toplevel(master)
    img= ImageTk.PhotoImage(Image.open("Car.png"))
    panel = Label(new_window, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    new_window.mainloop()

master = Tk()
master.geometry("800x400")
master.title("Collision Simulator")
Label(master, text="Modify Vehicle Parameters").grid(row=0, column=2, pady=5, padx = 5)
Label(master, text="Speed (km/hr)").grid(row=1, column=2, pady=1, padx = 5)
Label(master, text="Distance (m)").grid(row=1, column=3, pady=1, padx = 5)
Label(master, text="Brake Wear (%)").grid(row=1, column=4, pady=1, padx = 5)

lSpeed = Scale(master, from_=0, to=150, orient=HORIZONTAL, length=150)
lSpeed.set(60)
lDistance = Scale(master, from_=0, to=500, orient=HORIZONTAL, length=250)
lDistance.set(150)
lBrakeWear = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=100)
lBrakeWear.set(0)

eSpeed = Scale(master, from_=0, to=150, orient=HORIZONTAL, length=150)
eSpeed.set(60)
eDistance = Scale(master, from_=0, to=500, orient=HORIZONTAL, length=250)
eDistance.set(150)
eBrakeWear = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=100)
eBrakeWear.set(0)

fSpeed = Scale(master, from_=0, to=150, orient=HORIZONTAL, length=150)
fSpeed.set(60)
fDistance = Scale(master, from_=0, to=500, orient=HORIZONTAL, length=250)
fDistance.set(150)
fBrakeWear = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=100)
fBrakeWear.set(0)

fReaction = Scale(master, from_=0, to=4.5, resolution=0.1, orient=HORIZONTAL, length=150)
fReaction.set(2.5)
roadIndex = Scale(master, from_=0.5, to=1, resolution=0.05, orient=HORIZONTAL, length=150)
roadIndex.set(0.9)


Label(master, text="Lead").grid(row=2, column=1, pady=4, padx = 5)
lSpeed.grid(row=2, column=2, pady=4, padx = 5)
lDistance.grid(row=2, column=3, pady=4, padx = 5)
lBrakeWear.grid(row=2, column=4, pady=4, padx = 5)
#var = int()
#text = Entry(master, textvariable=var, Event = lSpeed.set(var)).grid(row=3, column=21, pady=4, padx = 5)

Label(master, text="Ego").grid(row=3, column=1, pady=4, padx = 5)
#Button(master, text="Open New Window", command= lambda : openNewWindow("Ego")).grid(row=2, column=4, pady=4, padx = 5)
eSpeed.grid(row=3, column=2, pady=4, padx = 5)
eDistance.grid(row=3, column=3, pady=4, padx = 5)
eBrakeWear.grid(row=3, column=4, pady=4, padx = 5)

Label(master, text="Follower").grid(row=4, column=1, pady=4, padx = 5)
#Button(master, text="Open New Window", command= lambda : openNewWindow("Follower")).grid(row=3, column=4, pady=4, padx = 5)
fSpeed.grid(row=4, column=2, pady=4, padx = 5)
fDistance.grid(row=4, column=3, pady=4, padx = 5)
fBrakeWear.grid(row=4, column=4, pady=4, padx = 5)

Label(master, text="Reaction Speed").grid(row=5, column=1, pady=4, padx = 5)
fReaction.grid(row=5, column=2, pady=4, padx = 5)

Label(master, text="Road Index").grid(row=6, column=1, pady=4, padx = 5)
roadIndex.grid(row=6, column=2, pady=4, padx = 5)

Button(master, text="Run",  command= lambda : runSim([lSpeed.get(), lDistance.get(), lBrakeWear.get(), eSpeed.get(), eDistance.get(), fBrakeWear.get(), fSpeed.get(), fDistance.get(), fBrakeWear.get(), fReaction.get(), roadIndex.get()])).grid(row=7, column=3, pady=4, padx = 5)

master.mainloop()
