from PortMap import *
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from Estimation import *
from AdvancedActions import *
import autotime
#5 west
#2 north
#facing north
#blue home
#attachment down
#tray loaded
class CraneMission(MissionBase):
    def routine(self): 
        driveBase.settings(straight_speed=200, turn_rate=90),
        driveBase.use_gyro(False)
        self.runAction(SeriesAction(
            DriveStraightAction(440),
            DriveTurnAction(-43),
            DriveStraightAction(250),
            DriveTurnAction(-42),
            DriveStraightAction(630)))
        driveBase.settings(turn_rate=45)
        self.runAction(SeriesAction(
            DriveTurnAction(90),
            DriveStraightAction(170),
            DriveStraightAction(-50),
            SpinMotor(300, 145),
            DriveStraightAction(-80),
            DriveTurnAction(-170, disable_gyro=True)))
        driveBase.settings(turn_rate=135)
        driveBase.use_gyro(False)
        self.runAction(SeriesAction(
            DriveStraightAction(110),
            SpinMotor(360,1460),
            DriveStraightAccurate(-70),
            DriveTurnAction(-90),
            DriveStraightAction(-200),
            DriveTurnAction(90),
            DriveStraightAction(-70),
            DriveStraightAction(60),
            DriveTurnAction(-80, disable_gyro=True),
            DriveStraightAction(790),
            ParallelAction(
                DriveCurveAction(150, -45),
                SpinMotor(200, -270)
            ),
            DriveStraightAction(100),
            DriveTurnAction(-30),
            DriveTurnAction(30),
            DriveStraightAction(-100),
            #SpinMotor(200, -1440),
            #WaitForButtonPressAction(),
            #DriveStraightAction(90),
            #WaitForButtonPressAction(),
            #DriveTurnAction(-30),
            #WaitForButtonPressAction(),
            #SpinMotor(200, 30),
            #WaitForButtonPressAction(),
            #DriveTurnAction(-30)
            DriveTurnAction(-90),
            DriveStraightAction(-200),
            DriveTurnAction(45),
            DriveStraightAction(-700, disable_gyro=True)
            ))

if __name__ == "__main__": #run on file run but not import
    CraneMission()
    CraneMission = CraneMission()
    CraneMission.run()
