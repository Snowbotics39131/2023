from PortMap import *
from MissionBase import *
from Actions import *

class SampleMission1(MissionBase):
    def __init__(self):
        pass #starting pose
    
    def routine(self):
        #self.runAction(DriveStraightAction(1000))
        self.runAction(ParallelAction(DriveStraightAction(1000),SpinMotor(1000,1000)))
        self.runAction(ParallelAction(DriveStraightAction(-1000),
                                      SeriesAction(
                                      SpinMotor(1000,-1000),
                                      SpinMotor(1000,1000))))
        
        #runAction()



if __name__ == "__main__": #run on file run but not import
    SampleMission1()

sampleMission1 = SampleMission1()
sampleMission1.run()