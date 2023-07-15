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
    def __init__(self, location, destination):
        # creating a vector between location and destination
        vector = tuple((destination.x-location.x, destination.y-location.y))
        # using the arc tangent to detirmine the angle of the vector
        direction = jmath.atan2(vector[0], vector[1])
        # detirmine the shortest correction between our current angle and the angle of the shortest path
        turn = jmath.shortestDirectionBetweenBearings(direction, location.a)
        self.angle = turn
        self.vector = vector
        self.direction = direction


class GoToPoint_Straight(DriveStraightAction):
    def __init__(self, vector):
        self.distance = (vector[0]**2+vector[1]**2)**0.5  # drive along the vector with magnitude


class GoToPoint_EndTurn(DriveTurnAction):
    def __init__(self, destination, direction):
        # turning to final orientation should be inline with destination
        self.angle = jmath.shortestDirectionBetweenBearings(destination.a, direction)


GoToPoint = SeriesAction(GoToPoint_StartTurn, GoToPoint_Straight, GoToPoint_EndTurn)
# first attempt - doesn't work yet
