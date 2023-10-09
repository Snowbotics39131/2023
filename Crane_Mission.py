from PortMap import *
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from Estimation import *


class CraneMission(MissionBase):
    def routine(self): 
        driveBase.settings(turn_rate=90),
        self.runAction(SeriesAction(
            DriveStraightAction(570),
            DriveTurnAction(-180),
            DriveStraightAction(615),
            DriveTurnAction(-180),
            DriveStraightAction(66),
            SpinMotor(180,1460),
            ParallelAction(
                SpinMotor(230,-1460),
                SeriesAction(
                DriveStraightAction(-66),
                DriveTurnAction(-180),
                DriveStraightAction(700))),
            SpinMotor(430,1230),
            DriveStraightAction(65),
            DriveTurnAction(-110),
            DriveStraightAction(20),
            DriveTurnAction(-90),
            DriveStraightAction(-180),
            DriveTurnAction(-95),
            DriveStraightAction(195),
            DriveStraightAction(110),
            DriveTurnAction(180),
            SpinMotor(430,-1230),
            DriveStraightAction(115),
            DriveTurnAction(-75)
            ))

if __name__ == "__main__": #run on file run but not import
    CraneMission()
    CraneMission = CraneMission()
    CraneMission.run()