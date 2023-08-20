from PortMap import *
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from Estimation import *
class BananaMission(MissionBase):
    def __init__(self):
        #redzone 10 east 0 north
        simpleEstimate.initial(0,0,0)
        pass #starting pose
    def routine(self):
        #self.runAction(DriveStraightAction(1000))
        self.runAction(SeriesAction(
            ParallelAction( DriveStraightAction(620),SpinMotor(-270,100)),
           
            DriveTurnAction(90),
            DriveStraightAction(470),
            DriveTurnAction(-90),
            DriveStraightAction(60),
            SpinMotor(360,150)
        ))
                                      
        #self.runAction(ParallelAction(DriveStraightAction(100),SpinMotor(1000,1000)))
        
        #runAction()

    def done(self):
        simpleEstimate.update()
        print(simpleEstimate.log)


if __name__ == "__main__": #run on file run but not import
    BananaMission()

BananaMission = BananaMission()
BananaMission.run()