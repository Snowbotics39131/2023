from PortMap import *


class DriveBasePlus2(DriveBase):
    def straight(self,*args,**kwargs):
        if('wait' in kwargs and not kwargs['wait']):
            super(DriveBasePlus,self).straight(*args,**kwargs)
        else:
            kwargs['wait'] = False

            super(DriveBasePlus,self).straight(*args,**kwargs)
            while not super(DriveBasePlus,self).done():
                print(super(DriveBasePlus,self).distance())


class DriveBasePlus():
    def straight(self,*args,**kwargs):
        if('wait' in kwargs and not kwargs['wait']):
            driveBase.straight(*args,**kwargs)
        else:
            kwargs['wait'] = False
            driveBase.straight(*args,**kwargs)
            while not driveBase.done():
                print(driveBase.distance())

driveBase2=DriveBasePlus2()

driveBase2.straight(1000)
wait(1000)