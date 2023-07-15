from PortMap import *
from Actions import *
import jmath

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
class GoToPoint_StartTurn(DriveTurnAction):
    def __init__(self, selfself):
        # creating a vector between location and destination
        vector = tuple((selfself.destination.x-selfself.location.x,
                       selfself.destination.y-selfself.location.y))
        # using the arc tangent to detirmine the angle of the vector
        direction = jmath.atan2(vector[0], vector[1])
        # detirmine the shortest correction between our current angle and the angle of the shortest path
        turn = jmath.shortestDirectionBetweenBearings(direction, selfself.location.a)
        self.angle = turn
        self.vector = vector
        self.direction = direction
        selfself.angle = turn
        selfself.vector = vector
        selfself.direction = direction


class GoToPoint_Straight(DriveStraightAction):
    def __init__(self, selfself):
        # drive along the vector with magnitude
        self.distance = (selfself.vector[0]**2+selfself.vector[1] ** 2)**0.5


class GoToPoint_EndTurn(DriveTurnAction):
    def __init__(self, selfself):
        # turning to final orientation should be inline with destination
        self.angle = jmath.shortestDirectionBetweenBearings(
            selfself.destination.a, selfself.direction)


GoToPoint = SeriesAction()
GoToPoint = SeriesAction(GoToPoint_StartTurn(GoToPoint),
                         GoToPoint_Straight(GoToPoint),
                         GoToPoint_EndTurn(GoToPoint))
for i in enumerate(GoToPoint.mRemainingActions):
    GoToPoint.mRemainingActions[i[0]].selfself = GoToPoint
