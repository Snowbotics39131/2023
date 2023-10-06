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
##63mm north 2.5 squares
##415mm east
#19 east <-- this, not mm measurements
#1 north
class MoveCamera(MissionBase):
    def routine(self):
        driveBase.settings(straight_speed=100, turn_rate=90)
        self.runAction(DriveStraightAction(-100))
        self.runAction(DriveStraightAction(40))
        self.runAction(SpinMotor(200*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO))
        self.runAction(DriveTurnAction(90))
        self.runAction(DriveStraightAction(30))
        self.runAction(DriveTurnAction(2))
        self.runAction(DriveStraightAction(20))
        self.runAction(SpinMotor(300*SPEED_GEAR_RATIO, 110*ANGLE_GEAR_RATIO))
        self.runAction(ParallelAction(
            SpinMotorTime(20*SPEED_GEAR_RATIO, 4000),
            SeriesAction(
                DriveStraightAction(-60),
                DriveTurnAction(-70)
            )
        ))
        self.runAction(SpinMotor(300*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO))
        self.runAction(DriveTurnAction(45))
        self.runAction(DriveStraightAction(-450))
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
wait=True
def waitForButtonPressWithMessage(message):
    print(message)
    if wait:
        while not hub.buttons.pressed():
            pass
if __name__=='__main__':
    #1 north
    #16 east
    #attachment 90
    #facing north
    driveBase.settings(straight_speed=100, turn_rate=90)
    DriveStraightAction(553).run()
    DriveTurnAction(-10).run()
    GetToPink().run()
    DriveTurnAction(13).run()
    DriveStraightAction(-300).run()
    SpinMotor(200*SPEED_GEAR_RATIO, -135*ANGLE_GEAR_RATIO).run()
    DriveTurnAction(-90).run()
    DriveStraightAction(210).run()
    DriveTurnAction(90).run()
    DriveStraightAction(40).run()
    Dragon().run()
    DriveTurnAction(-45).run()
    Dragon().run()
    DriveTurnAction(-30).run()
    DriveStraightAction(-400).run()
    DriveStraightAction(70).run()
    DriveTurnAction(90).run()
    DriveStraightAction(455).run() #TODO: make this check brightness change from
    DriveTurnAction(-90).run()     #white to light blue instead of fixed value
    SpinMotor(300*SPEED_GEAR_RATIO, 100*ANGLE_GEAR_RATIO).run()
    #waitForButtonPressWithMessage('Starting MoveCamera on button press')
    MoveCamera().run()