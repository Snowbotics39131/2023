from PortMap import *
from Actions import Action

class DriveStraightAction(Action):

#example action should probably share a drive actions file  
    def __init__(self,distance):
        self.distance = distance

    #overriding the method in the parent class
    def start(self):
        driveBase.straight(self.distance,wait=False)
    #override
    def update(self): pass
    #override
    def isFinished(self):
        if (driveBase.done()):
            print("Drive finished")
            return True    
        return False
    #override    
    def done(self): pass

class DriveTurnAction(Action):
 
    def __init__(self,angle):
        self.angle = angle

    #overriding the method in the parent class
    def start(self):
        driveBase.turn(self.angle,wait=False)
    #override
    def update(self): pass
    #override
    def isFinished(self):
        if (driveBase.done()):
            print("Drive finished")
            return True    
        return False
    #override    
    def done(self): pass

#make a Action that drives to a point like the functions in new.py using sub actions shown above hint look at the SeriesAction 

