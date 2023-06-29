from PortMap import * # standard do not remove

class LineFollow: # creats class for following 35 which is the ideal mix of white and black.
    kP = .7 # proportional constant
    kI = 0.000 # intergral constant
    kD = 0.01 # dirivitive constant

    def settings(self,kP,kI,kD): # method that lets you input custom pid values
        self.kP = kP #self means that its the version of the class unself means its the version in the argument
        self.kI = kI
        self.kD = kD
# two lines define each side of the robots color sensors should be combined in the future
    def Left(self,speed, distance): # has the arguments for the speed and distance
        driveBase.reset() # reset the drive base to start tracking distance
        Ierror=0 # intergral error
        lastError=0 # starting at zero
        while (distance>driveBase.distance()): # argument for loop ending is if it has gone the distance defined
            error=(colorSensorLeft.reflection()-35)/35 # takes the difference 
            #if abs(value)<3:
            #   error=0
            Ierror+= error # adding Ierror to error
            Derror=error-lastError # defining difference in errors between the last cycle and the current cycle
            correction=(error*self.kP) + (Ierror*self.kI) +(Derror*self.kD) # PID controller 
            motorLeft.run(speed*(1+correction)) 
            motorRight.run(speed*(1-correction)) # ensures the correction is porportional to the speed of travel
            lastError=error # resets the error out with the old in with the new
        motorLeft.stop 
        motorRight.stop

    def Right(self,speed, distance):
        driveBase.reset()
        Ierror=0
        lastError=0
        while (distance>driveBase.distance()):
            error=(colorSensorRight.reflection()-35)/35
            #if abs(value)<3:
            #   error=0
            Ierror+= error 
            Derror=error-lastError
            correction=(error*self.kP) + (Ierror*self.kI) +(Derror*self.kD)
            motorLeft.run(speed*(1-correction*1.20))
            motorRight.run(speed*(1+correction))
            lastError=error
        motorLeft.stop
        motorRight.stop

