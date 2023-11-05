from Actions import *
from AdvancedActions import *
from BasicDriveActions import *
from MissionBase import *
from PortMap import *
#1 north
#13 west
#facing north
#TODO: make this alignment fully inside the home
#DriveTurnAction(-45).run()
#DriveStraightAction(250).run()
#motorBack.run_time(-1100, 2000)

#1 north
#6 east
#facing north
class GoToBlueHomeScoopGuys(MissionBase):
    def routine(self):
        driveBase.straight(200)
        driveBase.turn(90)
        driveBase.straight(250)
        driveBase.turn(-45)
        driveBase.straight(150)
        driveBase.turn(45)
        driveBase.straight(200)
        driveBase.turn(30)
        driveBase.straight(100)
        driveBase.turn(-30)
        driveBase.straight(450)
        driveBase.turn(45)
        driveBase.straight(150)
        driveBase.turn(-45)
        driveBase.straight(100)
        driveBase.turn(-90)
        driveBase.straight(120)
        driveBase.turn(135)
        driveBase.straight(200)
class GoToBlueHomeGetIzzy(MissionBase):
    def routine(self):
        driveBase.straight(200)
        driveBase.turn(90)
        driveBase.straight(1125)
        driveBase.turn(-45)
        driveBase.straight(70)
        driveBase.turn(90)
        driveBase.straight(300)
        driveBase.turn(-45)
        driveBase.straight(200)
class GoToBlueHomeCurves(MissionBase):
    def routine(self):
        self.runAction(DriveCurveAction(180, 90))
        self.runAction(DriveStraightAction(40))
        self.runAction(DriveCurveAction(370, -45))
        self.runAction(DriveStraightAction(50))
        self.runAction(DriveCurveAction(130, 90))
        self.runAction(ParallelAction(
            DriveCurveAction(800, -45),
            SeriesAction(
                WaitAction(400),
                SpinMotorD(-90, 720)
            )
        ))
        self.runAction(DriveCurveAction(100, -45))
        self.runAction(DriveStraightAction(150))
        self.runAction(DriveTurnAction(45))
        self.runAction(DriveCurveAction(400, 45))
class Chicken(MissionBase):
    pass
if __name__=='__main__':
    GoToBlueHomeCurves().run()
    autotime.checkpoint('GoToBlueHome', True)