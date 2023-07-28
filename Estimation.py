from PortMap import *
import jmath
class Pose:  # pose is the postion of a robot at an x y angle
    x = 0  # is from the left wall of the field are negative
    y = 0  # is from the orgin to the non orgin
    a = 0  # angle

    def __init__(self, x, y, a):  # constructor defines intial position
        self.x = x
        self.y = y
        self.a = a
    
    def appendPose(self,pose):
        self.x += pose.x
        self.y += pose.y
        self.a = (self.a + pose.a)%360 #not sure this is right

class SimpleEstimate:
    log = []
    action = []
    def __init__(self):
        pass
    def initial(self, x,y,a): # constructor defines intial position
        self.bestPose = Pose(x,y,a)
        self.missionTimer = StopWatch()
        self.update()
    def changeInPose(self, pose):
        self.bestPose.appendPose(pose)
        self.update()
    def linearChange(self,distance):
        "uses current bestPose angle"
        angle = self.bestPose.a
        self.bestPose.appendPose(Pose(distance*jmath.cos(angle),distance*jmath.sin(angle),0))
    def getCurrentPose(self):
        return self.bestPose
    def update(self):
        #self.log.append([self.missionTimer.time(),self.action,self.bestPose.x,self.bestPose.y,self.bestPose.a]) 
        pass
    def addAction(self,name):
        self.action.append(name)
        self.update()
    def removeAction(self,name):
        self.action.remove(name)
        self.update()

simpleEstimate = SimpleEstimate()