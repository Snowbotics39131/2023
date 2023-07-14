from PortMap import *
from Kinematics import Kinematics
from pybricks.parameters import Icon

kinematics = Kinematics(hub,0,0,0)
def mission2():
    print("mission2")
    hub.display.icon(Icon.HAPPY)
    kinematics.precalibrate(200)
    kinematics.reset(0,0,0)
    driveBase.straight(1000,Stop.HOLD,False)
    print("time(ms),angularV,angle,xVelocity,xAcceleration")
    while not driveBase.done():
        kinematics.update()
    av =[x[4] for x in kinematics.log]
    print(sum(av)/len(av))
    
    

if __name__ == "__main__": #run on file run but not import
    mission2()
