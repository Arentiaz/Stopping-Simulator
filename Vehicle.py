import uuid
import numpy as np
#DT defined as a tenth of a second.

DT = 0.1
class Vehicle:
    def __init__(self, parameters):
        self.currentRoadIndex = parameters[4]
        #varies from 0.7-1.0g
        self.maxAcceleration = 9.8*(1-parameters[2]/4)
        self.desiredTimeGap = parameters[5]
        self.reactionSpeed = parameters[3]
        self.vehicleGap = parameters[1]
        self.v = parameters[0]
        self.a = 0
        self.desiredDistance = self.v*self.desiredTimeGap
        self.stopped = False

    # Update acceleration
    def updateAcceleration(self, lead, rear):
        self.a = self.maxAcceleration*(1-pow((self.v/60),4) - pow((self.desiredDistance/(self.vehicleGap)),2))

    def update(self, lead, rear):
        # Update position and velocity
        if self.v >= 1:
            self.v += (self.a*DT)*self.currentRoadIndex
            self.vehicleGap -= (self.v*DT + self.a*DT*DT*self.currentRoadIndex/2) + (lead.v*DT + lead.a*DT*DT*self.currentRoadIndex/2)
            #determining how far this vehicle wants to 
            self.desiredDistance = max(self.v*self.desiredTimeGap, 3)
        else:
            self.v = 0
            self.stopped = True
        self.updateAcceleration(lead, rear)
    
    def getGap(self):
        return self.vehicleGap
    
    def getState(self):
        return self.stopped

class Ego(Vehicle):
    def updateAcceleration(self, lead, rear):
        self.a = self.maxAcceleration*(1-pow((self.v/60),4) - pow(self.desiredDistance/(self.vehicleGap),2) - pow((self.desiredDistance/(rear.vehicleGap)),2))


        
