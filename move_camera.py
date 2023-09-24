#red home
#4 squares north
#1 square east
#facing east
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from PortMap import *
SPEED_GEAR_RATIO=-2
ANGLE_GEAR_RATIO=2
print(driveBase.settings())
class SpinMotorTime(Action):
    def __init__(self, speed, time):
        self.speed=speed
        self.time=time
    def start(self):
        motorCenter.run_time(self.speed, self.time, wait=False)
    def update(self):
        pass
    def done(self):
        pass
    def isFinished(self):
        return motorCenter.done()
class SpinMotorUntilStalled(Action):
    def __init__(self, *args, **kwargs):
        '''
        speed, then=Stop.COAST, duty_limit=None
        '''
        #kwargs['wait']=False
        self.args=args
        self.kwargs=kwargs
    def start(self):
        motorCenter.run_until_stalled(*self.args, **self.kwargs)
    def update(self):
        pass
    def done(self):
        pass
    def isFinished(self):
        return motorCenter.done()
class ChangeDriveBaseSettings(Action):
    def __init__(self, *args, **kwargs):
        self.args=args
        self.kwargs=kwargs
    def start(self):
        driveBase.settings(*self.args, **self.kwargs)
    def update(self):
        pass
    def isFinished(self):
        return True
    def done(self):
        pass
wait=True
def waitForButtonPressWithMessage(message):
    print(message)
    if wait:
        while not hub.buttons.pressed():
            pass
class MoveCamera(MissionBase):
    def routine(self):
        ChangeDriveBaseSettings(straight_speed=50, turn_rate=45)
        waitForButtonPressWithMessage('I will do the first SpinMotorUntilStalled')
        self.runAction(SpinMotorUntilStalled(300*SPEED_GEAR_RATIO))
        waitForButtonPressWithMessage('I will turn the motor -25 degrees')
        self.runAction(SpinMotor(100*SPEED_GEAR_RATIO, -25*ANGLE_GEAR_RATIO))
        waitForButtonPressWithMessage('I will turn 10 degrees')
        self.runAction(DriveTurnAction(10))
        waitForButtonPressWithMessage('I will drive 28mm')
        self.runAction(DriveStraightAction(28))
        waitForButtonPressWithMessage('I will turn -20 degrees')
        self.runAction(DriveTurnAction(-20))
        waitForButtonPressWithMessage('I will move over the lever')
        self.runAction(SpinMotor(200*SPEED_GEAR_RATIO, -45*ANGLE_GEAR_RATIO))
        self.runAction(DriveTurnAction(-3))
        self.runAction(SpinMotor(200*SPEED_GEAR_RATIO, 45*ANGLE_GEAR_RATIO))
        waitForButtonPressWithMessage('I will run the second SpinMotorUntilStalled')
        self.runAction(SpinMotorUntilStalled(300*SPEED_GEAR_RATIO))
        waitForButtonPressWithMessage('I will hold the motor down for 3 seconds and drive')
        self.runAction(ParallelAction(
            SpinMotorTime(30*SPEED_GEAR_RATIO, 3000),
            SeriesAction(
                DriveStraightAction(-50),
                DriveTurnAction(-45),
                DriveStraightAction(100),
                DriveTurnAction(-90)
            )
        ))
        waitForButtonPressWithMessage('I will turn the motor -90 degrees')
        self.runAction(SpinMotor(300*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO))
#red home
#13 squares north
#1 square east
#facing north
#attachment up
class Dragon(MissionBase):
    def routine(self):
        self.runAction(DriveTurnAction(45))
#near red home
#580mm north
#230mm east
#facing north
class GetToPink(MissionBase):
    def __init__(self, color='pink'):
        self.color=color
    def routine(self):
        if self.color=='blue':
            times=0
        elif self.color in ('orange', 'yellow'):
            times=2
        elif self.color=='pink':
            times=1
        else:
            raise ValueError(f'Invalid color: {self.color}')
        for i in range(times):
            self.runAction(SeriesAction(
                #SpinMotor(400*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO),
                DriveStraightAction(30),
                #SpinMotorTime(400*SPEED_GEAR_RATIO, 2000),
                SpinMotorUntilStalled(400*SPEED_GEAR_RATIO),
                DriveStraightAction(-30)
            ))
#start with blue piece on back up against sliders
class SoundMixer(MissionBase):
    def routine(self):
        driveBase.settings(turn_rate=90)
        self.runAction(SeriesAction(
            DriveStraightAction(-90),
            DriveTurnAction(90)
        ))
class Chicken(MissionBase):
    def routine(self):
        while True:
            self.runAction(SeriesAction(
                SpinMotor(200*SPEED_GEAR_RATIO, -135*ANGLE_GEAR_RATIO),
                ParallelAction(
                    SpinMotor(200*SPEED_GEAR_RATIO, 135*ANGLE_GEAR_RATIO),
                    DriveStraightAction(-30)
                ),
                DriveStraightAction(30)
            ))
class ThrowGuyMission(MissionBase):
    def routine(self):
        self.runAction(SpinMotor(1000*SPEED_GEAR_RATIO, -180*ANGLE_GEAR_RATIO))
def zero_pad(number, digits):
    number=str(number)
    return '0'*(digits-len(number))+number
def countdown(time, message=''):
    print(message)
    for i in range(time):
        print(zero_pad(time-i, len(str(time))), end='\r')
        hub.display.number(time-i)
        wait(1000)
    print('now')
    hub.display.off()
if __name__=='__main__':
    #MoveCamera().run()
    #print('Stop me')
    #while True:
    #    pass
    #1 north
    #15.75 east
    #attachment 90
    #facing north
    driveBase.settings(straight_speed=100, turn_rate=90)
    DriveStraightAction(550).run()
    DriveTurnAction(-10).run()
    GetToPink().run()
    DriveTurnAction(13).run()
    DriveStraightAction(-300).run()
    SpinMotor(200*SPEED_GEAR_RATIO, -135*ANGLE_GEAR_RATIO).run()
    DriveTurnAction(-90).run()
    DriveStraightAction(210).run()
    DriveTurnAction(90).run()
    DriveStraightAction(33).run()
    Dragon().run()
    DriveTurnAction(-45).run()
    Dragon().run()
    DriveTurnAction(-30).run()
    DriveStraightAction(-260).run()
    DriveTurnAction(95).run()
    DriveStraightAction(450).run()
    MoveCamera().run()