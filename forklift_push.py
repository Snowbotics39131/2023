#forklift attachment, all the way down, tray loaded
#1 north, 6 west, blue home
#facing north
from BasicDriveActions import *
from MissionBase import *
class PushTray(MissionBase):
    def routine(self):
        self.runAction(DriveStraightAction(400))
        self.runAction(DriveTurnAction(-45))
        self.runAction(DriveStraightAction(250))
        self.runAction(DriveTurnAction(-45))
        self.runAction(DriveStraightAction(540))
        driveBase.settings(turn_rate=90)
        self.runAction(DriveTurnAction(90))
if __name__=='__main__':
    push_tray=PushTray()
    push_tray.run()