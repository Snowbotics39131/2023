from PortMap import*
import jmath
 
def autobalance():
    
    balanced = False
    p=0
    treshold1 = 3
    treshold2 = 3
    speed = 1000
    while True:
        pitch = hub.imu.tilt()[1]+1

        if abs(pitch) > treshold1:
            MotorLeft.run(jmath.sin(pitch)*speed)
            MotorRight.run(jmath.sin(pitch)*speed)
            p=0
            print('More than threshold1')
        if  abs(pitch) < treshold2: 
            MotorLeft.hold()
            MotorRight.hold()
            p+=1  #p=p+1
            print('Less than threshold2')
            if p>10: break

        print(pitch)
    MotorLeft.run(0)
    MotorRight.run(0)
    hub.speaker.beep()
driveBase.straight(100)
autobalance()