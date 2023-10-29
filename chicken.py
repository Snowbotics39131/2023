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
class GoToBlueHome(MissionBase):
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
class Chicken(MissionBase):
    pass
if __name__=='__main__':
    GoToBlueHome().run()