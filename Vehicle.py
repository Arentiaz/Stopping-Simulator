import uuid
import numpy as np
#DT defined as a tenth of a second.

DT = 0.1
class Vehicle:
    def __init__(self, parameters):
        self.currentRoadIndex = parameters[4]
        #varies from 0.7-1.0g
        self.maxAcceleration = 9.8*(1-(parameters[2]/400))
        self.desiredTimeGap = parameters[5]
        self.reactionSpeed = int(parameters[3]*10)
        self.vehicleGap = [parameters[1]]*self.reactionSpeed*2
        self.v = [parameters[0]]*self.reactionSpeed*5
        self.a = 0
        self.desiredDistance = parameters[0]*self.desiredTimeGap
        self.stopped = False
        self.epoch = 0
        self.backLooking = parameters[6]

    # Update acceleration
    def updateAcceleration(self, lead, rear):
        if self.epoch > self.reactionSpeed*5:
            if self.backLooking == True:
                desiredBraking = self.maxAcceleration*(1-pow((self.v[-1]/(lead.v[-self.reactionSpeed]+3)),4) - pow(self.desiredDistance/(self.vehicleGap[-self.reactionSpeed])- (self.desiredDistance)/(rear.vehicleGap[-self.reactionSpeed]),2))
            else:
                desiredBraking = self.maxAcceleration*(1-pow((self.v[-1]/(lead.v[-self.reactionSpeed]+3)),4) - pow((self.desiredDistance/(self.vehicleGap[-self.reactionSpeed])),2))
            if desiredBraking > 0:
                self.a = min(desiredBraking, 1 + self.maxAcceleration)
            elif desiredBraking <= 0:
                self.a = max(desiredBraking, 1 - self.maxAcceleration)

    def update(self, lead, rear):
        self.epoch += 1
        if self.v[-1] >= 1 or self.a > 0:
            self.v.append(self.v[-1] + (self.a*DT)*self.currentRoadIndex)
            speedDiff = lead.v[-1] - self.v[-1] 
            self.vehicleGap.append(self.vehicleGap[-1] + speedDiff*DT + self.a*DT*DT*self.currentRoadIndex/2 - lead.a*DT*DT*self.currentRoadIndex/2)
            #determining how far this vehicle wants to 
            self.desiredDistance = max(lead.v[-1]*self.desiredTimeGap, 5)
        else:
            self.v.append(0)
            self.stopped = True
        self.updateAcceleration(lead, rear)
    
    def getGap(self):
        return self.vehicleGap[-1]
    
    def getState(self):
        return self.stopped
    
    def getSpeed(self):
        return self.v[-1]

class Ego(Vehicle):
    def updateAcceleration(self, lead, rear):
        #desiredBraking = self.maxAcceleration*(1-pow((self.v[-1]/(lead.v[-self.reactionSpeed]+3)),4) - pow((self.desiredDistance/(self.vehicleGap[-self.reactionSpeed])),2))
        desiredBraking = self.maxAcceleration*(1-pow((self.v[-1]/(lead.v[-self.reactionSpeed]+3)),4) - pow(self.desiredDistance/(self.vehicleGap[-self.reactionSpeed])- (self.desiredDistance)/(rear.vehicleGap[-self.reactionSpeed]),2))
        if desiredBraking > 0: 
            self.a = min(desiredBraking, self.maxAcceleration*1)
        elif desiredBraking <= 0:
            self.a = max(desiredBraking, -self.maxAcceleration*1)


        
