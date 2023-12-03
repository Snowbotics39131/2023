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
        driveBase.straight(-500)
        driveBase.turn(-135)
        driveBase.straight(50)
        motorCenter.run_until_stalled(2000)
        motorCenter.run_angle(2000, -180)
        driveBase.curve(-92, 90)
        driveBase.curve(-92, -90)
        driveBase.straight(-100)
        driveBase.turn(45)
        driveBase.straight(290)
        driveBase.turn(90)
        driveBase.straight(150)
        driveBase.turn(30)
        driveBase.turn(-30)
        driveBase.straight(-300)
if __name__=='__main__':
    scene_change=SceneChange(1)
    scene_change.run()