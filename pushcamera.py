from Actions import *
from BasicDriveActions import *
from AdvancedActions import *
from MissionBase import *
import autotime
#1 north
#1 west
#facing west
#blue home
class PushCamera(MissionBase):
    def routine(self):
        #motorCenter.run_until_stalled(-400, duty_limit=70)
        self.runAction(ParallelAction(DriveStraightAction(267),SpinMotorUntilStalled(-600,duty_limit=70)))
        self.runAction(SpinMotor(600, 540))
        self.runAction(DriveStraightAction(120, speed=400))
        self.runAction(DriveTurnAction(20))
        self.runAction(ParallelAction(SpinMotor(600, -540),
                        SeriesAction(DriveTurnAction(-20),
                        DriveStraightAction(-500, speed=900))))
#1 north
#1 west
#facing north
#blue home
class CraftCreator(MissionBase):
    def routine(self):
        self.runAction(ParallelAction(
            DriveTurnAction(-45),
            SpinMotorUntilStalled(-400, duty_limit=70)
        ))
        self.runAction(DriveStraightAction(570))
        self.runAction(SpinMotor(400,450))
        self.runAction(ParallelAction(
            DriveStraightAction(-100),
            SpinMotor(400,270)
        ))
        self.runAction(ParallelAction(
            DriveStraightAction(-450),
            SpinMotorUntilStalled(-400, duty_limit=70)
        ))
        #motorCenter.run_until_stalled(-400, duty_limit=70)
        #driveBase.turn(-45)
        #driveBase.straight(600)
        #driveBase.straight(-30)
        #motorCenter.run_angle(400, 450)
        #driveBase.straight(-100)
        #motorCenter.run_angle(400, -270)
        #driveBase.straight(-50)
        #motorCenter.run_until_stalled(-400, duty_limit=70)
        #driveBase.straight(-400)
if __name__=='__main__':
    autotime.checkpoint('before', True)
    #PushCamera().run()
    CraftCreator().run()
    autotime.checkpoint('after', True)
    autotime.print_all_deltas()