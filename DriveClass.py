from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
leftMotor=Motor(Port.A)
rightMotor=Motor(Port.B)

class Drive:
    def __init__:
        leftMotor=Motor(Port.A)
        rightMotor=Motor(Port.B)
    def moveStraight(distance,speed):
        while (movedDistance<distance):
            leftMotor.speed(speed)
            rightMotor.speed(speed)

         
    

    def turn():
