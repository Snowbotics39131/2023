from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
motorLeft = Motor(Port.E,Direction.COUNTERCLOCKWISE) 
motorRight = Motor(Port.A,Direction.CLOCKWISE)
driveBase = DriveBase(motorLeft,motorRight,56,115)
try:
    colorSensorLeft=ColorSensor(Port.F)
    colorSensorRight=ColorSensor(Port.B)
    name = "Main"
except:
    name = "Bug"