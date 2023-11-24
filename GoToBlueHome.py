from Actions import *
from AdvancedActions import *
from BasicDriveActions import *
from MissionBase import *
class SpinMotorD(Action):
    name = "SpinMotorD"
    def __init__(self,*args,**kwargs):
        '''run_angle(speed: Number, rotation_angle: Number, then: Stop=Stop.HOLD, wait: bool=True) -> None'''
        self.args = args
        self.kwargs = kwargs
        self.kwargs['wait'] = False
    def start(self):
        simpleEstimate.addAction(self.name)
        motorBack.run_angle(*self.args,**self.kwargs)
    def isFinished(self):
        return motorBack.done()
#4 east 1 north
class GoToBlueHome(MissionBase):
    def routine(self):
        #global motorBack
        #try:
        #    motorBack=Motor(Port.D, Direction.COUNTERCLOCKWISE)
        #except OSError:
        #    pass #Assume PortMap already detected it
        self.runAction(DriveCurveAction(300, 90, then=Stop.NONE))
        self.runAction(DriveStraightAction(65, then=Stop.NONE))
        self.runAction(DriveCurveAction(190, -90, then=Stop.NONE))
        self.runAction(DriveStraightAction(100))
        driveBase.settings(turn_rate=90)
        self.runAction(DriveCurveAction(20, 180, then=Stop.NONE))
        driveBase.settings(turn_rate=180)
        self.runAction(DriveStraightAction(150, then=Stop.NONE))
        self.runAction(DriveCurveAction(290, -55))
        self.runAction(SpinMotorD(200, 90))
        self.runAction(DriveTurnAction(-15, then=Stop.NONE))
        self.runAction(DriveStraightAction(350, then=Stop.NONE))
        self.runAction(DriveTurnAction(30, then=Stop.NONE))
        self.runAction(DriveStraightAction(100))
        self.runAction(DriveTurnAction(-80, then=Stop.NONE))
        self.runAction(DriveStraightAction(120))
        #self.runAction(DriveCurveAction(205.67, -19.6))
        #self.runAction(DriveCurveAction(205.67, 19.6))
        #self.runAction(DriveStraightAction(-10))
        self.runAction(DriveTurnAction(45, then=Stop.NONE))
        self.runAction(DriveCurveAction(460, 90))
        driveBase.stop()
#6 west 1 north
class Chicken(MissionBase):
    def routine(self):
        self.runAction(DriveCurveAction(57, -90))
        self.runAction(DriveStraightAction(50))
        self.runAction(DriveCurveAction(330, 45))
        self.runAction(DriveStraightAction(50))
        motorBack.run_time(-1100, 2000)
        self.runAction(DriveCurveAction(-600, 45))
if __name__=='__main__':
    wait_for_button_press()
    try:
        motorBack=Motor(Port.D, Direction.COUNTERCLOCKWISE)
    except OSError:
        pass
    motorBack.angle()
    GoToBlueHome().run()
    wait_for_button_press()
    Chicken().run()