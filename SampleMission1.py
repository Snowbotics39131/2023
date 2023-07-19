from PortMap import *
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from Estimation import *
class SampleMission1(MissionBase):
    def __init__(self):
        simpleEstimate.initial(0,0,0)
        pass #starting pose
    def routine(self):
        #self.runAction(DriveStraightAction(1000))
        self.runAction(ParallelAction(GoToPoint(Pose(-250, 500, 180)),
                                      SeriesAction(
                                      SpinMotor(1000,-1000),
                                      SpinMotor(1000,1000))))
        self.runAction(ParallelAction(DriveStraightAction(100),SpinMotor(1000,1000)))
        
        #runAction()

    def done(self):
        simpleEstimate.update()
        print(simpleEstimate.log)


if __name__ == "__main__": #run on file run but not import
    SampleMission1()

sampleMission1 = SampleMission1()
sampleMission1.run()