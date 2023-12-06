from PortMap import *
from MissionBase import *
from BasicDriveActions import *
#0, 3
class Finish(MissionBase):
    def routine(self):
        driveBase.settings(straight_speed=400)
        self.runAction(DriveStraightAction(280, then=Stop.NONE))
        driveBase.settings(straight_speed=300)
        self.runAction(DriveCurveAction(300, -90, then=Stop.NONE))
        driveBase.settings(straight_speed=500)
        self.runAction(DriveStraightAction(1160, then=Stop.NONE))
        driveBase.settings(straight_speed=300)
        self.runAction(DriveCurveAction(100, -45))
        driveBase.settings(straight_speed=200)
        self.runAction(DriveStraightAction(-40))
if __name__=='__main__':
    import autotime2 as autotime
    event=autotime.Event('Finish')
    event.start()
    Finish().run()
    event.stop()
    print(str(event))