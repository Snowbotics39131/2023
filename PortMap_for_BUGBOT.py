from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = PrimeHub()
motorLeft = Motor(Port.E,Direction.CLOCKWISE) 
motorRight = Motor(Port.A,Direction.COUNTERCLOCKWISE)
driveBase = DriveBase(motorLeft,motorRight,56*0.95,80) #56, 113
#colorSensorLeft=ColorSensor(Port.F)
#colorSensorRight=ColorSensor(Port.B)
motorCenter = Motor(Port.C,Direction.CLOCKWISE)
#backMediumMotor = Motor(Port.D,Direction.CLOCKWISE)\\\\\\\\\\\\\\\