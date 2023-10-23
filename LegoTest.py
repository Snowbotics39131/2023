from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch



hub = PrimeHub()
motorB = Motor(Port.B)
motorA = Motor(Port.A)
#motorA.reset_angle()
#motorB.reset_angle()
print('waiting to start')
hub.light.on(Color.BLUE) 
while True:
    target_angle = motorA.angle()
    
    if(abs(target_angle - motorB.angle()) > 1):
        motorB.track_target(target_angle)
    hub.display.number(target_angle/36)