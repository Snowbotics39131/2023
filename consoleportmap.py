#For convenience, copy and paste this file into the console (accessed with the
#button to the right of stop) instead of copying certain lines from PortMap.py.
motorRight=Motor(Port.A, Direction.CLOCKWISE)
motorLeft=Motor(Port.E, Direction.COUNTERCLOCKWISE)
motorCenter=Motor(Port.C, Direction.CLOCKWISE)
colorSensorLeft=ColorSensor(Port.F)
colorSensorRight=ColorSensor(Port.B)
driveBase=DriveBase(motorLeft, motorRight, 56, 114)
driveBase.use_gyro(True)