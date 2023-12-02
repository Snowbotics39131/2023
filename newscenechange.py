from AdvancedActions import wait_for_button_press
from PortMap import *
driveBase.straight(570)
driveBase.turn(-45)
driveBase.straight(200)
driveBase.straight(-100)
driveBase.straight(-50)
driveBase.turn(20)
motorCenter.run_until_stalled(-100)
motorCenter.run_angle(100, 15)
driveBase.turn(25)
driveBase.straight(-300)