from PortMap import *
driveBase.drive(200, 0)
while not hub.imu.stationary():
    pass
driveBase.stop()
hub.speaker.beep()