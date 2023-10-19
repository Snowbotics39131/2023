from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

motorC=Motor(Port.C)
motorC.run(motorC.control.limits()[0])
while True:
    v=hub.battery.voltage()
    hub.display.number(v/100)