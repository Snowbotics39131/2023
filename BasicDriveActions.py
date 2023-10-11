#!/usr/bin/env pybricks-micropython
from PortMap import *
from Actions import *
from Estimation import *
from pybricks.geometry import Axis
import jmath
simpleEstimate.initial(0, 0, 0)  # not really sure what to do here

class DriveStraightAction(Action):

#example action should probably share a drive actions file
    name = "DriveStraightAction"
    def __init__(self,distance, speed=None):
        self.distance = distance
        self.speed=speed
        
    #overriding the method in the parent class
    def start(self):
        simpleEstimate.addAction(self.name)
        if self.speed is not None:
            driveBase.settings(straight_speed=self.speed)
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
class PointIntegral:
    def __init__(self, first_point, name=''): #name for testing only, remove later
        self.value=0
        self.error=0
        self.prev_point=first_point
        self.name=name
    def add_point(self, point):
        trap_added_area=0.5*(point[1]+self.prev_point[1])*(point[0]-self.prev_point[0])
        max_added_area=point[1]*(point[0]-self.prev_point[0])
        self.value+=trap_added_area
        self.error+=abs(max_added_area-trap_added_area)
        #print(f'{self.name} {trap_added_area}=0.5*({point[1]}+{self.prev_point[1]})*({point[0]}-{self.prev_point[0]}) {self.value}')
        self.prev_point=point
    def __float__(self):
        return self.value
    def __int__(self):
        return int(self.value)
    def __str__(self):
        return f'{self.value} +- {self.error}' #PyBricks cannot render ± sign
def weighted_average(values, weights=None):
    if weights is None:
        return sum(values)/len(values)
    else:
        values=[i[0]*i[1] for i in zip(values, weights)]
        return sum(values)/sum(weights)
class DriveStraightAccurate(Action):
    def __init__(self, distance, speed=None, weights=None, compensate=False, verbose=False):
        '''weights is [ultrasonic, imu, driveBase, attempted]'''
        self.distance=distance
        self.speed=speed
        if weights is None:
            self.weights=[1, 0, 2, 1]
        else:
            self.weights=weights
        #print('init', self.weights, weights)
        self.compensate=compensate
        self.verbose=verbose
        self.stopwatch=StopWatch()
    def start(self):
        if device.has_ultrasonicSensor:
            self.start_ultrasonic_distance=ultrasonicSensor.distance()
            if self.start_ultrasonic_distance==2000:
                self.ultrasonic_reliable=False
            else:
                self.ultrasonic_reliable=True
        time=self.stopwatch.time()/1000
        self.imu_vel=PointIntegral((time, hub.imu.acceleration(Axis.Y)), 'vel')
        self.imu_pos=PointIntegral((time, self.imu_vel.value), 'pos')
        driveBase.reset()
        if self.speed is not None:
            driveBase.settings(straight_speed=self.speed)
        driveBase.straight(self.distance, wait=False)
    def update(self):
        time=self.stopwatch.time()/1000
        self.imu_vel.add_point((time, hub.imu.acceleration(Axis.Y)))
        self.imu_pos.add_point((time, self.imu_vel.value))
    def done(self):
        if device.has_ultrasonicSensor:
            end_ultrasonic_distance=ultrasonicSensor.distance()
            if end_ultrasonic_distance==2000:
                self.ultrasonic_reliable=False
            ultrasonic_distance=self.start_ultrasonic_distance-end_ultrasonic_distance
        imu_distance=self.imu_pos.value
        driveBase_distance=driveBase.distance()
        attempted_distance=self.distance
        if self.verbose:
            if device.has_ultrasonicSensor:
                if self.ultrasonic_reliable:
                    print(f'ultrasonic\t{ultrasonic_distance} (init {self.start_ultrasonic_distance}, end {end_ultrasonic_distance})')
                else:
                    print('ultrasonic out of range')
            else:
                print('ultrasonic sensor not connected')
            print(f'imu       \t{self.imu_pos}')
            print(f'driveBase \t{driveBase_distance}')
        print(f'attempted \t{attempted_distance}')
        if device.has_ultrasonicSensor and self.ultrasonic_reliable:
            est_distance=weighted_average((
                ultrasonic_distance,
                imu_distance,
                driveBase_distance,
                attempted_distance
            ), self.weights)
        else:
            #del(self.weights[0])
            self.weights[0]=0
            #print('after 0', self.weights)
            est_distance=weighted_average((
                0,
                imu_distance,
                driveBase_distance,
                attempted_distance
            ), self.weights)
        print(f'estimated \t{est_distance}')
        if self.compensate:
            print(f'driving {self.distance-est_distance}')
            DriveStraightAction(self.distance-est_distance).run()
        else:
            print('compensation disabled')
    def isFinished(self):
        return driveBase.done()


if __name__ == '__main__':
    dsa=DriveStraightAccurate(100, compensate=True, verbose=True)
    dsa.run()