from PortMap import *

class Action:
    def start(self):
        ''' Run code once when the action is started, for setup'''
        pass
    
    def update(self):
        '''Called by runAction in AutoModeBase iteratively until isFinished returns true.'''
        pass
    
    def isFinished(self):
        '''Returns whether or not the code has finished execution'''
        pass

    def done(self):
        ''' Run code once when the action finishes, usually for clean up'''
        pass
 
class ParallelAction(Action): #child class of class Action
 
    def __init__(self,*actions):
        self.mActions = actions
    #override
    def start(self):
        ''' Run code once when the action is started, for setup'''
        for action in self.mActions: action.start() 
    #override    
    def update(self):
        '''Called by runAction in AutoModeBase iteratively until isFinished returns true.'''
        for action in self.mActions: action.update() 
        pass
    #override    
    def isFinished(self):
        '''Returns whether or not the code has finished execution'''
        for action in self.mActions: 
            if not action.isFinished():
                return False
        return True
    #override
    def done(self):
        ''' Run code once when the action finishes, usually for clean up'''
        for action in self.mActions: action.done() 

class SeriesAction(Action):
    mCurrentAction = None
    mRemainingActions = []
    def __init__(self,*actions):
        self.mRemainingActions = list(actions)

    #override
    def start(self):
        pass
    #override    
    def update(self):
        if(self.mCurrentAction == None):
            if(not self.mRemainingActions): return
            self.mCurrentAction = self.mRemainingActions.pop(0)
            self.mCurrentAction.start()
        self.mCurrentAction.update()
        if(self.mCurrentAction.isFinished()):
            self.mCurrentAction.done()
            self.mCurrentAction = None

        pass
    #override    
    def isFinished(self):
        return not self.mRemainingActions and self.mCurrentAction == None
    #override
    def done(self):
        pass



class DriveStraightAction(Action):

#example action should probably share a drive actions file  
    def __init__(self,distance):
        self.distance = distance

    #overriding the method in the parent class
    def start(self):
        driveBase.straight(self.distance,wait=False)
    #override
    def update(self): pass
    #override
    def isFinished(self):
        if (driveBase.done()):
            print("Drive finished")
            return True    
        return False
    #override    
    def done(self): pass

class SpinMotor(Action):

    def __init__(self,*args,**kwargs):
        '''run_angle(speed: Number, rotation_angle: Number, then: Stop=Stop.HOLD, wait: bool=True) -> None'''
        self.args = args
        self.kwargs = kwargs
        self.kwargs['wait'] = False

    def start(self):
        motorCenter.run_angle(*self.args,**self.kwargs)

    #override
    def update(self): pass
    #override
    def isFinished(self):
        if (motorCenter.done()):
            print("Motor finished")
            return True    
        return False
    #override    
    def done(self): pass