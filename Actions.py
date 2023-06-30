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
 
class ParallelAction(Action):
 
    def __init__(self,*actions):
        self.mActions = actions
    #override
    def start(self):
        ''' Run code once when the action is started, for setup'''
        for Action in self.mActions: Action.start() 
    #override    
    def update(self):
        for Action in self.mActions: Action.update() 
        '''Called by runAction in AutoModeBase iteratively until isFinished returns true.'''
        pass
    #override    
    def isFinished(self):
        '''Returns whether or not the code has finished execution'''
        for Action in self.mActions: 
            if not Action.isFinished():
                return False
        return True
    #override
    def done(self):
        ''' Run code once when the action finishes, usually for clean up'''
        for Action in self.mActions: Action.done() 


class DriveStraightAction(Action):

#example action should probably share a drive actions file  
    def __init__(self,distance):
        self.distance = distance

    #overriding the method in the parent class
    def start(self):
        driveBase.straight(self.distance,wait=True)
    #override
    def update(self): pass
    #override
    def isFinished(self):
        if (driveBase.done()):
            System.out.println("Drive finished")
            return True    
        return False
    #override    
    def done(self): pass

class SpinMotor(Action):

    def __init__(self,*args,**kwargs):
        '''same as Motor.run_angle'''
        self.args = args
        self.kwargs = kwargs

    def start(self):
        motorCenter.run_angle(args,ka)
    #override
    def update(self): pass
    #override
    def isFinished(self):
        if (driveBase.done()):
            System.out.println("Drive finished")
            return True    
        return False
    #override    
    def done(self): pass