#red home
#4 squares north
#1 square east
#facing east
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from PortMap import *
import autotime
SPEED_GEAR_RATIO=-2
ANGLE_GEAR_RATIO=2
TURN_FACTOR=1
STRAIGHT_FACTOR=1
WAIT=True
def wait_for_button_press(message=None, checkpoint_message=None):
    if message is not None:
        print(message)
    if WAIT:
        while not hub.buttons.pressed():
            pass
        autotime.checkpoint(f'wait_for_button_press({repr(message)})' if checkpoint_message is None else checkpoint_message, False)
print(driveBase.settings())
voltage=hub.battery.voltage()
print(voltage)
if voltage>=8000:
    print('Battery OK')
else:
    print('Battery low')
    wait_for_button_press('Press button to continue anyway')
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
#19 east
#1 north
class MoveCamera(MissionBase):
    def routine(self):
        #driveBase.settings(straight_speed=100, turn_rate=90)
        self.runAction(DriveStraightAccurate(-200*STRAIGHT_FACTOR)) #square
        self.runAction(DriveStraightAccurate(40*STRAIGHT_FACTOR))
        #self.runAction(SpinMotor(200*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO))
        self.runAction(DriveTurnAction(90*TURN_FACTOR))
        self.runAction(DriveStraightAccurate(20*STRAIGHT_FACTOR))
        self.runAction(DriveTurnAction(8.5*TURN_FACTOR))
        self.runAction(DriveStraightAccurate(23*STRAIGHT_FACTOR))
        self.runAction(SpinMotor(100*SPEED_GEAR_RATIO, 115*ANGLE_GEAR_RATIO))
        self.runAction(ParallelAction(
            SpinMotorTime(20*SPEED_GEAR_RATIO, 3000),
            SeriesAction(
                DriveStraightAccurate(-40*STRAIGHT_FACTOR),
                DriveTurnAction(-60*TURN_FACTOR)
            )
        ))
        self.runAction(DriveStraightAccurate(-15*STRAIGHT_FACTOR))
        self.runAction(SpinMotor(300*SPEED_GEAR_RATIO, -60*ANGLE_GEAR_RATIO))
        #wait_for_button_press()
#red home
#13 squares north
#1 square east
#facing north
#attachment up
class Dragon(MissionBase):
    def routine(self):
        self.runAction(DriveTurnAction(45*TURN_FACTOR))
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
                DriveStraightAccurate(30*STRAIGHT_FACTOR),
                #SpinMotorTime(400*SPEED_GEAR_RATIO, 2000),
                SpinMotorUntilStalled(400*SPEED_GEAR_RATIO),
                DriveStraightAccurate(-30*STRAIGHT_FACTOR)
            ))
#start with blue piece on back up against sliders
class SoundMixer(MissionBase):
    def routine(self):
        #SpinMotor(300*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO).run()
        SpinMotorUntilStalled(-300*SPEED_GEAR_RATIO).run()
        SpinMotor(300*SPEED_GEAR_RATIO, 105*ANGLE_GEAR_RATIO).run()
        #wait_for_button_press('Press button if back attachment fell')
        DriveStraightAction(-100*STRAIGHT_FACTOR).run()
        driveBase.settings(turn_rate=90)
        self.runAction(SeriesAction(
            DriveStraightAccurate(-90*STRAIGHT_FACTOR),
            DriveTurnAction(90*TURN_FACTOR)
        ))
class Chicken(MissionBase):
    def routine(self):
        while True:
            self.runAction(SeriesAction(
                SpinMotor(200*SPEED_GEAR_RATIO, -135*ANGLE_GEAR_RATIO),
                ParallelAction(
                    SpinMotor(200*SPEED_GEAR_RATIO, 135*ANGLE_GEAR_RATIO),
                    DriveStraightAccurate(-30*STRAIGHT_FACTOR)
                ),
                DriveStraightAccurate(30*STRAIGHT_FACTOR)
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
    #1 north
    #16 east
    #attachment 90
    #facing north
    driveBase.settings(straight_speed=100, turn_rate=180)
    DriveStraightAccurate(565*STRAIGHT_FACTOR).run()
    DriveTurnAction(-10*TURN_FACTOR).run()
    autotime.checkpoint('Travel to GetToPink', True)
    GetToPink().run()
    autotime.checkpoint('GetToPink', True)
    DriveTurnAction(13*TURN_FACTOR).run()
    DriveStraightAccurate(-300*STRAIGHT_FACTOR).run()
    SpinMotor(200*SPEED_GEAR_RATIO, -135*ANGLE_GEAR_RATIO).run()
    DriveTurnAction(-90*TURN_FACTOR).run()
    DriveStraightAccurate(240*STRAIGHT_FACTOR).run()
    DriveTurnAction(90*TURN_FACTOR).run()
    DriveStraightAccurate(20*STRAIGHT_FACTOR).run()
    autotime.checkpoint('Travel to Dragon', True)
    Dragon().run()
    DriveTurnAction(-45*TURN_FACTOR).run()
    Dragon().run()
    DriveTurnAction(-45*TURN_FACTOR).run()
    Dragon().run()
    autotime.checkpoint('Dragon', True)
    DriveTurnAction(-30*TURN_FACTOR).run()
    DriveStraightAction(-400*STRAIGHT_FACTOR).run()
    DriveStraightAccurate(70*STRAIGHT_FACTOR).run()
    DriveTurnAction(90*TURN_FACTOR).run()
    DriveStraightAccurate(450*STRAIGHT_FACTOR).run()
    DriveTurnAction(-90*TURN_FACTOR).run()
    #SpinMotor(300*SPEED_GEAR_RATIO, 100*ANGLE_GEAR_RATIO).run()
    autotime.checkpoint('Travel to MoveCamera', True)
    wait_for_button_press('Starting MoveCamera on button press')
    MoveCamera().run()
    autotime.checkpoint('MoveCamera', True)
    DriveTurnAction(55*TURN_FACTOR).run()
    DriveStraightAccurate(-180).run()
    print("The corner of the robot should be on the 'Lego Education' insignia.")
    wait_for_button_press('Starting SoundMixer on button press')
    DriveStraightAccurate(-200*STRAIGHT_FACTOR).run()
    SpinMotor(300*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO).run()
    DriveTurnAction(135*TURN_FACTOR).run()
    DriveStraightAccurate(-200*STRAIGHT_FACTOR).run()
    autotime.checkpoint('Travel to SoundMixer', True)
    SoundMixer().run()
    autotime.checkpoint('SoundMixer', True)
    autotime.print_all_deltas()
