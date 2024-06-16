from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

TEST_MOTORS = 'ABCDEF'
TEST_TIME = 1000
TEST_COUNT = 10
DELAY_BETWEEN_TRIES=500
millis = len(TEST_MOTORS) * (TEST_TIME + DELAY_BETWEEN_TRIES) * TEST_COUNT
seconds = millis / 1000
minutes = int(seconds / 60)
seconds = int(seconds % 60)
print(f'Estimated time {minutes}m{seconds}s')
def std_dev(thing):
    mean = sum(thing) / len(thing)
    return sum((mean - i)**2 for i in thing)**0.5
end_times = {}
for i in TEST_MOTORS:
    motor = Motor(eval(f'Port.{i}'))
    angles_pos = []
    angles_neg = []
    posneg = 1
    for _ in range(TEST_COUNT):
        motor.reset_angle()
        motor.dc(100*posneg)
        wait(TEST_TIME)
        if posneg == 1:
            angles_pos.append(motor.angle())
        else:
            angles_neg.append(motor.angle())
        motor.brake()
        wait(DELAY_BETWEEN_TRIES)
        posneg *= -1
    #print(angles_pos)
    #print(angles_neg)
    mean_pos = sum(angles_pos) / len(angles_pos)
    std_dev_pos = std_dev(angles_pos)
    mean_neg = sum(angles_neg) / len(angles_neg)
    std_dev_neg = std_dev(angles_neg)
    print(f'{i} pos {mean_pos} +- {std_dev_pos} neg {mean_neg} +- {std_dev_neg}')
    print('Move the wheel thing and press a button that\'s not stop', end='\r')
    if i != TEST_MOTORS[-1]:
        while not hub.buttons.pressed():
            pass
    print(' '*len('Move the wheel thing and press a button that\'s not stop'), end='\r')