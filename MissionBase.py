from Actions import *
from BasicDriveActions import *
from Estimation import *
from PortMap import *

class MissionEndedException(Exception):
    pass

'''https://github.com/Team254/FRC-2022-Public/blob/main/src/main/java/com/team254/frc2022/auto/modes/AutoModeBase.java'''

class MissionBase:
    mUpdateRate = 1.0/10.0
    mActive = False
    mIsInterrupted = False
    startPose = None
    endPose = None

    def setStart(self):
        pass

    def run(self):
        self.mActive=True
        try:
           
            self.routine()
        except MissionEndedException:
            print("MISSION DONE!!!! ENDED EARLY!!!!")
            return
        self.done()
            
    def done(self):
        pass
    
    def stop(self):
        self.mActive = False

    def isActive(self):
        return self.mActive
       

    def isActiveWithRaise(self):
        if(not self.mActive): raise MissionEndedException()
        return self.isActive()

    def interrupt(self): 
        self.mIsInterrupted = True
        print("Mission Interrupted")
    
    def resume(self):
        self.mIsInterrupted = False
        print("Mission resumed")
    
    def runAction(self,action): #Action action
        self.isActiveWithRaise()
        waitTime = (self.mUpdateRate*1000)
        action.start()
        while(self.isActiveWithRaise() and (not action.isFinished()) and (not self.mIsInterrupted)):
            action.update()
            wait(waitTime)
            #wait/sleep and error catches?
            #threading?
        action.done()
        

    def getIsInterrupted(self):
        return self.mIsInterrupted


class Sequence:
    def __init__(self, *missions):
        self.missions = missions
    def run(self):
        for i in self.missions:
            GoToPoint(i.startPose).run()
            i.run()
