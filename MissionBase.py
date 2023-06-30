from PortMap import *
from Actions import *


'''https://github.com/Team254/FRC-2022-Public/blob/main/src/main/java/com/team254/frc2022/auto/modes/AutoModeBase.java'''

class MissionBase:
    mUpdateRate = 1.0/10.0
    mActive = False
    mIsInterrupted = False
    def setStart(self):
        pass

    def run(self):
        self.mActive=True
        try:
            routine()
        except:
            print("MISSION DONE!!!! ENDED EARLY!!!!")
            return
        done()
            
    def done(self):
        pass
    
    def stop(self):
        self.mActive = False

    def isActive(self):
        return self.mActive
        '''add some error checking'''

    def interrupt(self): 
        self.mIsInterrupted = True
        print("Mission Interrupted")
    
    def resume(self):
        self.mIsInterrupted = False
        print("Mission resumed")
    
    def runAction(self,action): #Action action

        action.start()

        while(self.isActive() and not action.isFinished() and not self.mIsInterrupted):
            action.update()
            #wait/sleep and error catches?
            #threading?
        action.done()

    def getIsInterrupted(self):
        return self.mIsInterrupted
