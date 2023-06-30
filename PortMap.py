try:
    from pybricks.hubs import *
    from pybricks.parameters import *
    from pybricks.pupdevices import *
    from pybricks.robotics import *
    from pybricks.tools import *
except Exception:
    pass

def hubType():
    try:
        hub = CityHub()
        return 'city'
    except: pass
    try:
        hub = MoveHub()
        return 'move'
    except: pass
    try:
        hub = EV3Brick()
        return 'EV3'
    except: pass
    try:
        hub = TechnicHub()
        return 'technic'
    except: pass 
    try:
        hub = PrimeHub()
        return 'prime'
    except: pass
        try:
        hub = EssentialHub()
        return 'essential'
    except: pass
    return 'virtual'

hubName = hubType()

if hubName == 'city':
    pass
if hubName == 'move':
    motorLeft=Motor(Port.B, Direction.COUNTERCLOCKWISE)
    motorRight=Motor(Port.A, Direction.CLOCKWISE)
    drivebase=DriveBase(motorLeft, motorRight, 50, 50)
if hubName == 'EV3':
    pass
if hubName == 'technic':
    pass
if hubName == 'prime':
    motorRight=Motor(Port.A, Direction.CLOCKWISE)
    motorLeft=Motor(Port.E, Direction.COUNTERCLOCKWISE)
    try:
        drivebase=DriveBase(motorLeft, motorRight, 56, 114)
        colorSensorLeft=ColorSensor(Port.F)
        colorSensorLight=ColorSensor(Port.B)
        hubName += 'snow'
    except:
        drivebase=DriveBase(motorLeft, motorRight, 50, 50)
        hubName += 'bug'
if hubName == 'essential':
    pass