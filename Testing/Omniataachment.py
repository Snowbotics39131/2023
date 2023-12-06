from Actions import *
from PortMap import *
from jmath import *
class OmniAttachment:
    def __init__(self,height,orientation):
        self.height=height
        self.orientation=orientation
omni = OmniAttachment(0,0)

class OmniLiftAction(Action):
    def __init__(self,height):
        self.height=height

    def start(self):
        motorBack.run_angle(self.height-omni.height*(360+270),wait=False)
        omni.height = self.height
    #override
    def update(self): pass

    #override
    def isFinished(self):
        return motorBack.done()

    #override    
    def done(self):

class OmniLiftAction(Action):
    def __init__(self,spin):
        self.spin=spin

    def start(self):
        spinDistance = jmath.shortestDirectionBetweenBearings(self.spin,omni.orientation)
        motorBack.run_angle(spinDistance,wait=False)
        omni.orientation = self.spin
    #override
    def update(self): pass

    #override
    def isFinished(self):
        return motorBack.done()
        
    #override    
    def done(self):