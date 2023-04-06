from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import umath


hub = PrimeHub()
motorRight = Motor(Port.A)
motorLeft = Motor(Port.E)

print('waiting to start')
hub.light.on(Color.BLUE)
angleBalanceMin=2
angleBalanceMax=6
autoBalanceMode = False

while True:
    angleX = hub.imu.tilt()[1]
    if (not autoBalanceMode and abs(angleX)>=angleBalanceMax):
        autoBalanceMode = True
    if (autoBalanceMode and abs(angleX)<=angleBalanceMin):
        autoBalanceMode = False
        motorLeft.run(0)
        motorRight.run(0)
    if (autoBalanceMode):
        hub.light.on(Color.RED)
        speed = umath.sin(umath.radians(angleX))
        motorLeft.run(speed*-1000)
        motorRight.run(speed*1000)
    if (not autoBalanceMode):
        hub.light.on(Color.GREEN)
        speed = 0