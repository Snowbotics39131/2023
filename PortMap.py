#!/usr/bin/env pybricks-micropython
try:# all imports here
    from pybricks.hubs import *
    from pybricks.parameters import *
    try: from pybricks.pupdevices import *
    except: from pybricks.ev3devices import *
    from pybricks.robotics import *
    from pybricks.tools import *
except ImportError: print("Import error") #ModuleNotFoundError doesn't seem to work everywhere

try: from PortMapPlus import *
except ImportError: print("PortMapPlus Needed")

hubName = hubType()
def attachment_change():
    global motorBack
    global ultrasonicSensor
    global device
    try:
        motorBack=Motor(Port.D, Direction.COUNTERCLOCKWISE)
        print('motorBack detected')
    except:
        try:
            ultrasonicSensor=UltrasonicSensor(Port.D)
            print('ultrasonicSensor detected')
        except:
            print('Port D disconnected')
    device=Device()
if hubName == 'prime':
    #if you are using the spike this is all you need to mess with
    motorRight=Motor(Port.A, Direction.CLOCKWISE)
    motorLeft=Motor(Port.E, Direction.COUNTERCLOCKWISE)
    try: motorCenter=Motor(Port.C, Direction.CLOCKWISE)
    except: pass
    try:
        colorSensorLeft=ColorSensor(Port.F)
        colorSensorRight=ColorSensor(Port.B)
        attachment_change()
        driveBase=DriveBase(motorLeft, motorRight, 56, 114)
        try:
            driveBase.use_gyro(True)
        except NameError:
            try:
                GyroDriveBase
            except NameError:
                pass
            else:
                print('GyroDriveBase has been replaced by use_gyro. Update your firmware to the newest beta.')
            print('not using gyro')
        else:
            print('using gyro')
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
    try:
        motorLeft=Motor(Port.A)
        motorGear=Motor(Port.B)
        motorRight=Motor(Port.C)
        motorCross=Motor(Port.D)
        gyroSensor=GyroSensor(Port.S1)
        colorSensor=ColorSensor(Port.S4)
        colorSensorLeft=colorSensor #alias official names
        colorSensorRight=colorSensor
        driveBase=DriveBase(motorLeft, motorRight, 100, 130)
    except: print('Check Ports')
if hubName == 'technic':
    pass
if hubName == 'essential':
    pass

hub = hubDef()
device=Device()

#demo remove later
if __name__=='__main__':
    print(device.has_motorLeft)
    print(device.has_motorRight)
    print(device.has_colorSensorLeft)
    print(device.has_colorSensorRight)
    print(device.has_driveBase)
    print(device.has_ultrasonicSensor)
