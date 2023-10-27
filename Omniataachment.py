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
        motorCenter.run_angle(1000,(self.height-omni.height)*(360+270),wait=False)
        omni.height = self.height
    #override
    def update(self): pass

    #override
    def isFinished(self):
        return motorCenter.done()
  
    #override    
    def done(self):
        pass
        
class OmniorientationAction(Action):
    def __init__(self,orientation):
        self.orientation=orientation

    def start(self):
        orientationDistance = jmath.shortestDirectionBetweenBearings(self.orientation,omni.orientation)
        motorBack.run_angle(500,self.orientation*5,wait=False)
        motorCenter.run_angle(100,-self.orientation,wait=False)
        omni.orientation = self.orientation
    #override
    def update(self): pass

    #override
    def isFinished(self):
        return motorBack.done()
        
    #override    
    def done(self): pass
        
if __name__ == '__main__':
    # gtp = GoToPoint(Pose(-250, 500, 180))
    # while not gtp.isFinished():
    #     gtp.update()
    while True:
        example = OmniLiftAction(0)
        example.start()
        while not example.isFinished():
            example.update()
        example.done()
        example = OmniorientationAction(360)
        example.start()
        while not example.isFinished():
            example.update()
        example.done()
        example = OmniLiftAction(1)
        example.start()
        while not example.isFinished():
            example.update()
        example.done()