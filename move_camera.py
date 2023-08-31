#start in the red home
#3 squares north
#facing the track
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from PortMap import *
print(driveBase.settings())
class SpinMotorForever(Action):
    def __init__(self, speed):
        self.speed=speed
    def start(self):
        motorCenter.run(self.speed)
    def update(self):
        pass
    def done(self):
        pass
    def isFinished(self):
        return False
class ChangeTurnRateAction(Action):
    def __init__(self, turn_rate):
        self.turn_rate=turn_rate
    def start(self):
        driveBase.settings(turn_rate=self.turn_rate)
    def update(self):
        pass
    def done(self):
        pass
    def isFinished(self):
        return True
class MoveCamera(MissionBase):
    def routine(self):
        self.runAction(SeriesAction(
            ChangeTurnRateAction(90),
            SpinMotor(200, -90),
            DriveTurnAction(3.7),
            DriveStraightAction(450),
            SpinMotor(200, 90),
            ParallelAction(
                SpinMotorForever(30),
                SeriesAction(
                    DriveStraightAction(-30),
                    DriveTurnAction(-60)
                )
            )
        ))
if __name__=='__main__':
    move_camera=MoveCamera()
    move_camera.run()