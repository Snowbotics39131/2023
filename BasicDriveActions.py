#!/usr/bin/env pybricks-micropython
from PortMap import *
from Actions import *
from Estimation import *
import jmath
simpleEstimate.initial(0, 0, 0)  # not really sure what to do here

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
    def __init__(self, getfunc, setfunc, target, kP=1, kI=0.01, kD=0.1, verbose=False):
        self.getfunc = getfunc
        self.setfunc = setfunc
        self.target = target
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.verbose=verbose
        self.olderror = (self.target-self.getfunc())/self.target
        self.ierror = self.olderror

    def config(self, target=None, kP=None, kI=None, kD=None, getfunc=None, setfunc=None, verbose=None):
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
        if verbose!=None:
            self.verbose=verbose

    def cycle(self):
        error = (self.target-self.getfunc())/self.target
        self.ierror += error
        derror = error-self.olderror
        if self.verbose:
            print(f'{self.kP*error+self.kI*self.ierror+self.kD*derror}={self.kP}*{error}+{self.kI}*{self.ierror}+{self.kD}*{derror}')
            #print(self.kP*error+self.kI*self.ierror+self.kD*derror)
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

        def setfunc(turn):
            motorLeft.run(200*(1+turn))
            motorRight.run(200*(1-turn))
        self.pid = PIDController(colorSensorLeft.reflection,
                                 setfunc,
                                 self.reflecttarget,
                                 self.kP,
                                 self.kI,
                                 self.kD)
        self.old_angle = 0
        self.old_distance = 0

    def start(self):
        driveBase.reset()

    def update(self):
        self.pid.cycle()
        new_angle = driveBase.angle()
        new_distance = driveBase.distance()
        simpleEstimate.changeInPose(Pose(0, 0, new_angle-self.old_angle))
        simpleEstimate.linearChange(new_distance-self.old_distance)
        self.old_angle = new_angle
        self.old_distance = new_distance

    def isFinished(self):
        return driveBase.distance() >= self.distance

    def done(self):
        motorLeft.brake()
        motorRight.brake()


class FollowLineRight(Action):
    name = 'FollowLineRight'

    def __init__(self, distance, kP=1, kI=0, kD=0.1, reflecttarget=35):
        self.distance = distance
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.reflecttarget = reflecttarget

        def setfunc(turn):
            motorLeft.run(200*(1-turn))
            motorRight.run(200*(1+turn))
        self.pid = PIDController(colorSensorRight.reflection,
                                 setfunc,
                                 self.reflecttarget,
                                 self.kP,
                                 self.kI,
                                 self.kD)
        self.old_angle = 0
        self.old_distance = 0

    def start(self):
        driveBase.reset()

    def update(self):
        self.pid.cycle()
        new_angle = driveBase.angle()
        new_distance = driveBase.distance()
        simpleEstimate.changeInPose(Pose(0, 0, new_angle-self.old_angle))
        simpleEstimate.linearChange(new_distance-self.old_distance)
        self.old_angle = new_angle
        self.old_distance = new_distance

    def isFinished(self):
        return driveBase.distance() >= self.distance

    def done(self):
        motorLeft.brake()
        motorRight.brake()


class FindLine(Action):
    name = 'FindLine'

    def __init__(self, kP=1, kI=0, kD=0.1, reflecttarget=35):
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.reflecttarget = reflecttarget
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
        self.old_angle = 0
        self.old_distance = 0

    def start(self):
        driveBase.reset()
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
        new_angle = driveBase.angle()
        new_distance = driveBase.distance()
        simpleEstimate.changeInPose(Pose(0, 0, new_angle-self.old_angle))
        simpleEstimate.linearChange(new_distance-self.old_distance)
        self.old_angle = new_angle
        self.old_distance = new_distance

    def isFinished(self):
        return self.state_left == 'done' and self.state_right == 'done'
class DriveStraightUltrasonic(Action):
    def __init__(self, distance, kP=7, kI=0, kD=3):
        self.distance=distance
        def setfunc(speed):
            motorLeft.run(-100*speed)
            motorRight.run(-100*speed)
        self.pid_controller=PIDController(ultrasonicSensor.distance,
                                          setfunc,
                                          distance,
                                          kP,
                                          kI,
                                          kD,)
    def start(self):
        pass
    def update(self):
        self.pid_controller.cycle()
    def done(self):
        motorLeft.brake()
        motorRight.brake()
    def isFinished(self):
        return abs(self.pid_controller.getfunc()-self.pid_controller.target)<=1
        #distance sensor rounds to mm, so this works
        #return self.pid_controller.getfunc()-self.pid_controller.target==0
class UltrasonicSquare(Action):
    #jigs should be at (8,2) and (2,5)
    #robot should be just above 'Challenge' logo
    def start(self):
        driveBase.settings(straight_speed=100, turn_rate=45)
        DriveStraightAction(-200).run()
        DriveTurnAction(90).run()
        DriveStraightAction(-200).run() #wall square
        DriveStraightAction(120).run()
        DriveTurnAction(-90).run()
        DriveStraightAction(150).run()
        DriveStraightUltrasonic(75).run()
        DriveTurnAction(-90).run()
        DriveStraightUltrasonic(125).run()
        DriveTurnAction(90).run()
    def update(self):
        pass
    def done(self):
        pass
    def isFinished(self):
        return True


if __name__ == '__main__':
    us=UltrasonicSquare()
    while True:
        us.run()