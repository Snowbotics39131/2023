from PortMap import *
import umath

timer = StopWatch()
timeToBal = []
kP = .5 #proportional constant 
kD = 1 #dirivitive constant

def driveForward(distance,speed):
    motorLeft.run_angle(speed,distance,Stop.HOLD,wait=False)
    motorRight.run_angle(speed,distance,Stop.HOLD)
 
def autoBalance(kP,kD): 
    angleTreshholdMin=2
    angleTreshholdMax=6
    autoBalanceMode = False
    balanceCount = 0
    lastError = 0
    while True:
        angleX = hub.imu.tilt()[1]
        if (not autoBalanceMode and abs(angleX)>angleTreshholdMax):
            autoBalanceMode = True
            balanceCount = 0
        if (autoBalanceMode and abs(angleX)<=angleTreshholdMin):
            autoBalanceMode = False
        if (balanceCount > 3000):
            break
        if (autoBalanceMode):
            hub.light.on(Color.RED)
            error = umath.sin(umath.radians(angleX))
            derivative = lastError - error
            lastError = error
            speed = kP*error + kD*derivative 
            balanceCount = 0
        if (not autoBalanceMode):
            balanceCount+=1
            hub.light.on(Color.GREEN)
            speed = 0
        #print("error " + str(angleX) + "; correction " + str(speed) +"; kP " + str(error) +"; kD " + str(lastError) ) 
        motorLeft.run(speed*1000)
        motorRight.run(speed*1000)

kDList = []
average = []
kD= 0.125
for i in range(0,10):
    kD = -kD if kD>0 else kD*-2
    timeToBal.clear()
    average.append(0)
    for n in range(0,10):
        driveForward(100,1000)
        timer.reset()
        autoBalance(kP,kD)
        timeToBal.append(timer.time())
        average[i] = sum(timeToBal)/len(timeToBal)
    kDList.append(average)
    print(str(kD) + ": " + str(average[i]) + "   -----Battery:"+ str(hub.battery.voltage()))
