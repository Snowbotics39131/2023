from PortMap import *
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from Estimation import *
import autotime
class WaitForButtonPressAction(Action):
    def __init__(self, message=None, checkpoint_message=None):
        self.message=message
        self.checkpoint_message=checkpoint_message
    def start(self):
        if self.message:
            print(self.message)
        hub.speaker.beep()
        while not hub.buttons.pressed():
            pass
    def update(self):
        if hub.buttons.pressed():
            self._is_finished=True
    def isFinished(self):
        return self._is_finished
    def done(self):
        autotime.checkpoint(self.checkpoint_message if self.checkpoint_message else f'WaitForButtonPressAction({repr(self.message)})', False)
#5 west
#1 north
#facing north
#blue home
#attachment down
#tray loaded
class CraneMission(MissionBase):
    def routine(self):
        driveBase.settings(turn_rate=90),
        self.runAction(SeriesAction(
            DriveStraightAction(440),
            DriveTurnAction(-45),
            DriveStraightAction(250),
            DriveTurnAction(-45),
            DriveStraightAction(590)))
        driveBase.settings(turn_rate=45)
        self.runAction(SeriesAction(
            DriveTurnAction(90),
            DriveStraightAction(150), #square
            WaitForButtonPressAction(),
            DriveStraightAction(-50),
            WaitForButtonPressAction(),
            SpinMotor(300, 145),
            DriveStraightAction(-45),
            WaitForButtonPressAction(),
            DriveTurnAction(-180),
            DriveStraightAction(110),
            SpinMotor(180,1460),
            ParallelAction(
                SpinMotor(230,-1460),
                SeriesAction(
                DriveStraightAction(-66),
                DriveTurnAction(-90),
                DriveStraightAction(700))),
            SpinMotor(430,1230),
            DriveStraightAction(65),
            DriveTurnAction(-110),
            DriveStraightAction(20),
            DriveTurnAction(-90),
            DriveStraightAction(-180),
            DriveTurnAction(-95),
            DriveStraightAction(195),
            DriveStraightAction(110),
            DriveTurnAction(180),
            SpinMotor(430,-1230),
            DriveStraightAction(115),
            DriveTurnAction(-75)
            ))

if __name__ == "__main__": #run on file run but not import
    CraneMission()
    CraneMission = CraneMission()
    CraneMission.run()
