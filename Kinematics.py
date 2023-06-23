class Dimension:
    position= 0
    positionError=0
    velocity=0
    velocityError=0
    acceleration=0
    accelerationError=0
try:
    from PortMap import *
    from pybricks.geometry import Axis
    
    class Kinematics:
        time = 0
        x = Dimension()
        y = Dimension()
        angle = Dimension()
        time = StopWatch()
        log = list()
        log.append((0,0,0,0,0,0))
        xVestimate =0
        aEstimate=0
        def __init__(self, hub, X, Y, angle):
            self.hub = hub
            self.x.position = X
            self.y.position = Y
            self.angle.position = angle
    
        def __str__(self):
            return f"X({self.x.position}),Y({self.y.position}),A({self.angle.position})"
    
        def reset(self,X,Y,angle):
            self.x.position = X
            self.y.position = Y
            self.angle.position = angle
            #hub.imu.reset_heading()
            self.time.reset()
            self.log= [(0,0,0,0,0,0)]
    
        def precalibrate(self,delay):
            time2 = StopWatch()
            time2.reset()
            while time2.time() < delay:
                self.angle.velocity = hub.imu.angular_velocity(Axis.Z)
                self.x.acceleration = hub.imu.acceleration(Axis.Y)
                tempTime =time2.time()
                tempTuple =tuple((tempTime,self.angle.velocity,self.x.acceleration,))
                self.log.append(tempTuple)
            AVList =[x[1] for x in self.log]
            XAList =[x[2] for x in self.log]
            self.angle.velocityError = sum(AVList)/len(AVList)
            self.x.accelerationError = sum(XAList)/len(XAList)
            print(self.x.accelerationError)
            
    
        def update(self):
            self.angle.velocity = hub.imu.angular_velocity(Axis.Z)-self.angle.velocityError
            self.x.acceleration = hub.imu.acceleration(Axis.Y)-self.angle.accelerationError
            self.x.velocity = (MotorLeft.speed()+MotorRight.speed())*176/(360*2)
            #self.angle.position = hub.imu.heading()
            tempTime =self.time.time()
            self.xVestimate = self.xVestimate + self.x.acceleration*(tempTime-self.log[len(self.log)-1][0])/1000
            self.aEstimate = self.aEstimate + self.angle.velocity*(tempTime-self.log[len(self.log)-1][0])/1000
            tempTuple =tuple((tempTime,self.angle.velocity,self.angle.position,self.x.velocity,self.x.acceleration,self.xVestimate,self.aEstimate))
            self.log.append(tempTuple)
            print(tempTuple)
        
        #def kalmenFilter():
except ImportError:
    pass