#!/usr/bin/env pybricks-micropython
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


class Pose:  # pose is the postion of a robot at an x y angle
    x = 0  # is from the left wall of the field are negative
    y = 0  # is from the orgin to the non orgin
    a = 0  # angle

    def __init__(self, x, y, a):  # constructor defines intial position
        self.x = x
        self.y = y
        self.a = a


class GoToPoint(SeriesAction):
    def __init__(self, location, destination):
        self.destination = destination
        self.location = location
        # creating a vector between location and destination
        vector = tuple((destination.x-location.x, destination.y-location.y))
        # using the arc tangent to detirmine the angle of the vector
        direction = jmath.atan2(vector[0], vector[1])
        # detirmine the shortest correction between our current angle and the angle of the shortest path
        turn = jmath.shortestDirectionBetweenBearings(direction, location.a)
        super().__init__(DriveTurnAction(turn),
                         DriveStraightAction((vector[0]**2+vector[1]**2)**0.5),
                         DriveTurnAction(jmath.shortestDirectionBetweenBearings(destination.a, direction)))


if __name__ == '__main__':
    gtp = GoToPoint(Pose(0, 0, 0), Pose(-250, 500, 180))
    while not gtp.isFinished():
        gtp.update()
