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
        driveBase.straight(-15)
        motorCenter.run_until_stalled(-100)
        driveBase.turn(25)
        driveBase.straight(-700)
        wait(10)
        hub.imu.reset_heading(0)
        driveBase.curve(140, -135)
        motorCenter.run_until_stalled(22000)
        motorCenter.run_angle(-2000, 180)
        driveBase.straight(-380)
        driveBase.turn(45)
        driveBase.straight(350)
        driveBase.turn(90)
        driveBase.straight(30)
        driveBase.use_gyro(False)
        driveBase.turn(45)
        driveBase.turn(-45)
        driveBase.use_gyro(True)
        driveBase.straight(-300)
if __name__=='__main__':
    scene_change=SceneChange(1)
    scene_change.run()