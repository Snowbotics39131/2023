from Actions import *
from BasicDriveActions import *
from MissionBase import *
import autotime
class PushCamera(MissionBase):
    def routine(self):
        self.runAction(DriveStraightAction(267))
        self.runAction(SpinMotor(200, 540))
        self.runAction(DriveStraightAction(120, speed=400))
        self.runAction(DriveTurnAction(20))
        self.runAction(SpinMotor(500,-300))
        self.runAction(DriveTurnAction(-20))
        self.runAction(DriveStraightAction(-500))
if __name__=='__main__':
    autotime.checkpoint('before', True)
    PushCamera().run()
    autotime.checkpoint('after', True)
    autotime.print_all_deltas()