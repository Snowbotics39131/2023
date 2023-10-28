from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
motorB = Motor(Port.B)
ultrasonicSensor = UltrasonicSensor(Port.D)

print('waiting to start')
hub.light.on(Color.BLUE)
angle= 5
while True:
    dist1 = ultrasonicSensor.distance()
    if (dist1< 2000):
        ultrasonicSensor.lights.on(int((400-dist1)/4))
        print(100-int(dist1/400))
        print(dist1)
    motorB.run_angle(50,angle,then=Stop.COAST) 
    if ultrasonicSensor.distance()>=dist1:
        motorB.run_angle(50,-angle,then=Stop.COAST)

angleOClosest

def trackUltraClosest(angle)
    angle




