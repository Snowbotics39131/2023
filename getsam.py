from AdvancedActions import *
from PortMap import *
import autotime
driveBase.straight(550)
driveBase.turn(-15)
driveBase.straight(-20)
motorCenter.run_until_stalled(-100)
motorCenter.run(-10)
driveBase.straight(-30)
driveBase.turn(20)
driveBase.straight(-600)
driveBase.curve(57, -90, then=Stop.NONE)
driveBase.straight(100)
autotime.checkpoint('get sam', True)
autotime.print_all_deltas()