from Actions import *
from BasicDriveActions import *
from PortMap import *
from pybricks.geometry import Axis
STRAIGHT_FACTOR=1
TURN_FACTOR=2
class ChallengeSquare(Action):
    def __init__(self):
        self.state_left='start'
        self.state_right='start'
        #not sure why lambdas aren't working here
        def a():
            return colorSensorLeft.hsv().s
        self.pid_left=PIDController(a, motorLeft.run, 50)
        def aa():
            return colorSensorRight.hsv().s
        self.pid_right=PIDController(aa, motorRight.run, 50)
    def start(self):
        #DriveStraightAction(-200*STRAIGHT_FACTOR).run()
        motorLeft.run(-300)
        motorRight.run(-300)
        maxaccy=0
        minaccy=0
        while (minaccy>-3000 or maxaccy<6500) and not hub.buttons.pressed():
            accy=hub.imu.acceleration(Axis.Y)
            if accy>maxaccy:
                maxaccy=accy
            if accy<minaccy:
                minaccy=accy
            print(minaccy, accy, maxaccy)
        motorLeft.stop()
        motorRight.stop()
        hub.speaker.beep()
        #while True:
        #    pass
        DriveStraightAction(100*STRAIGHT_FACTOR).run()
        DriveTurnAction(180*TURN_FACTOR).run()
        motorLeft.run(100)
        motorRight.run(100)
    def update(self):
        print(self.pid_left.getfunc(), self.pid_right.getfunc())
        if self.state_left=='start':
            if colorSensorLeft.color()==Color.RED:
                motorLeft.brake()
                self.state_left='pid'
        elif self.state_left=='pid':
            self.pid_left.cycle()
            if abs(self.pid_left.target-self.pid_left.getfunc())<=10:
                motorLeft.hold()
                hub.speaker.beep(250)
                self.state_left='done'
        if self.state_right=='start':
            if colorSensorRight.color()==Color.RED:
                motorRight.brake()
                self.state_right='pid'
        elif self.state_right=='pid':
            self.pid_right.cycle()
            if abs(self.pid_right.target-self.pid_right.getfunc())<=10:
                motorRight.hold()
                hub.speaker.beep(1000)
                self.state_right='done'
    def done(self):
        pass
    def isFinished(self):
        return self.state_left=='done'and self.state_right=='done'
if __name__=='__main__':
    challenge_square=ChallengeSquare()
    challenge_square.run()