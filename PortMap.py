try:# all imports here
    from pybricks.hubs import *
    from pybricks.parameters import *
    from pybricks.pupdevices import *
    from pybricks.robotics import *
    from pybricks.tools import *
except Exception: print("Import error")

try: from PortMapPlus import *
except: print("PortMapPlus Needed")

hubName = hubType()
if hubName == 'prime':
    #if you are using the spike this is all you need to mess with
    motorRight=Motor(Port.A, Direction.CLOCKWISE)
    motorLeft=Motor(Port.E, Direction.COUNTERCLOCKWISE)
    try:
        colorSensorLeft=ColorSensor(Port.F)
        colorSensorLight=ColorSensor(Port.B)
        driveBase=DriveBase(motorLeft, motorRight, 56, 114)
        hubName += 'snow'
    except:
        driveBase=DriveBase(motorLeft, motorRight, 50, 50)
        hubName += 'bug'

# don't mess with the below unless you are not using the spike
if hubName == 'city':
    pass
if hubName == 'move':
    try:
        motorLeft=Motor(Port.B, Direction.COUNTERCLOCKWISE)
        motorRight=Motor(Port.A, Direction.CLOCKWISE)
        driveBase=DriveBase(motorLeft, motorRight, 50, 50)
    except: print("Check Motors")
if hubName == 'EV3':
    pass
if hubName == 'technic':
    pass
if hubName == 'essential':
    pass

hub = hubDef()
device = Device()

#demo remove later
'''
print(device.has_motorLeft)
print(device.has_motorRight)
print(device.has_colorSensorLeft)
print(device.has_colorSensorRight)
print(device.has_driveBase)
'''