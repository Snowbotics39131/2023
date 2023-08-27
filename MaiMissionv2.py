from PortMap import *
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from Estimation import *
class BananaMission(MissionBase):
    def __init__(self):
        #redzone 1 east 14 north
        simpleEstimate.initial(0,0,0)
        pass #starting pose
    def routine(self):
        self.runAction(SeriesAction(
            DriveStraightAction(310),
           
            DriveTurnAction(-45),
            DriveStraightAction(800),
            DriveTurnAction(45),
            DriveStraightAction(380),
            DriveTurnAction(-45),
            DriveStraightAction(180),
            DriveStraightAction(-180),
            DriveTurnAction(45),
            DriveStraightAction(-380),
            DriveTurnAction(-90),
            DriveStrightAction(160),
            DriveStraightAction(-160)
            #ParallelAction( DriveStraightAction(),SpinMotor(-270,100)),
            #SpinMotor(360,150)
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