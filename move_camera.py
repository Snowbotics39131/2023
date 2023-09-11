#red home
#4 squares north
#1 square east
#facing east
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from PortMap import *
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
class MoveCamera(MissionBase):
    def routine(self):
        driveBase.settings(straight_speed=100, turn_rate=30)
        self.runAction(SeriesAction(
            SpinMotor(70, -90),
            DriveStraightAction(465),
            DriveTurnAction(13.5),
            SpinMotor(70, 90),
            ParallelAction(
                SpinMotorTime(30, 4000),
                SeriesAction(
                    DriveStraightAction(-50),
                    DriveTurnAction(-70),
                    DriveStraightAction(-40)
                )
            ),
            SpinMotor(200, -180),
            DriveTurnAction(-30),
            DriveStraightAction(-200), #square
            DriveStraightAction(80),
            DriveTurnAction(90),
            DriveStraightAction(-375),
            SpinMotor(200, 180)
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
                SpinMotor(400, -90),
                DriveStraightAction(30),
                SpinMotorTime(400, 2000),
                DriveStraightAction(-30)
            ))
#start with blue piece on back up against sliders
class SoundMixer(MissionBase):
    def routine(self):
        driveBase.settings(turn_rate=90)
        self.runAction(SeriesAction(
            DriveStraightAction(-90),
            DriveTurnAction(45)
        ))
class Chicken(MissionBase):
    def routine(self):
        while True:
            self.runAction(SeriesAction(
                SpinMotor(200, -135),
                ParallelAction(
                    SpinMotor(200, 135),
                    DriveStraightAction(-30)
                ),
                DriveStraightAction(30)
            ))
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
    
    #4 north
    #0 east
    #facing east
    driveBase.settings(straight_speed=100, turn_rate=90)
    DriveStraightAction(170).run()
    DriveTurnAction(-90).run()
    DriveStraightAction(530).run()
    DriveTurnAction(-20).run()
    DriveStraightAction(5).run()
    GetToPink().run()
    DriveTurnAction(20).run()
    DriveStraightAction(-300).run()
    SpinMotor(200, -180).run()
    DriveTurnAction(-90).run()
    DriveStraightAction(230).run()
    DriveTurnAction(90).run()
    DriveStraightAction(15).run()
    Dragon().run()