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
        driveBase.settings(turn_rate=90),
        self.runAction(SeriesAction(
            DriveStraightAction(415),
            DriveTurnAction(-45),
            DriveStraightAction(250),
            DriveTurnAction(-45),
            DriveStraightAction(630)))
        driveBase.settings(turn_rate=45)
        self.runAction(SeriesAction(
            DriveTurnAction(90),
            DriveStraightAction(170),
            DriveStraightAction(-50),
            SpinMotor(300, 145),
            DriveStraightAction(-80),
            DriveTurnAction(-180),
            DriveStraightAction(110),
            SpinMotor(180,1460),
            DriveStraightAccurate(-70),
            DriveTurnAction(-90),
            DriveStraightAction(-200),
            DriveTurnAction(90),
            DriveStraightAction(-70),
            DriveStraightAction(50),
            DriveTurnAction(-90),
            DriveStraightAction(790),
            ParallelAction(
                DriveCurveAction(200, -45),
                SpinMotor(200, -270)
            ),
            DriveStraightAction(10),
            DriveTurnAction(-20),
            DriveTurnAction(20),
            DriveStraightAction(-10)
            ))

if __name__ == "__main__": #run on file run but not import
    CraneMission()
    CraneMission = CraneMission()
    CraneMission.run()
