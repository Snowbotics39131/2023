#!/usr/bin/env pybricks-micropython
from MissionBase import *
from Estimation import *
from Actions import *
from BasicDriveActions import *
from PortMap import hub
class BatteryError(Exception):
    pass
if hub.battery.voltage()<7000: #guess
    raise BatteryError(f'Battery voltage less than 7000')
class Push(MissionBase):
    def routine(self):
        self.runAction(SeriesAction(
            DriveStraightAction(25),
            DriveTurnAction(-45),
            DriveStraightAction(590),
            DriveStraightAction(-100),
            DriveTurnAction(90),
            DriveStraightAction(150),
            DriveTurnAction(-90),
            DriveStraightAction(100),
            DriveTurnAction(90),
            DriveStraightAction(250)
            #FindLine(),
            #DriveStraightAction(150)
        ))
if __name__=='__main__':
    print(hub.battery.voltage())
    print(hub.battery.current())
    mission=Push()
    mission.run()