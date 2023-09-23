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

class MoveCamera(MissionBase):
    def routine(self):
        driveBase.settings(straight_speed=100, turn_rate=30)
        self.runAction(SeriesAction(
            SpinMotor(70*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO),
            DriveStraightAction(465),
            DriveTurnAction(13.5),
            SpinMotor(70*SPEED_GEAR_RATIO, 90*ANGLE_GEAR_RATIO),
            ParallelAction(
                SpinMotorTime(30*SPEED_GEAR_RATIO, 4000),
                SeriesAction(
                    DriveStraightAction(-50),
                    DriveTurnAction(-70),
                    DriveStraightAction(-40)
                )
            ),
            SpinMotor(200*SPEED_GEAR_RATIO, -180*ANGLE_GEAR_RATIO),
            DriveTurnAction(-30),
            #driveBase.settings(straight_speed=300, turn_rate=180)
            DriveStraightAction(-200), #square
            DriveStraightAction(80),
            DriveTurnAction(90),
            DriveStraightAction(-375),
            SpinMotor(200*SPEED_GEAR_RATIO, 180*ANGLE_GEAR_RATIO)
        ))
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
    #move_camera=MoveCamera()
    #move_camera.run()

    #dragon=Dragon()
    #dragon.run()

    #get_to_pink=GetToPink('orange')
    #while True:
    #    get_to_pink.run()
    #get_to_pink.run()

    #sound_mixer=SoundMixer()
    #sound_mixer.run()

    #chicken=Chicken()
    #chicken.run()
    
    #1 north
    #15.75 east
    #attachment 90
    #facing north
    driveBase.settings(straight_speed=100, turn_rate=90)
    #DriveStraightAction(170).run()
    #DriveTurnAction(-90).run()
    #SpinMotor(200*SPEED_GEAR_RATIO, 100*ANGLE_GEAR_RATIO).run()
    #SpinMotor(400*SPEED_GEAR_RATIO, -90*ANGLE_GEAR_RATIO).run()
    DriveStraightAction(553).run()
    DriveTurnAction(-10).run()
    #DriveStraightAction(3).run()
    #wait(3000)
    GetToPink().run()
    #while True:
    #    GetToPink().run()
    DriveTurnAction(13).run()
    DriveStraightAction(-300).run()
    SpinMotor(200*SPEED_GEAR_RATIO, -135*ANGLE_GEAR_RATIO).run()
    DriveTurnAction(-90).run()
    DriveStraightAction(210).run()
    DriveTurnAction(90).run()
    DriveStraightAction(27).run()
    Dragon().run()
    DriveTurnAction(-45).run()
    Dragon().run()
    DriveTurnAction(-30).run()
    DriveStraightAction(-50).run()
    DriveTurnAction(90).run()
    DriveStraightAction(300).run()
    DriveTurnAction(135).run()
    DriveStraightAction(70).run()
    SpinMotor(200*SPEED_GEAR_RATIO, -70*ANGLE_GEAR_RATIO).run()
    DriveStraightAction(-45).run()
    SoundMixer().run()
    driveBase.settings(straight_speed=500, turn_rate=360)
    DriveStraightAction(150).run()
    DriveTurnAction(-45).run()
    DriveStraightAction(800).run()
    SpinMotor(500*SPEED_GEAR_RATIO, 180*ANGLE_GEAR_RATIO).run()
    print('Prepare for camera mission and press left or right')
    while not hub.buttons.pressed():
        pass
    driveBase.settings(straight_speed=100, turn_rate=90)
    MoveCamera().run()