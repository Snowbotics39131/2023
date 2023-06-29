from PortMap import*
import jmath
 
def autobalance():
    pitch = 100
    balanced = False
    p=0
    tresholdmax = 3
    tresholdmin = 3
    speed = 2500
    mode = "Balancing"
    timer = StopWatch()
    if name == "Bug":
        axis = 0
    else:
        axis = 1
    while True:
        pitch = hub.imu.tilt()[axis]
        #if mode = "not Balanced":
        print(timer.time())
        if mode == "Balanced":
            motorLeft.hold()
            motorRight.hold()
            hub.light.on(Color.GREEN)
        if mode == "Balancing":    
            motorLeft.run(jmath.sin(pitch)*speed)
            motorRight.run(jmath.sin(pitch)*speed)
            hub.light.on(Color.RED)
        if abs(pitch) > tresholdmax and mode == "Balanced": 
            mode = "Balancing"
            timer.reset
            timer.pause
        if  abs(pitch) < tresholdmin and mode == "Balancing":
            mode = "Balanced"
            timer.resume
        if mode == "Balanced" and timer.time() > 10000:
            break
    motorLeft.run(0)
    motorRight.run(0)
    hub.speaker.beep()
autobalance()