from AdvancedActions import wait_for_button_press
from BasicDriveActions import *
from MissionBase import *
from PortMap import *
class SceneChange(MissionBase):
    def __init__(self, changes=1):
        self.changes=changes
    def routine(self):
        self.runAction(DriveStraightAction(570))
        self.runAction(DriveTurnAction(-45))
        for i in range(self.changes):
            self.runAction(DriveStraightAction(200))
            self.runAction(DriveStraightAction(-100))
        self.runAction(DriveStraightAction(-50))
        self.runAction(DriveTurnAction(20))
        self.runAction(DriveStraightAction(-10))
        motorCenter.run_until_stalled(-150)
        self.runAction(DriveTurnAction(25))
        self.runAction(DriveStraightAction(-700))
        wait(25)
        hub.imu.reset_heading(0)
        self.runAction(DriveCurveAction(110, -135))
        motorCenter.run_until_stalled(22000)
        motorCenter.run_angle(-2000, 180)
        self.runAction(DriveStraightAction(-330))
        driveBase.settings(turn_rate=60)
        self.runAction(DriveTurnAction(45))
        driveBase.settings(turn_rate=180)
        self.runAction(DriveStraightAction(340))
        self.runAction(DriveTurnAction(90))
        self.runAction(DriveStraightAction(20))
        driveBase.use_gyro(False)
        self.runAction(DriveTurnAction(45))
        self.runAction(DriveTurnAction(-45))
        driveBase.use_gyro(True)
        self.runAction(DriveStraightAction(-300))
if __name__=='__main__':
    scene_change=SceneChange(1)
    scene_change.run()
