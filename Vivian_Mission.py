from PortMap import *
from BasicDriveActions import *
for i in range (4):
    DriveStraightAction(304.8).run()
    SpinMotor(500,90).run()
    DriveTurnAction(-100).run()
DriveStraightAction(152.4).run()
SpinMotor(100, 180).run()