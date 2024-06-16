from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

TEST='ABCDEF'

stopwatch=StopWatch()
end_times = {}
for i in TEST:
    motor = Motor(eval(f'Port.{i}'))
    times = []
    for _ in range(20):
        stopwatch.reset()
        motor.dc(100)
        angle = motor.angle()
        while angle < 360:
            angle = motor.angle()
        times.append(stopwatch.time())
        motor.brake()
        wait(300)
        motor.reset_angle()
    end_times[i] = times
means = {key: sum(value) / len(value) for key, value in end_times.items()}
def std_dev(thing):
    mean = sum(thing) / len(thing)
    return sum((mean - i)**2 for i in thing)**0.5
std_devs = {key: std_dev(value) for key, value in end_times.items()}
for i in means:
    print(f'{i} {means[i]} +- {std_devs[i]}')

'''motors = []
for i in TEST:
    motors.append(Motor(eval(f'Port.{i}')))
def do_thing_all_motors(thing):
    for i in range(len(motors)):
        exec(f'motors[{i}].{thing}')
do_thing_all_motors('dc(100)')
while True:
    pass
'''