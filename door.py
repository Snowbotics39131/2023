from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()


doormotor = Motor (Port.C)
sensor = UltrasonicSensor (Port.A)
while True:
    if sensor.distance() < 100:
        doormotor.run_angle (speed=100, rotation_angle=-90)
        hub.display.text("Access granted")
        wait (time=3000)
        doormotor.run_angle (speed=100, rotation_angle=90)

