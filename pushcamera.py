from Actions import *
from BasicDriveActions import *
from MissionBase import *
class PushCamera(MissionBase):
    def routine(self):
        self.runAction(DriveStraightAction(270))
        self.runAction(SpinMotor(200, 540))
        self.runAction(DriveStraightAction(120))
if __name__=='__main__':
    PushCamera().run()