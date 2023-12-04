from AdvancedActions import wait_for_button_press
from MissionBase import *
from PortMap import *
class SceneChange(MissionBase):
    def __init__(self, changes=1):
        self.changes=changes
    def routine(self):
        driveBase.straight(570)
        driveBase.turn(-45)
        for i in range(self.changes):
            driveBase.straight(200)
            driveBase.straight(-100)
        driveBase.straight(-50)
        driveBase.turn(20)
        driveBase.straight(-10)
        motorCenter.run_until_stalled(-100)
        driveBase.turn(25)
        driveBase.straight(-600)
        driveBase.curve(120, -135)
        motorCenter.run_until_stalled(22000)
        motorCenter.run_angle(-2000, 180)
        driveBase.straight(-300)
        driveBase.turn(45)
if __name__=='__main__':
    scene_change=SceneChange(1)
    scene_change.run()