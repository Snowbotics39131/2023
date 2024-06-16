from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import umath

hub = InventorHub(top_side=-Axis.X,front_side=Axis.Z)
motorLeft = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
motorRight = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)


class BetterIMU:
    gyroAngle = 0
    accelAngle = 0
    filteredAngle = 0
    static = 0
    def get_acc_angle(self):
        accZ = hub.imu.acceleration(Axis.Z)
        accX = hub.imu.acceleration(Axis.X)
        self.accelAngle = -(umath.degrees(umath.atan2(accX,accZ))) - self.static

    def _init_(self):
        self.get_acc_angle()
        self.filtered_angle = self.accelAngle
        self.gyroAngle = 0
    timeConstant= 750


    def get_tilt():
        return hub.imu.tilt()[0]

    #complementary filter
    #The time constant of a filter is the relative duration of signal it will act on.
    #For a low-pass filter, signals much longer than the time constant pass through unaltered
    #while signals shorter than the time constant are filtered out. The opposite is true for a high-
    #pass filter. The time constant, τ, of a digital low-pass filter
    
    def filtered_Angle(self,accelAngle,gyroAngle,samplePeriod):
        gyroRate = hub.imu.angular_velocity(Axis.Y)
        gyroRate = gyroRate*samplePeriod/1000
        filterCoefficient = self.timeConstant/(self.timeConstant+samplePeriod)
        self.filteredAngle = filterCoefficient*(self.filteredAngle + gyroRate) + (1-filterCoefficient)*(accelAngle)


    def gyro_angle(self,samplePeriod):
        gyroRate = hub.imu.angular_velocity(Axis.Y)
        self.gyroAngle = self.gyroAngle + gyroRate*samplePeriod/1000

    def getAccelAngle(self):
        return self.accelAngle

    def getGyroAngle(self):
        return self.gyroAngle
     
    def getFilteredAngle(self):
        return self.filteredAngle
    
    def update(self,samplePeriod):
        self.get_acc_angle()
        self.filtered_Angle(self.accelAngle,self.gyroAngle,samplePeriod)
        
johhnathansIMU = BetterIMU()

kP = 5
kI = 1
kD = 3
lastTilt = 0
prevTime = 0
minThreshold = 0.4
tiltIntegral = 0
timer = StopWatch()
while True:
    wait(4)
    currentTime = timer.time()
    loopTime = currentTime - prevTime
    prevTime = currentTime
    johhnathansIMU.update(loopTime)
    #tilt = -((johhnathansIMU.getFilteredAngle() +3)/2)*abs((johhnathansIMU.getFilteredAngle() +3)/2)
    #tilt = -((johhnathansIMU.getFilteredAngle() +2.5))
    tilt = -((johhnathansIMU.getFilteredAngle() +3.55))
    print(tilt)
    tilt *= abs(tilt)
    #complementary filter
    #if (abs(tilt) < minThreshold): tiltIntegral = 0
    if tilt/abs(tilt+10**-15) != tiltIntegral/abs(tiltIntegral+10**-15):
        tiltIntegral = 0
    tiltIntegral += tilt
    dError = (lastTilt - tilt)/ loopTime
    lastTilt = tilt 
    correction = kP*tilt + kD*dError +kI*tiltIntegral
    #print(kP*tilt,kI*tiltIntegral,kD*dError)
    motorLeft.run(0.1*correction)
    motorRight.run(0.1*correction)
    

