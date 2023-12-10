from AdvancedActions import wait_for_button_press
from MissionBase import *
from PortMap import *
class SceneChange(MissionBase):
    def __init__(self, changes=1):
        self.changes=changes
    def routine(self):
        settings=driveBase.settings()
        driveBase.settings(straight_speed=400)
        driveBase.straight(570)
        driveBase.settings(*settings)
        driveBase.turn(-45)
        for i in range(self.changes):
            driveBase.straight(200)
            driveBase.straight(-100)
        driveBase.straight(-50)
        driveBase.turn(20)
        driveBase.straight(-10)
        #motorCenter.run_until_stalled(-150)
        driveBase.turn(25)
        settings=driveBase.settings()
        driveBase.settings(straight_speed=900)
        driveBase.straight(-700)
        driveBase.settings(*settings)
        wait(500)
        hub.imu.reset_heading(0)
        driveBase.curve(100, -135)
        motorCenter.run_until_stalled(22000, duty_limit=50)
        motorCenter.run_angle(-2000, 180)
        driveBase.straight(-355)
        driveBase.settings(turn_rate=45)
        driveBase.turn(45)
        driveBase.settings(turn_rate=180)
        driveBase.straight(300)
        driveBase.turn(90)
        driveBase.straight(20)
        driveBase.use_gyro(False)
        driveBase.turn(45)
        driveBase.turn(-45)
        driveBase.use_gyro(True)
        driveBase.straight(-300)
if __name__=='__main__':
    scene_change=SceneChange(1)
    scene_change.run()