from Actions import *
from AdvancedActions import *
from BasicDriveActions import *
from PortMap import *
#1 north
#13 west
#facing north
#TODO: make this alignment fully inside the home
DriveTurnAction(-45).run()
DriveStraightAction(250).run()
wait_for_button_press()
motorBack.run_time(-1100, 2000)