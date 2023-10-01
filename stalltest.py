from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

SPEED_GEAR_RATIO=-2
ANGLE_GEAR_RATIO=2
motor_c=Motor(Port.C)
for i in range(10, 101, 5):
    print(i)
    motor_c.run_until_stalled(400*SPEED_GEAR_RATIO, duty_limit=i)