from Actions import *
from BasicDriveActions import *
from PortMap import *
from MissionBase import *
driveBase.settings(straight_speed=100)
class ChangeSpeedAction(Action):
    def __init__(self, new_speed):
        self.new_speed=new_speed
    def start(self):
        driveBase.settings(straight_speed=self.new_speed)
    def update(self):
        pass
    def done(self):
        pass
    def isFinished(self):
        return True
class HookMission(MissionBase):
    def routine(self):
        self.runAction(SeriesAction(
            ChangeSpeedAction(195),
            DriveStraightAction(220),
            ChangeSpeedAction(100),
            DriveStraightAction(120),
            SpinMotor(500, -90),
            ParallelAction(
                SpinMotor(500, -360),
                DriveStraightAction(-120)
            ),
            SpinMotor(500, 450),
            ChangeSpeedAction(195),
            DriveStraightAction(-220),
            DriveTurnAction(-45),
            DriveStraightAction(-100),
            DriveTurnAction(90),
            DriveStraightAction(550),
            DriveStraightAction(-50),
            SpinMotor(500, -420),
            DriveStraightAction(-20),
            ParallelAction(
                SpinMotor(500, 400),
                DriveStraightAction(-120)
            ),
            #DriveTurnAction(10), 
            #DriveStraightAction(200),
            #DriveTurnAction(35),
        ))
#start this pointing towards the track in the home that says Masterpiece
#one unit from the corner
if __name__=='__main__':
    hook=HookMission()
    hook.run()
    #while True:
    #    test.run()
