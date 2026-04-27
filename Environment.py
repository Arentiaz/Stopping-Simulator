import tkinter as tk
from tkinter import *
import Vehicle
import os
from PIL import ImageTk, Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#append to a list, all vehicle parameters per tick as a list, use numpy.
#use a while loop.
#whats the best way to add parameters?
#what if we make an actual popup with sliders to control vehicle parameters
#

#0 lSpeed.get(), 1 lBrakeWear.get(), 2 eSpeed.get(), 3 eDistance.get(), 4 eBrakeWear.get(), 5 fSpeed.get(), 6 fDistance.get(), 7 fBrakeWear.get(), 8 fReaction.get(), 9 roadIndex.get(), 10 eTimeGap.get(), 11 fTimeGap.get()


def simWindow(paramList):
    newWindow = Toplevel(master)
    newWindow.geometry("1500x500")
    img= Image.open("Car.png")
    img = ImageTk.PhotoImage(img.resize((74,42)))
    leadImage = Label(newWindow, image = img)
    egoImage = Label(newWindow, image = img)
    followerImage = Label(newWindow, image = img)

    #speed, distance, brake, reaction speed, road index, desired time gap
    wall = Vehicle.Vehicle([0,0,0,paramList[8],0,0, False])
    lead = Vehicle.Vehicle([paramList[0], paramList[0]*3.8, paramList[1], paramList[8], paramList[9], 3, False])
    ego = Vehicle.Vehicle([paramList[2], paramList[3], paramList[4], paramList[8], paramList[9], paramList[10], paramList[12]])
    follower = Vehicle.Vehicle([paramList[5], paramList[6], paramList[7], paramList[8], paramList[9], paramList[11], False])
    
    leadImage.place(x = 1350, y = 200)
    egoImage.place(x = 1350 - 74 - paramList[3], y = 200)
    followerImage.place(x = 1350 - 148 - paramList[3] -paramList[6], y = 200)

    run = Button(newWindow, text="Run",  command= lambda: updatePostitions(newWindow, egoImage, followerImage, wall, lead, ego, follower, {"leadDisplacement":[],
         "egoDisplacement":[], "followerDisplacement":[], "leadSpeed":[], "egoSpeed":[], "followerSpeed":[], "leadAcceleration":[], "egoAcceleration":[], "followerAcceleration":[]}))
    run.place(x = 1350/2, y = 50)
    newWindow.mainloop()

def calculatePositions(lead, ego, follower):
    return(lead.getGap(), ego.getGap(), follower.getGap())

def graphData(displacementData):
    leadGraph = pd.DataFrame(displacementData["leadDisplacement"], columns=["Lead"], index=range(len(displacementData["leadDisplacement"])))
    egoGraph = pd.DataFrame(displacementData["egoDisplacement"], columns=["Ego"], index=range(len(displacementData["egoDisplacement"])))
    followerGraph = pd.DataFrame(displacementData["followerDisplacement"], columns=["Follower"], index=range(len(displacementData["followerDisplacement"])))
    leadSpeed = pd.DataFrame(displacementData["leadSpeed"], columns=["Lead Speed"], index=range(len(displacementData["leadSpeed"])))
    egoSpeed = pd.DataFrame(displacementData["egoSpeed"], columns=["Ego Speed"], index=range(len(displacementData["egoSpeed"])))
    followerSpeed = pd.DataFrame(displacementData["followerSpeed"], columns=["Follower Speed"], index=range(len(displacementData["followerSpeed"])))
    leadAcceleration = pd.DataFrame(displacementData["leadAcceleration"], columns=["Lead Acceleration"], index=range(len(displacementData["leadAcceleration"])))
    egoAcceleration = pd.DataFrame(displacementData["egoAcceleration"], columns=["Ego Acceleration"], index=range(len(displacementData["egoAcceleration"])))
    followerAcceleration = pd.DataFrame(displacementData["followerAcceleration"], columns=["Follower Acceleration"], index=range(len(displacementData["followerAcceleration"])))
    #2 graphs, one for displacement, one for speed, x axis is time, y axis is displacement/speed, 3 lines per graph, one for each vehicle.
    
    fig, ax = plt.subplots(3, 3)
    ax[0,0].plot(leadSpeed, label="Lead Speed"); ax[0,0].set_xlabel("Time (s)"); ax[0,0].set_ylabel("Lead Speed (m/s)"); ax[0,0].legend()
    ax[1,0].plot(egoSpeed, label="Ego Speed"); ax[1,0].set_xlabel("Time (s)"); ax[1,0].set_ylabel("Ego Speed (m/s)"); ax[1,0].legend()
    ax[2,0].plot(followerSpeed, label="Follower Speed"); ax[2,0].set_xlabel("Time (s)"); ax[2,0].set_ylabel("Follower Speed (m/s)"); ax[2,0].legend()
    ax[0,1].plot(leadGraph, label="Lead Displacement"); ax[0,1].set_xlabel("Time (s)"); ax[0,1].set_ylabel("Lead Displacement (m)"); ax[0,1].legend()
    ax[1,1].plot(egoGraph, label="Ego Displacement"); ax[1,1].set_xlabel("Time (s)"); ax[1,1].set_ylabel("Ego Displacement (m)"); ax[1,1].legend()
    ax[2,1].plot(followerGraph, label="Follower Displacement"); ax[2,1].set_xlabel("Time (s)"); ax[2,1].set_ylabel("Follower Displacement (m)"); ax[2,1].legend()
    ax[0,2].plot(leadAcceleration, label="Lead Acceleration"); ax[0,2].set_xlabel("Time (s)"); ax[0,2].set_ylabel("Lead Acceleration (m/s^2)"); ax[0,2].legend()
    ax[1,2].plot(egoAcceleration, label="Ego Acceleration"); ax[1,2].set_xlabel("Time (s)"); ax[1,2].set_ylabel("Ego Acceleration (m/s^2)"); ax[1,2].legend()
    ax[2,2].plot(followerAcceleration, label="Follower Acceleration"); ax[2,2].set_xlabel("Time (s)"); ax[2,2].set_ylabel("Follower Acceleration (m/s^2)"); ax[2,2].legend()
    plt.show()

def updatePostitions(newWindow, egoImage, followerImage, wall, lead, ego, follower, displacementData):
    displacementData["leadDisplacement"].append(lead.getGap())
    displacementData["egoDisplacement"].append(ego.getGap())    
    displacementData["followerDisplacement"].append(follower.getGap())
    displacementData["leadSpeed"].append(lead.getSpeed())
    displacementData["egoSpeed"].append(ego.getSpeed())
    displacementData["followerSpeed"].append(follower.getSpeed())
    displacementData["leadAcceleration"].append(lead.getAcceleration())
    displacementData["egoAcceleration"].append(ego.getAcceleration())
    displacementData["followerAcceleration"].append(follower.getAcceleration()) 
    lead.update(wall, ego)
    ego.update(lead, follower)
    follower.update(ego, wall)
    egoImage.place(x = 1350 - 74 - ego.getGap(), y = 200)
    followerImage.place(x = 1350 - 2 * 74 - ego.getGap() - follower.getGap(), y = 200)
    if lead.getGap() < 0 or ego.getGap() < 0 or follower.getGap() < 0:
        print("Vehicle Collision:")
        print(lead.getGap(), ego.getGap(), follower.getGap())
        graphData(displacementData)
    elif lead.getState() == False or ego.getState() == False or follower.getState() == False:
        newWindow.after(5, updatePostitions, newWindow, egoImage, followerImage, wall, lead, ego, follower, displacementData)
    else:
        graphData(displacementData)


master = Tk()
master.eval('tk::PlaceWindow . center')
master.geometry("1000x400")
master.title("Collision Simulator")
Label(master, text="Modify Vehicle Parameters").grid(row=0, column=2, pady=5, padx = 5)
Label(master, text="Speed (m/s)").grid(row=1, column=2, pady=1, padx = 5)
Label(master, text="Distance (m)").grid(row=1, column=3, pady=1, padx = 5)
Label(master, text="Brake Wear (%)").grid(row=1, column=4, pady=1, padx = 5)
Label(master, text="Driver Desired Time Gap (s)").grid(row=1, column=5, pady=1, padx = 5)

lSpeed = Scale(master, from_=0, to=70, orient=HORIZONTAL, length=150)
lSpeed.set(20)
lBrakeWear = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=100)
lBrakeWear.set(0)

eSpeed = Scale(master, from_=0, to=70, orient=HORIZONTAL, length=150)
eSpeed.set(20)
eDistance = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=250)
eDistance.set(30)
eBrakeWear = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=100)
eBrakeWear.set(0)
eTimeGap = Scale(master, from_=0, to=4, resolution=0.1, orient=HORIZONTAL, length=200)
eTimeGap.set(3)

fSpeed = Scale(master, from_=0, to=70, orient=HORIZONTAL, length=150)
fSpeed.set(20)
fDistance = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=250)
fDistance.set(30)
fBrakeWear = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=100)
fBrakeWear.set(0)
fTimeGap = Scale(master, from_=0, to=4, resolution=0.1, orient=HORIZONTAL, length=200)
fTimeGap.set(3)

fReaction = Scale(master, from_=0.1, to=1, resolution=0.1, orient=HORIZONTAL, length=150)
fReaction.set(.2)
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

Label(master, text="Reaction Speed (s)").grid(row=5, column=1, pady=4, padx = 5)
fReaction.grid(row=5, column=2, pady=4, padx = 5)

Label(master, text="Road Index").grid(row=6, column=1, pady=4, padx = 5)
roadIndex.grid(row=6, column=2, pady=4, padx = 5)

Button(master, text="Render Ego as IDM",  command= lambda : simWindow([lSpeed.get(), lBrakeWear.get(), eSpeed.get(), eDistance.get(), fBrakeWear.get()
    , fSpeed.get(), fDistance.get(), fBrakeWear.get(), fReaction.get(), roadIndex.get(), eTimeGap.get(), fTimeGap.get(), False])).grid(row=7, column=2, pady=4, padx = 5)

Button(master, text="Render Ego as Back Looking IDM",  command= lambda : simWindow([lSpeed.get(), lBrakeWear.get(), eSpeed.get(), eDistance.get(), fBrakeWear.get()
    , fSpeed.get(), fDistance.get(), fBrakeWear.get(), fReaction.get(), roadIndex.get(), eTimeGap.get(), fTimeGap.get(), True])).grid(row=7, column=3, pady=4, padx = 5)
master.mainloop()
