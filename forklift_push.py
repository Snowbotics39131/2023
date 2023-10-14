#forklift attachment, all the way down, tray loaded
#1 north, 6 west, blue home
#facing north
from BasicDriveActions import *
stopwatch=StopWatch()
start=stopwatch.time()
DriveStraightAction(400).run()
DriveTurnAction(-45).run()
DriveStraightAction(250).run()
DriveTurnAction(-45).run()
DriveStraightAction(540).run()
driveBase.settings(turn_rate=90)
DriveTurnAction(90).run()
#DriveStraightAction(70).run()
#DriveStraightAction(-70).run()
end=stopwatch.time()
print(end-start)