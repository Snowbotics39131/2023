#forklift attachment, all the way down, tray loaded
#1 north, 6 west, blue home
#facing north
from BasicDriveActions import *
from MissionBase import *
class PushTray(MissionBase):
    def routine(self):
        start_db_settings=driveBase.settings()
        self.runAction(DriveStraightAction(420, speed=max(driveBase.settings()[0], 200)))
        self.runAction(DriveTurnAction(-45))
        self.runAction(DriveStraightAction(250))
        self.runAction(DriveTurnAction(-45))
        self.runAction(DriveStraightAction(550))
        driveBase.settings(straight_speed=200, turn_rate=45)
        self.runAction(DriveTurnAction(90))
        self.runAction(DriveStraightAction(110))
        self.runAction(DriveStraightAction(-50))
        self.runAction(SpinMotor(300, 135))
        self.runAction(DriveStraightAction(-60))
        self.runAction(DriveTurnAction(-170))
        self.runAction(DriveStraightAction(110))
        self.runAction(SpinMotor(180,1460))
        driveBase.settings(*start_db_settings)
if __name__=='__main__':
    push_tray=PushTray()
    push_tray.run()