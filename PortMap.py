from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
#print('PortMap.py running')
hub = PrimeHub()
MotorLeft = Motor(Port.E,Direction.COUNTERCLOCKWISE) 
MotorRight = Motor(Port.A,Direction.CLOCKWISE)
driveBase = DriveBase(MotorLeft,MotorRight,56,115)
colorSensorLeft= ColorSensor(Port.F)
colorSensorRight= ColorSensor(Port.B)










 






