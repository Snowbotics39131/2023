from PortMap import *
startsettings=driveBase.settings()
print(driveBase.settings())
driveBase.settings(straight_speed=100, turn_rate=90)
print(driveBase.settings())
driveBase.settings(*startsettings)
print(driveBase.settings())