from PortMap import *
distance=100
def spiral():
    while True:
        driveBase.straight(distance)
        driveBase.turn(90)
        distance+=100
#spiral()
#while True:
#    driveBase.turn(90)
#    wait(1000)
#    driveBase.turn(-90)
#    wait(1000)
def follow(driveBase, sensor):
    reflection=sensor.reflection()-50
    while True:
        if sensor.reflection()<0:
            driveBase.turn(1)
        elif sensor.reflection()>0:
            driveBase.turn(-1)
        else:
            pass
        driveBase.straight(10)
follow(driveBase, colorSensorLeft)
#driveBase.straight(500)
#MotorLeft.run_angle(250, 360*5, wait=False)
#MotorRight.run_angle(250, 360*5)
