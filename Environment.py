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

def simWindow(paramList):
    newWindow = Toplevel(master)
    newWindow.geometry("1500x500")
    img= Image.open("Car.png")
    img = ImageTk.PhotoImage(img.resize((74,42)))
    leadImage = Label(newWindow, image = img)
    egoImage = Label(newWindow, image = img)
    followerImage = Label(newWindow, image = img)

    leadImage.place(x=1350, y =200)
    egoImage.place(x=1350 - 74 - paramList[3], y =200)
    followerImage.place(x=1350 - 148 - paramList[3] -paramList[6], y =200)
    newWindow.mainloop()




master = Tk()
master.eval('tk::PlaceWindow . center')
master.geometry("1000x400")
master.title("Collision Simulator")
Label(master, text="Modify Vehicle Parameters").grid(row=0, column=2, pady=5, padx = 5)
Label(master, text="Speed (km/hr)").grid(row=1, column=2, pady=1, padx = 5)
Label(master, text="Distance (m)").grid(row=1, column=3, pady=1, padx = 5)
Label(master, text="Brake Wear (%)").grid(row=1, column=4, pady=1, padx = 5)
Label(master, text="Driver Desired Time Gap (s)").grid(row=1, column=5, pady=1, padx = 5)

lSpeed = Scale(master, from_=0, to=150, orient=HORIZONTAL, length=150)
lSpeed.set(60)
lBrakeWear = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=100)
lBrakeWear.set(0)

eSpeed = Scale(master, from_=0, to=150, orient=HORIZONTAL, length=150)
eSpeed.set(60)
eDistance = Scale(master, from_=0, to=500, orient=HORIZONTAL, length=250)
eDistance.set(150)
eBrakeWear = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=100)
eBrakeWear.set(0)
eTimeGap = Scale(master, from_=0, to=4, resolution=0.1, orient=HORIZONTAL, length=200)
eTimeGap.set(3)

fSpeed = Scale(master, from_=0, to=150, orient=HORIZONTAL, length=150)
fSpeed.set(60)
fDistance = Scale(master, from_=0, to=500, orient=HORIZONTAL, length=250)
fDistance.set(150)
fBrakeWear = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=100)
fBrakeWear.set(0)
fTimeGap = Scale(master, from_=0, to=4, resolution=0.1, orient=HORIZONTAL, length=200)
fTimeGap.set(3)

fReaction = Scale(master, from_=0, to=4.5, resolution=0.1, orient=HORIZONTAL, length=150)
fReaction.set(2.5)
roadIndex = Scale(master, from_=0.5, to=1, resolution=0.05, orient=HORIZONTAL, length=150)
roadIndex.set(0.9)


Label(master, text="Lead").grid(row=2, column=1, pady=4, padx = 5)
lSpeed.grid(row=2, column=2, pady=4, padx = 5)
lBrakeWear.grid(row=2, column=4, pady=4, padx = 5)
#var = int()
#text = Entry(master, textvariable=var, Event = lSpeed.set(var)).grid(row=3, column=21, pady=4, padx = 5)

Label(master, text="Ego").grid(row=3, column=1, pady=4, padx = 5)
#Button(master, text="Open New Window", command= lambda : openNewWindow("Ego")).grid(row=2, column=4, pady=4, padx = 5)
eSpeed.grid(row=3, column=2, pady=4, padx = 5)
eDistance.grid(row=3, column=3, pady=4, padx = 5)
eBrakeWear.grid(row=3, column=4, pady=4, padx = 5)
eTimeGap.grid(row=3, column=5, pady=4, padx = 5)

Label(master, text="Follower").grid(row=4, column=1, pady=4, padx = 5)
#Button(master, text="Open New Window", command= lambda : openNewWindow("Follower")).grid(row=3, column=4, pady=4, padx = 5)
fSpeed.grid(row=4, column=2, pady=4, padx = 5)
fDistance.grid(row=4, column=3, pady=4, padx = 5)
fBrakeWear.grid(row=4, column=4, pady=4, padx = 5)
fTimeGap.grid(row=4, column=5, pady=4, padx = 5)

Label(master, text="Reaction Speed").grid(row=5, column=1, pady=4, padx = 5)
fReaction.grid(row=5, column=2, pady=4, padx = 5)

Label(master, text="Road Index").grid(row=6, column=1, pady=4, padx = 5)
roadIndex.grid(row=6, column=2, pady=4, padx = 5)

Button(master, text="Run",  command= lambda : simWindow([lSpeed.get(), lBrakeWear.get(), eSpeed.get(), eDistance.get(), fBrakeWear.get()
    , fSpeed.get(), fDistance.get(), fBrakeWear.get(), fReaction.get(), roadIndex.get(), eTimeGap.get(), fTimeGap.get()])).grid(row=7, column=3, pady=4, padx = 5)

master.mainloop()
