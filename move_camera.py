#red home
#4 squares north
#1 square east
#facing east
from MissionBase import *
from Actions import *
from AdvancedActions import *
from BasicDriveActions import *
from PortMap import *
from forklift_push import *
from Crane_Mission import *
import autotime
SPEED_GEAR_RATIO=-2
ANGLE_GEAR_RATIO=2
TURN_FACTOR=1
STRAIGHT_FACTOR=1
COMPENSATE=False
ACCURATE_SPEED=150
TRAVEL_SPEED=300
FAST_SPEED=600
#19 east
#1 north
class MoveCamera(MissionBase):
    def routine(self):
        #FIXME: 7-degree angle is too much
        self.runAction(DriveStraightAccurate(20*STRAIGHT_FACTOR, speed=ACCURATE_SPEED, compensate=COMPENSATE))
        self.runAction(DriveTurnAction(7*TURN_FACTOR))
        self.runAction(DriveStraightAccurate(23*STRAIGHT_FACTOR, speed=ACCURATE_SPEED, compensate=COMPENSATE))
        self.runAction(SpinMotor(100*SPEED_GEAR_RATIO, 115*ANGLE_GEAR_RATIO))
        self.runAction(ParallelAction(
            SpinMotorTime(20*SPEED_GEAR_RATIO, 3000),
            SeriesAction(
                DriveStraightAccurate(-120*STRAIGHT_FACTOR, speed=ACCURATE_SPEED, compensate=COMPENSATE),
                DriveTurnAction(-55*TURN_FACTOR)
            )
        ))
        #self.runAction(DriveStraightAccurate(-30*STRAIGHT_FACTOR, speed=ACCURATE_SPEED, compensate=COMPENSATE))
        self.runAction(SpinMotor(300*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO))
#red home
#13 squares north
#1 square east
#facing north
#attachment up
class Dragon(MissionBase):
    def __init__(self, tries=2):
        self.tries=tries
    def routine(self):
        self.runAction(DriveTurnAction(30*TURN_FACTOR))
        for i in range(self.tries-1):
            self.runAction(DriveTurnAction(-30*TURN_FACTOR))
            self.runAction(DriveTurnAction(30*TURN_FACTOR))
#near red home
#580mm north
#230mm east
#facing north
class GetToPink(MissionBase):
    def __init__(self, color='pink'):
        """color not currently used"""
        self.color=color
    def routine(self):
        if self.color=='blue':
            times=3 #need to get the flag down
        elif self.color in ('orange', 'yellow'):
            times=2
        elif self.color=='pink':
            times=1
        else:
            raise ValueError(f'Invalid color: {self.color}')
        self.runAction(DriveTurnAction(-20))
        self.runAction(DriveStraightAccurate(20, speed=ACCURATE_SPEED, weights=[0, 0, 2, 1], compensate=True, verbose=True))
        self.runAction(SpinMotorAngleOrUntilStalled(150*SPEED_GEAR_RATIO, 135*ANGLE_GEAR_RATIO))
        self.runAction(SpinMotor(300*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO))
        self.runAction(DriveStraightAccurate(-35, speed=ACCURATE_SPEED, weights=[0, 0, 2, 1], compensate=True, verbose=True))
        #If the guy didn't land in the zone, the corner of the robot can nudge it slightly forward.
        self.runAction(DriveStraightAccurate(60, speed=ACCURATE_SPEED, weights=[0, 0, 2, 1], compensate=True, verbose=True))
        self.runAction(DriveStraightAccurate(-60, speed=ACCURATE_SPEED, weights=[0, 0, 2, 1], compensate=True, verbose=True))
        self.runAction(DriveTurnAction(20))
        DriveStraightAccurate(20, speed=ACCURATE_SPEED, weights=[0, 0, 2, 1], compensate=True, verbose=True).run()
        self.runAction(SeriesAction(
            #SpinMotor(400*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO),
            DriveStraightAccurate(30*STRAIGHT_FACTOR, speed=ACCURATE_SPEED, compensate=COMPENSATE),
            #DriveTurnAction(-20),
            #DriveTurnAction(20),
            SpinMotorUntilStalled(400*SPEED_GEAR_RATIO, duty_limit=85),
            #SpinMotorAngleOrUntilStalled(400*SPEED_GEAR_RATIO, 135),
            DriveStraightAccurate(-30*STRAIGHT_FACTOR, speed=ACCURATE_SPEED, compensate=COMPENSATE)
        ))
        DriveTurnAction(13*TURN_FACTOR).run()
        self.runAction(DriveStraightAccurate(-20, speed=ACCURATE_SPEED, weights=[0, 0, 2, 1], compensate=True, verbose=True))
        self.runAction(DriveTurnAction(35))
        self.runAction(DriveStraightAccurate(80, speed=ACCURATE_SPEED, weights=[0, 0, 2, 1], compensate=True, verbose=True))
        self.runAction(DriveTurnAction(15))
        SpinMotor(300*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO).run()
        SpinMotor(-motorCenter.control.limits()[0], 90*ANGLE_GEAR_RATIO).run()
        self.runAction(DriveTurnAction(-15))
        self.runAction(DriveStraightAccurate(-80, speed=ACCURATE_SPEED, weights=[0, 0, 2, 1], compensate=True))
        self.runAction(DriveTurnAction(-35))
        #self.runAction(DriveStraightAccurate(20, speed=ACCURATE_SPEED, weights=[0, 0, 2, 1], compensate=True))
#start with blue piece on back up against sliders
class SoundMixer(MissionBase):
    def routine(self):
        #FIXME: went to the right
        start_db_settings=driveBase.settings()
        DriveTurnAction(-50).run()
        SpinMotorUntilStalled(-300*SPEED_GEAR_RATIO).run()
        DriveTurnAction(45).run()
        SpinMotor(300*SPEED_GEAR_RATIO, 105*ANGLE_GEAR_RATIO).run()
        DriveStraightAction(-120*STRAIGHT_FACTOR, speed=ACCURATE_SPEED).run()
        driveBase.settings(turn_rate=90)
        self.runAction(SeriesAction(
            DriveStraightAccurate(-90*STRAIGHT_FACTOR, speed=TRAVEL_SPEED, compensate=COMPENSATE),
            DriveTurnAction(90*TURN_FACTOR)
        ))
        driveBase.settings(*start_db_settings)
class Chicken(MissionBase):
    def routine(self):
        while True:
            self.runAction(SeriesAction(
                SpinMotor(200*SPEED_GEAR_RATIO, -135*ANGLE_GEAR_RATIO),
                ParallelAction(
                    SpinMotor(200*SPEED_GEAR_RATIO, 135*ANGLE_GEAR_RATIO),
                    DriveStraightAccurate(-30*STRAIGHT_FACTOR, compensate=COMPENSATE)
                ),
                DriveStraightAccurate(30*STRAIGHT_FACTOR, speed=ACCURATE_SPEED, compensate=COMPENSATE)
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
class CombinedMission1(MissionBase):
    def __init__(self, push=True):
        self.push=push
    def routine(self):
        #1 north
        #16 east
        #attachment 90
        #facing north
        driveBase.settings(turn_rate=180)
        DriveStraightAccurate(558*STRAIGHT_FACTOR, speed=TRAVEL_SPEED, compensate=COMPENSATE).run()
        DriveTurnAction(-8*TURN_FACTOR).run()
        autotime.checkpoint('Travel to GetToPink', True)
        GetToPink().run()
        autotime.checkpoint('GetToPink', True)
        DriveStraightAccurate(-300*STRAIGHT_FACTOR, speed=TRAVEL_SPEED, compensate=COMPENSATE).run()
        SpinMotor(200*SPEED_GEAR_RATIO, -135*ANGLE_GEAR_RATIO).run()
        DriveTurnAction(-90*TURN_FACTOR).run()
        DriveStraightAccurate(240*STRAIGHT_FACTOR, speed=TRAVEL_SPEED, compensate=COMPENSATE).run()
        DriveTurnAction(90*TURN_FACTOR).run()
        DriveStraightAccurate(60*STRAIGHT_FACTOR, speed=ACCURATE_SPEED, compensate=COMPENSATE).run()
        autotime.checkpoint('Travel to Dragon', True)
        Dragon().run()
        autotime.checkpoint('Dragon', True)
        DriveTurnAction(-30*TURN_FACTOR).run()
        DriveStraightAction(-400*STRAIGHT_FACTOR, speed=FAST_SPEED, stop=True).run()
        #DriveStraightAccurate(70*STRAIGHT_FACTOR, speed=TRAVEL_SPEED, compensate=COMPENSATE).run()
        #DriveTurnAction(90*TURN_FACTOR).run()
        #DriveStraightAccurate(150*STRAIGHT_FACTOR, speed=TRAVEL_SPEED, compensate=COMPENSATE).run()
        autotime.checkpoint('Travel to MoveCamera alignment', True)
        print('The back edge of the robot should be on the right edge of the C.')
        print('The right edge should be 2 units south of the edge of the red.')
        wait_for_button_press(checkpoint_message='Align for MoveCamera')
        DriveStraightAccurate(340*STRAIGHT_FACTOR, speed=TRAVEL_SPEED, compensate=COMPENSATE).run()
        #DriveTurnAction(-90*TURN_FACTOR).run()
        #SpinMotor(300*SPEED_GEAR_RATIO, 100*ANGLE_GEAR_RATIO).run()
        autotime.checkpoint('Travel to MoveCamera', True)
        #wait_for_button_press('Starting MoveCamera on button press')
        MoveCamera().run()
        autotime.checkpoint('MoveCamera', True)
        DriveTurnAction(30*TURN_FACTOR).run()
        #stop does not work on DriveStraightAccurate
        #DriveStraightAccurate(-340*STRAIGHT_FACTOR, speed=FAST_SPEED, compensate=COMPENSATE, stop=True).run()
        DriveStraightAction(-340*STRAIGHT_FACTOR, speed=FAST_SPEED, stop=True).run()
        SpinMotor(400*SPEED_GEAR_RATIO, -45*ANGLE_GEAR_RATIO).run()
        autotime.checkpoint('Travel to SoundMixer alignment', True)
        print("The corner of the robot should be on the dot of the i in of 'Foundation'.")
        wait_for_button_press('Starting SoundMixer on button press')
        DriveStraightAccurate(-90*STRAIGHT_FACTOR, speed=TRAVEL_SPEED, compensate=COMPENSATE).run()
        DriveTurnAction(135*TURN_FACTOR).run()
        DriveStraightAccurate(-170*STRAIGHT_FACTOR, speed=TRAVEL_SPEED, compensate=COMPENSATE).run()
        autotime.checkpoint('Travel to SoundMixer', True)
        SoundMixer().run()
        autotime.checkpoint('SoundMixer', True)
        DriveTurnAction(90).run()
        DriveStraightAction(-300, speed=FAST_SPEED, stop=True).run()
        autotime.checkpoint('Return to home for alignment', True)
        wait_for_button_press('Remove attachment and prepare to travel to blue home')
        #faster than usual travel, but not like you're rushing back to align
        DriveStraightAction(220, speed=(TRAVEL_SPEED+FAST_SPEED)/2).run()
        DriveTurnAction(90).run()
        DriveStraightAction(500).run()
        DriveTurnAction(45).run()
        DriveStraightAction(160).run()
        DriveTurnAction(-45).run()
        DriveStraightAction(700).run()
        DriveTurnAction(45).run()
        DriveStraightAction(250).run()
        autotime.checkpoint('Travel to blue home', True)
        autotime.print_all_deltas()
class CombinedMission2(MissionBase):
    def routine(self):
        wait_for_button_press('Prepare to push tray with forklift')
        #PushTray().run()
        CraneMission().run()
        autotime.checkpoint('PushTray', True)
        print('not running PushTray')
        
if __name__=='__main__':
    voltage=hub.battery.voltage()
    print(voltage)
    if voltage>=8000:
        print('Battery OK')
    else:
        print('Battery low')
        wait_for_button_press('Press button to continue anyway')
    CombinedMission1().run()
    CombinedMission2().run()