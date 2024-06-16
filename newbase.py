from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

motorLeft=Motor(Port.F, Direction.COUNTERCLOCKWISE)
motorRight=Motor(Port.A)
driveBase=DriveBase(motorLeft, motorRight, 56, 113)
driveBase.use_gyro(True)

driveBase.straight(1000)
#motorLeft.dc(25)
#motorRight.dc(33)
#while True:
#    pass