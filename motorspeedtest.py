from PortMap import *
motorCenter.control.limits(1110, 2000, 199)
print(motorCenter.control.limits())
speed, acceleration, torque=motorCenter.control.limits()
motorCenter.run(speed)
while True:
    pass