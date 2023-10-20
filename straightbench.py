from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import GyroDriveBase, DriveBase

hub = PrimeHub()

WAIT=True
def wait_for_button_press(message=None, checkpoint_message=None):
    if message is not None:
        print(message)
    hub.speaker.beep()
    if WAIT:
        while not hub.buttons.pressed():
            pass
        #autotime.checkpoint(f'wait_for_button_press({repr(message)})' if checkpoint_message is None else checkpoint_message, False)

motorRight=Motor(Port.A, Direction.CLOCKWISE)
motorLeft=Motor(Port.E, Direction.COUNTERCLOCKWISE)
driveBase=GyroDriveBase(motorLeft, motorRight, 56, 114)
output=[]
for i in range(32):
    driveBase.reset()
    hub.imu.reset_heading(0)
    driveBase.straight(500)
    output.append((hub.imu.heading(), driveBase.distance()))
    driveBase.straight(-500)
print(output)