import uuid
import numpy as np
#DT defined as a tenth of a second.

DT = 0.1
class Vehicle:
    def __init__(self, config={}):
        # Set default configuration
        self.setDefaultConfig()
        
    def setDefaultConfig(self):    
        self.currentRoadIndex = 0

        #varies from 0.7-1.0g
        self.maxAcceleration = 9.8
        self.desiredTimeGap = 3
        self.reactionSpeed = 0
        self.desiredDistance = 0
        self.vehicleGap = 0
        self.v = 0
        self.a = 0
        self.stopped = False

    # Update acceleration
    def updateAcceleration(self, lead, rear):
        self.a = self.maxAcceleration*(1-(self.v/lead.v)^2 - (self.desiredDistance/(self.vehicleGap))^2)

    def update(self, lead, rear):
        # Update position and velocity
        if self.v >= 1:
            self.v += (self.a*DT)*self.currentRoadIndex
            self.vehicleGap += (self.v*DT + self.a*DT*DT*self.currentRoadIndex/2) - (lead.v*DT + lead.a*DT*DT*self.currentRoadIndex/2)
            #determining how far this vehicle wants to 
            self.desiredDistance = lead.v*self.desiredTimeGap 
        else:
            self.v = 0
            self.stopped = True

class Ego(Vehicle):
    def updateAcceleration(self, lead, rear):
        self.a = self.maxAcceleration*(1-(self.v/lead.v)^2 - ((self.desiredDistance/(self.vehicleGap))^2 - (self.desiredDistance/(rear.x))^2))


        