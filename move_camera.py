#start in the red home
#3 squares north
#facing the track
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
        driveBase.settings(turn_rate=90)
        self.runAction(SeriesAction(
            SpinMotor(70, -90),
            #DriveTurnAction(3),
            DriveStraightAction(465),
            DriveTurnAction(12),
            SpinMotor(70, 90),
            ParallelAction(
                SpinMotorTime(30, 4000),
                #DriveTurnAction(-10),
                SeriesAction(
                    DriveStraightAction(-50),
                    DriveTurnAction(-70),
                    DriveStraightAction(-40)
                )
            ),
            SpinMotor(200, -180),
            DriveStraightAction(-200), #square
            DriveStraightAction(80),
            DriveTurnAction(90),
            DriveStraightAction(-400),
            SpinMotor(200, 180)
        ))
#start 12 squares north
#with attachment up
class Dragon(MissionBase):
    def routine(self):
        self.runAction(DriveTurnAction(30))
class GetToPink(MissionBase):
    def routine(self):
        for i in range(2):
            self.runAction(SeriesAction(
                SpinMotor(400, -90),
                DriveStraightAction(30),
                SpinMotorTime(400, 3000),
                DriveStraightAction(-30)
            ))
if __name__=='__main__':
    #move_camera=MoveCamera()
    #move_camera.run()
    #dragon=Dragon()
    #dragon.run()
    get_to_pink=GetToPink()
    while True:
        get_to_pink.run()