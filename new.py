from PortMap import *
import jmath
#lineMap
obstacleMap = list([[[-44,68],[-51,68],[-44,91],[-51,91]]]) # input obstacle you want to avoid takes 4 coordinates per obstacle

class Pose: # pose is the postion of a robot at an x y angle
    x=0 # is from the left wall of the field are negative
    y=0 # is from the orgin to the non orgin
    a=0 # angle
    def __init__(self,x,y,a): # constructor defines intial position
        self.x=x
        self.y=y
        self.a=a
    
    
def superFunction(destination,location): # drives from location to the destination where both location and destination are poses
    vector=tuple((destination.x-location.x,destination.y-location.y)) # creating a vector between location and destination
    direction = jmath.atan2(vector[0],vector[1]) # using the arc tangent to detirmine the angle of the vector
    turn = jmath.shortestDirectionBetweenBearings(direction,location.a) # detirmine the shortest correction between our current angle and the angle of the shortest path
    print(vector,turn) # print data
    driveBase.turn(turn) # align to our vector
    driveBase.straight((vector[0]**2+vector[1]**2)**0.5) # drive along the vector with magnitude
    driveBase.turn(jmath.shortestDirectionBetweenBearings(destination.a,direction)) # turning to final orientation should be inline with destination

driveBase.settings(turn_rate=60) # reduces the turn rate for smoother corrections
start=Pose(-50,25,0) # 
target=Pose(-610,990,0)
#start=Pose(0,0,0)
#target=Pose(0,0,-90)
print(driveBase.settings())
superFunction(target,start)
wait(2000)
superFunction(start,target)

