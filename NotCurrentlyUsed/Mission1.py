from PortMap import *
from Tools import LineFollow

line = LineFollow()
#mode="Empty"
mode="Heavy"

def mission1():
    if mode== "Empty":
        print("standered")
        speed =200
    elif mode == "Heavy":    
        driveBase.settings(turn_rate=60)
        line.settings(0.55,0,0) 
        speed = 150
    print(driveBase.settings())
    driveBase.straight(10)
    driveBase.turn(-45)
    driveBase.straight(200)
    line.Right(speed,1600)
    

if __name__ == "__main__": #run on file run but not import
    mission1()