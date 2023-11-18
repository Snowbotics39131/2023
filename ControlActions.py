from Actions import *
class NullAction(Action):
    def isFinished(self):
        return True
class IfAction(Action):
    def __init__(self, test_func, true_action, false_action=NullAction()):
        self.test_func=test_func
        self.true_action=true_action
        self.false_action=false_action
    def start(self):
        self.condition=self.test_func()
        if self.condition:
            self.true_action.start()
        else:
            self.false_action.start()
    def update(self):
        if self.condition:
            self.true_action.update()
        else:
            self.false_action.update()
    def isFinished(self):
        if self.condition:
            return self.true_action.isFinished()
        else:
            return self.false_action.isFinished()
    def done(self):
        if self.condition:
            self.true_action.done()
        else:
            self.false_action.done()
#not really a for because you're not iterating over anything
class RepeatAction(Action):
    def __init__(self, times, action):
        self.times=times
        self.action=action
        self.times_done=0
    def start(self):
        self.action.start()
    def update(self):
        if self.action.isFinished():
            self.action.done()
            self.times_done+=1
            if self.times_done<self.times:
                self.action.start()
        else:
            self.action.update()
    def isFinished(self):
        if self.times_done<self.times:
            return False
        return self.action.isFinished()
class WhileAction(Action):
    def __init__(self, test_func, action):
        self.test_func=test_func
        self.action=action
        self.complete=False
    def start(self):
        if self.test_func():
            self.action.start()
        else:
            self.complete=True
    def update(self):
        if self.action.isFinished():
            self.action.done()
            if self.test_func():
                self.action.start()
            else:
                self.complete=True
        else:
            self.action.update()
    def isFinished(self):
        return self.complete
    def done(self):
        pass
class TryAction(Action):
    def __init__(self, try_action, except_action=NullAction(), else_action=NullAction()):
        self.try_action=try_action
        self.except_action=except_action
        self.else_action=else_action
        self.state='try'
    def start(self):
        try:
            self.try_action.start()
        except Exception:
            self.state='except'
            self.except_action.start()
    def update(self):
        if self.state=='try':
            if self.try_action.isFinished():
                try:
                    self.try_action.done()
                except Exception:
                    self.state='except'
                    self.except_action.start()
                else:
                    self.state='else'
                    self.else_action.start()
            else:
                try:
                    self.try_action.update()
                except Exception:
                    self.state='except'
                    self.except_action.start()
        elif self.state=='except':
            self.except_action.update()
        elif self.state=='else':
            self.else_action.update()
    def isFinished(self):
        if self.state=='try':
            return False
        elif self.state=='except':
            return self.except_action.isFinished()
        elif self.state=='else':
            return self.else_action.isFinished()
    def done(self):
        if self.state=='except':
            self.except_action.done()
        elif self.state=='else':
            self.else_action.done()
class ExitAction(Action):
    def start(self):
        raise SystemExit
class FunctionAction(Action):
    def __init__(self, func, *args, **kwargs):
        self.func=func
        self.args=args
        self.kwargs=kwargs
    def start(self):
        self.func(*self.args, **self.kwargs)
    def isFinished(self):
        return True
if __name__=='__main__':
    import urandom
    NullAction().run()
    FunctionAction(print, 'I am a function.').run()
    IfAction(lambda: False, FunctionAction(print, 'True'), FunctionAction(print, 'False')).run()
    IfAction(lambda: True, FunctionAction(print, 'True'), FunctionAction(print, 'False')).run()
    RepeatAction(3, FunctionAction(print, 'RepeatAction')).run()
    WhileAction(lambda: urandom.randrange(10)!=3, FunctionAction(print, 'WhileAction')).run()
    TryAction(FunctionAction(print, 'try action successful'), FunctionAction(print, 'except action'), FunctionAction(print, 'else action')).run()
    TryAction(FunctionAction(lambda: 2/0, 'try action fail'), FunctionAction(print, 'except action'), FunctionAction(print, 'else action')).run()
    ExitAction().run()
