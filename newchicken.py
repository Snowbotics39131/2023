from PortMap import *
from MissionBase import *
class Chicken(MissionBase):
    def routine(self):
        driveBase.turn(-45)
        driveBase.straight(300)
        driveBase.turn(-30)
        driveBase.turn(30)
        driveBase.straight(50)
        try:
            motorBack.run_time(-1100, 3000)
        except:
            hub.speaker.beep()
if __name__=='__main__':
    Chicken().run()