from BasicDriveActions import *
from MissionBase import *
#11 north 1 west facing west
#angled a bit to the right
class GoToRedHome(MissionBase):
    def routine(self):
        self.runAction(DriveStraightAction(2000, speed=977))
        driveBase.stop()
#left corner 4 east 12 north
class GoToExpertLocations(MissionBase):
    def routine(self):
        self.runAction(DriveTurnAction(20))
        self.runAction(DriveStraightAction(600))
        self.runAction(DriveTurnAction(25))
        self.runAction(DriveStraightAction(30))
if __name__=='__main__':
    from AdvancedActions import wait_for_button_press
    GoToRedHome().run()
    wait_for_button_press()
    GoToExpertLocations().run()