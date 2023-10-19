#forklift attachment, all the way down, tray loaded
#1 north, 6 west, blue home
#facing north
from BasicDriveActions import *
from MissionBase import *
print(hub.battery.voltage())
def wait_for_button_press(message=None, checkpoint_message=None):
    if message is not None:
        print(message)
    hub.speaker.beep()
    while not hub.buttons.pressed():
        pass
class PushTray(MissionBase):
    def routine(self):
        start_db_settings=driveBase.settings()
        driveBase.settings(turn_rate=90)
        self.runAction(DriveStraightAction(420, speed=max(driveBase.settings()[0], 500)))
        self.runAction(DriveTurnAction(-45))
        self.runAction(DriveStraightAction(250))
        self.runAction(DriveTurnAction(-45))
        self.runAction(DriveStraightAction(580))
        driveBase.settings(straight_speed=200, turn_rate=45)
        self.runAction(DriveTurnAction(90))
        self.runAction(DriveStraightAction(110))
        self.runAction(DriveStraightAction(-50))
        self.runAction(SpinMotor(300, 135))
        self.runAction(DriveStraightAction(-60))
        wait_for_button_press()
        self.runAction(DriveTurnAction(-180))
        wait_for_button_press()
        self.runAction(DriveStraightAction(110))
        wait_for_button_press()
        self.runAction(SpinMotor(180,1460))
        driveBase.settings(*start_db_settings)
if __name__=='__main__':
    push_tray=PushTray()
    push_tray.run()