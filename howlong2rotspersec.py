from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

def std_dev(thing):
    mean = sum(thing) / len(thing)
    return sum((mean - i)**2 for i in thing)**0.5

TEST_MOTORS='ABCDEF'
TEST_COUNT = 30
DELAY_BETWEEN_TRIES = 500
MANUAL_SWITCH = True
print('Time - Lower is better')
stop_watch = StopWatch()
for i in TEST_MOTORS:
    motor = Motor(eval(f'Port.{i}'))
    times_pos = []
    times_neg = []
    posneg = 1
    for _ in range(TEST_COUNT):
        stop_watch.reset()
        motor.dc(100*posneg)
        while abs(motor.speed()) < 360 * 2:
            pass
        time = stop_watch.time()
        if posneg == 1:
            times_pos.append(time)
        else:
            times_neg.append(time)
        motor.brake()
        wait(DELAY_BETWEEN_TRIES)
        posneg *= -1
    mean_pos = sum(times_pos) / len(times_pos)
    std_dev_pos = std_dev(times_pos)
    mean_neg = sum(times_neg) / len(times_neg)
    std_dev_neg = std_dev(times_neg)
    print(f'{i} pos {mean_pos} +- {std_dev_pos} neg {mean_neg} +- {std_dev_neg}')
    if MANUAL_SWITCH:
        print('Move the wheel thing and press a button that\'s not stop', end='\r')
        if i != TEST_MOTORS[-1]:
            while not hub.buttons.pressed():
                pass
        print(' '*len('Move the wheel thing and press a button that\'s not stop'), end='\r')
