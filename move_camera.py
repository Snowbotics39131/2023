from MissionBase import *
from Actions import *
from BasicDriveActions import *
from PortMap import *
from Estimation import Pose
print(driveBase.settings())
print(hub.battery.voltage())
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
#red home
#4 squares north
#1 square east
#facing east
class MoveCamera(MissionBase):
    startPose=Pose(25, 100, 0)
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
    startPose=Pose(25, 325, -90)
    def routine(self):
        self.runAction(DriveTurnAction(30))
#near red home
#580mm north
#230mm east
#facing north
class GetToPink(MissionBase):
    startPose=Pose(230, 580, -90)
    def __init__(self, color='pink'):
        self.color=color
    def routine(self):
        if self.color=='blue':
            times=0
        elif self.color in ('orange', 'yellow'):
            times=1
        elif self.color=='pink':
            times=2
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
    seq_test=Sequence(GetToPink(), Dragon(), MoveCamera())
    seq_test.run()