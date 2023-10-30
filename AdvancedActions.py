from Actions import *
from PortMap import *
import autotime
def wait_for_button_press(message=None, checkpoint_message=None):
    if message is not None:
        print(message)
    hub.speaker.beep()
    while not hub.buttons.pressed():
        pass
    autotime.checkpoint(f'wait_for_button_press({repr(message)})' if checkpoint_message is None else checkpoint_message, False)
class WaitForButtonPressAction(Action):
    def __init__(self, message=None, checkpoint_message=None):
        self.message=message
        self.checkpoint_message=checkpoint_message
        self._is_finished=False
    def start(self):
        if self.message:
            print(self.message)
        hub.speaker.beep()
    def update(self):
        if hub.buttons.pressed():
            self._is_finished=True
    def isFinished(self):
        return self._is_finished
    def done(self):
        autotime.checkpoint(self.checkpoint_message if self.checkpoint_message else f'WaitForButtonPressAction({repr(self.message)})', False)
class SpinMotorTime(Action):
    def __init__(self, speed, time):
        self.speed=speed
        self.time=time
    def start(self):
        motorCenter.run_time(self.speed, self.time, wait=False)
    def update(self):
        pass
    def done(self):
        pass
    def isFinished(self):
        return motorCenter.done()
class SpinMotorUntilStalled(Action):
    def __init__(self, *args, **kwargs):
        #kwargs['wait']=False
        self.args=args
        self.kwargs=kwargs
    def start(self):
        motorCenter.run_until_stalled(*self.args, **self.kwargs)
    def update(self):
        pass
    def done(self):
        pass
    def isFinished(self):
        return motorCenter.done()
class SpinMotorAngleOrUntilStalled(Action):
    done_=0
    def __init__(self, speed, angle):
        self.speed=speed
        self.angle=angle
    def start(self):
        motorCenter.run_angle(self.speed, self.angle, wait=False)
    def update(self):
        if motorCenter.stalled():
            motorCenter.brake()
            self.done_=2
            print('motor stalled')
        elif motorCenter.done():
            self.done_=1
            print('motor completed angle')
    def isFinished(self):
        """
        0 - not done before angle done
        1 - completed angle
        2 - stalled before angle done
        """
        return self.done_
class ChangeDriveBaseSettings(Action):
    def __init__(self, *args, **kwargs):
        self.args=args
        self.kwargs=kwargs
    def start(self):
        driveBase.settings(*self.args, **self.kwargs)
    def update(self):
        pass
    def isFinished(self):
        return True
    def done(self):
        pass
#This is a really hacky way of doing this.
class ExitAction(Action):
    def start(self):
        exit()
