from PortMap import *
from Estimation import *
class Action:
    name = ""
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
    def run(self):
        self.start()
        while not self.isFinished():
            self.update()
        self.done()
def update_dec(func):
    def output(self, *args, **kwargs):
        if self.use_clock:
            time=self._stopwatch.time()
            if time<self.period:
                self._update_rate_flag=True
            else:
                self._stopwatch.reset()
                if not self._update_rate_flag:
                    print(f'update rate too slow: {time}/{self.period}ms')
                self._update_rate_flag=False
                if not self.is_interrupted:
                    func(self, *args, **kwargs)
        else:
            if not self.is_interrupted:
                func(self, *args, **kwargs)
    return output
class ActionPlus:
    def __init__(self, period=100, use_clock=True):
        self.period=period
        self.use_clock=use_clock
        self.is_interrupted=False
        self._stopwatch=StopWatch()
        self._update_rate_flag=True
    def start(self):
        self._stopwatch.reset()
    @update_dec
    def update(self):
        pass
    def isFinished(self):
        raise NotImplementedError('Must implement isFinished method of ActionPlus')
    def done(self):
        pass
    def run(self):
        self.start()
        while not self.isFinished():
            self.update()
        self.done()
    def interrupt(self):
        self.is_interrupted=True
    def resume(self):
        self.is_interrupted=False
    def isInterrupted(self):
        return self.is_interrupted
 
class ParallelAction(ActionPlus): #child class of class Action
 
    def __init__(self,*actions):
        self.mActions = actions
        super().__init__(use_clock=False)
    #override
    def start(self):
        ''' Run code once when the action is started, for setup'''
        for action in self.mActions: action.start() 
        super().start()
    #override    
    @update_dec
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

class SeriesAction(ActionPlus):
    mCurrentAction = None
    mRemainingActions = []
    def __init__(self,*actions):
        self.mRemainingActions = list(actions)
        super().__init__(use_clock=False)

    #override
    def start(self):
        super().start()
    #override
    @update_dec
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

class SpinMotor(Action):
    name = "SpinMotor"
    def __init__(self,*args,**kwargs):
        '''run_angle(speed: Number, rotation_angle: Number, then: Stop=Stop.HOLD, wait: bool=True) -> None'''
        self.args = args
        self.kwargs = kwargs
        self.kwargs['wait'] = False

    def start(self):
        simpleEstimate.addAction(self.name)
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
    def done(self): 
        simpleEstimate.removeAction(self.name)
if __name__=='__main__':
    class TestActionPlus(ActionPlus):
        def __init__(self):
            print('TestActionPlus __init__')
            super().__init__(period=200)
        def start(self):
            print('TestActionPlus start')
            super().start()
        @update_dec
        def update(self):
            print('TestActionPlus update')
        def isFinished(self):
            pass
        def done(self):
            print('TestActionPlus done')
    interrupt_1=False
    resume_2=False
    interrupt_3=False
    resume_4=False
    test_action_plus=TestActionPlus()
    test_action_plus.start()
    stopwatch=StopWatch()
    while stopwatch.time()<5000:
        second=int(stopwatch.time()/1000)
        if second==1 and not interrupt_1:
            test_action_plus.interrupt()
            interrupt_1=True
        elif second==2 and not resume_2:
            test_action_plus.resume()
            resume_2=True
        elif second==3 and not interrupt_3:
            test_action_plus.interrupt()
            interrupt_3=True
        elif second==4 and not resume_4:
            test_action_plus.resume()
            resume_4=True
        test_action_plus.update()
    test_action_plus.done()