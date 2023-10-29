from Actions import *
from AdvancedActions import *
from MissionBase import *
from PortMap import *
class MaiAttachment(MissionBase):
    def routine(self):
        for i in range(2):
            self.runAction(SpinMotor(400, 270))
            self.runAction(SpinMotor(400, -270))
        self.runAction(WaitForButtonPressAction())
        self.runAction(SpinMotorUntilStalled(500))
class ChickenExpertAttachment(MissionBase):
    def routine(self):
        motorBack.run_time(-1100, 2000)
class OmniAttachment(MissionBase):
    def routine(self):
        self.runAction(SpinMotorUntilStalled(-400))
        self.runAction(SpinMotorUntilStalled(400))
class ForkliftAttachment(MissionBase):
    def routine(self):
        self.runAction(SpinMotorUntilStalled(500))
        self.runAction(SpinMotorUntilStalled(-500))
#This is the order they run on the field; we may present in a different order.
if __name__=='__main__':
    MaiAttachment().run()
    wait_for_button_press()
    motorBack=Motor(Port.D)
    ChickenExpertAttachment().run()
    wait_for_button_press()
    OmniAttachment().run()
    wait_for_button_press()
    ForkliftAttachment().run()