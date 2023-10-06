from Actions import *
from BasicDriveActions import *
from PortMap import *
motorLeft.run(100)
motorRight.run(100)
while True:
    color_left=colorSensorLeft.color()
    color_right=colorSensorRight.color()
    print('left ', color_left)
    print('right', color_right)
    state_left=0
    state_right=0
    if state_left==0:
        if color_left!=Color.WHITE:
            motorLeft.stop()
            state_left=1
        else:
            #print('left ', color_left)
            pass
    if state_right==0:
        if color_right!=Color.WHITE:
            motorRight.stop()
            state_right=1
        else:
            #print('right', color_right)
            pass