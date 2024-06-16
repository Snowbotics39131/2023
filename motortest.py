from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

port='Port.F'
motor=Motor(eval(port))
times=[]
angles=[]
stopwatch=StopWatch()
for i in range(20):
    stopwatch.reset()
    motor.dc(100)
    angle=motor.angle()
    while angle<360:
        angle=motor.angle()
    times.append(stopwatch.time())
    angles.append(angle)
    motor.brake()
    wait(500)
    motor.reset_angle()
print(port, times, 'times')
print(port, angles, 'angles')
average=sum(times)/20
stddev=sum(abs(average-i)**2 for i in times)**0.5
print(average, stddev)