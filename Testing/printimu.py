from PortMap import *
from pybricks.parameters import Axis
while True:
    wait(1000)
    print(hub.imu.acceleration(Axis.X), hub.imu.acceleration(Axis.Y), hub.imu.acceleration(Axis.Z))
