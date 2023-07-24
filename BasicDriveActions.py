#!/usr/bin/env pybricks-micropython
from PortMap import *
from Actions import *
from Estimation import *
import jmath

class DriveStraightAction(Action):

#example action should probably share a drive actions file
    name = "DriveStraightAction"
    def __init__(self,distance):
        self.distance = distance
        
    #overriding the method in the parent class
    def start(self):
        simpleEstimate.addAction(self.name)
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
    def done(self):
        simpleEstimate.linearChange(driveBase.distance()) #better way
        simpleEstimate.removeAction(self.name)


class DriveTurnAction(Action):
    name = "DriveTurnAction"
    def __init__(self,angle):
        self.angle = angle

    #overriding the method in the parent class
    def start(self):
        simpleEstimate.addAction(self.name)
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
    def done(self): 
        simpleEstimate.bestPose.a = driveBase.angle() #better way
        simpleEstimate.removeAction(self.name)

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
    name = "GotoToPoint"

    def __init__(self, destination):
        location = simpleEstimate.getCurrentPose()
        # creating a vector between location and destination
        vector = tuple((destination.x-location.x, destination.y-location.y))
        # using the arc tangent to detirmine the angle of the vector
        direction = jmath.atan2(vector[0], vector[1])
        # detirmine the shortest correction between our current angle and the angle of the shortest path
        turn = jmath.shortestDirectionBetweenBearings(direction, location.a)
        super().__init__(DriveTurnAction(turn),
                         DriveStraightAction((vector[0]**2+vector[1]**2)**0.5),
                         DriveTurnAction(jmath.shortestDirectionBetweenBearings(destination.a, direction)))


class PIDController:
    def __init__(self, getfunc, setfunc, target, kP=1, kI=0.01, kD=0.1):
        self.getfunc = getfunc
        self.setfunc = setfunc
        self.target = target
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.olderror = (self.target-self.getfunc())/self.target
        self.ierror = self.olderror

    def config(self, target=None, kP=None, kI=None, kD=None, getfunc=None, setfunc=None):
        if target != None:
            self.target = target
        if kP != None:
            self.kP = kP
        if kI != None:
            self.kI = kI
        if kD != None:
            self.kD = kD
        if getfunc != None:
            self.getfunc = getfunc
        if setfunc != None:
            self.setfunc = setfunc

    def cycle(self):
        error = (self.target-self.getfunc())/self.target
        self.ierror += error
        derror = error-self.olderror
        self.setfunc(self.kP*error+self.kI*self.ierror+self.kD*derror)
        self.olderror = error


class FollowLineLeft(Action):
    name = 'FollowLineLeft'

    def __init__(self, distance, kP=1, kI=0, kD=0.1, reflecttarget=35):
        self.distance = distance
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.reflecttarget = reflecttarget

    def start(self):
        def setfunc(self, turn):
            motorLeft.run(200*(1+turn))
            motorRight.run(200*(1-turn))
        self.pid = PIDController(colorSensorLeft.reflection,
                                 setfunc,
                                 self.reflecttarget,
                                 self.kP,
                                 self.kI,
                                 self.kD)
        driveBase.reset()

    def update(self):
        self.pid.cycle()

    def isFinished(self):
        return driveBase.distance() >= self.distance


class FollowLineRight(Action):
    name = 'FollowLineRight'

    def __init__(self, distance, kP=1, kI=0, kD=0.1, reflecttarget=35):
        self.distance = distance
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.reflecttarget = reflecttarget

    def start(self):
        def setfunc(self, turn):
            motorLeft.run(200*(1-turn))
            motorRight.run(200*(1+turn))
        self.pid = PIDController(colorSensorRight.reflection,
                                 setfunc,
                                 self.reflecttarget,
                                 self.kP,
                                 self.kI,
                                 self.kD)
        driveBase.reset()

    def update(self):
        self.pid.cycle()

    def isFinished(self):
        return driveBase.distance() >= self.distance


class FindLine(Action):
    name = 'FindLine'

    def __init__(self, kP=1, kI=0, kD=0.1, reflecttarget=35):
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.reflecttarget = reflecttarget

    def start(self):
        self.pid_left = PIDController(colorSensorLeft.reflection,
                                      lambda speed: motorLeft.run(50*speed),
                                      self.reflecttarget,
                                      self.kP,
                                      self.kI,
                                      self.kD)
        self.pid_right = PIDController(colorSensorRight.reflection,
                                       lambda speed: motorRight.run(50*speed),
                                       self.reflecttarget,
                                       self.kP,
                                       self.kI,
                                       self.kD)
        self.white = 60
        self.black = 30
        self.state_left = 'start'
        self.state_right = 'start'
        motorLeft.run(100)
        motorRight.run(100)

    def update(self):
        # start -> white -> black -> pid -> done
        if self.state_left == 'start':
            if colorSensorLeft.reflection() >= self.white:
                self.state_left = 'white'
        if self.state_left == 'white':
            if colorSensorLeft.reflection() <= self.black:
                self.state_left = 'black'
        if self.state_left == 'black':
            if colorSensorLeft.reflection() >= self.white:
                motorLeft.brake()
                self.state_left = 'pid'
        if self.state_left == 'pid':
            self.pid_left.cycle()
            if abs(self.pid_left.target-self.pid_left.getfunc()) <= 2:
                motorLeft.hold()
                self.state_left = 'done'
        if self.state_right == 'start':
            if colorSensorRight.reflection() >= self.white:
                self.state_right = 'white'
        if self.state_right == 'white':
            if colorSensorRight.reflection() <= self.black:
                self.state_right = 'black'
        if self.state_right == 'black':
            if colorSensorRight.reflection() >= self.white:
                motorRight.brake()
                self.state_right = 'pid'
        if self.state_right == 'pid':
            self.pid_right.cycle()
            if abs(self.pid_right.target-self.pid_right.getfunc()) <= 2:
                motorRight.hold()
                self.state_right = 'done'

    def isFinished(self):
        return self.state_left == 'done' and self.state_right == 'done'


if __name__ == '__main__':
    # gtp = GoToPoint(Pose(-250, 500, 180))
    # while not gtp.isFinished():
    #     gtp.update()
    example = SeriesAction(FindLine(),
                           # -57 will probably need to be changed.
                           DriveStraightAction(-57),
                           DriveTurnAction(90),
                           FollowLineLeft(500),
                           DriveTurnAction(180),
                           FollowLineRight(500))
    while not example.isFinished():
        example.update()
