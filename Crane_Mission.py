from PortMap import *
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from Estimation import *
from AdvancedActions import *
from ControlActions import *
import autotime
#5 west
#2 north
#facing north
#blue home
#attachment down
#tray loaded
class CraneMission(MissionBase):
    def routine(self): 
        driveBase.settings(straight_speed=300, turn_rate=90),
        self.runAction(SeriesAction(
            SpinMotorUntilStalled(-200),
            SpinMotor(200, 90),
            DriveStraightAction(430),
            DriveTurnAction(-45),
            DriveStraightAction(250),
            DriveTurnAction(-45),
            #DriveCurveAction(1/2**0.5*250, -90),
            DriveStraightAction(630),
            FunctionAction(lambda x: exec(f'global prev_turn_rate; prev_turn_rate={x}'), driveBase.settings()[2]),
            FunctionAction(driveBase.settings, turn_rate=45),
            DriveTurnAction(90),
            FunctionAction(lambda gf: driveBase.settings(turn_rate=gf()), lambda: prev_turn_rate),
            DriveStraightAction(200, speed=150),
            FunctionAction(driveBase.reset),
            DriveStraightAction(-50),
            SpinMotor(300, 145),
            DriveStraightAction(-80),
            DriveTurnAction(-180),
            DriveStraightAction(130),
            #SpinMotor(360, 1460),
            SpinMotor(500, 1380),
            ParallelAction(
                DriveStraightAccurate(-75),
                SpinMotor(500, -70)),
            DriveTurnAction(-97),
            DriveStraightAction(-200),
            DriveTurnAction(97),
            DriveStraightAction(-83),
            DriveStraightAction(60, speed=300),
            ParallelAction(
                DriveTurnAction(-90),
                SpinMotor(900, -200)
            ),
            ParallelAction(
                DriveStraightAction(360),
                SpinMotorUntilStalled(-1000),
                ),
            DriveTurnAction(-65),
            DriveStraightAction(105),
            DriveTurnAction(20),
            DriveStraightAction(-40),
            DriveTurnAction(20),
            DriveStraightAction(-15),
            DriveTurnAction(25),
            ParallelAction(
                DriveStraightAction(470),
                SpinMotor(1000, 1600),
            ),
            FunctionAction(driveBase.settings, straight_speed=150),
            ParallelAction(
                DriveCurveAction(150, -45),
                SpinMotor(200, -180)
            ),
            DriveStraightAction(135),
            DriveTurnAction(-20),
            DriveTurnAction(35),
            DriveStraightAction(-100),
            ParallelAction( 
                DriveTurnAction(-90),
                SpinMotor(900, -300)
            ),
            ParallelAction( 
                DriveStraightAction(70),
                SpinMotorUntilStalled(-1000),
                SpinMotor(200, 40)
            ),
            DriveTurnAction(80),
            DriveStraightAction(55),
            DriveTurnAction(-100),
            DriveCurveAction(-150, -45),
            DriveStraightAction(-700, speed=500),
            ))

if __name__ == "__main__": #run on file run but not import
    CraneMission()
    CraneMission = CraneMission()
    CraneMission.run()
