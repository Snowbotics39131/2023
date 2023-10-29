from PortMap import * #PortMap has all the import
from move_camera import *
from pushcamera import *
from Crane_Mission import *

# Normally, the center button stops the program. But we want to use the
# center button for our menu. So we can disable the stop button.
hub.system.set_stop_button(None)

missionList = ["1","2","3", '4'] #add here for new mission

def runProgram(mission):
    if mission == "1":
        CombinedMission().run()
    elif mission == "2":
        CraneMission().run()
    elif mission == "3":
        PushCamera().run()
    elif mission=='4':
        CraftCreator().run()
    else:
        print("There is no mission:{mission}")

pressed={}

runBytes = hub.system.storage(offset=0,read=1,)
n=int.from_bytes(runBytes, 'big')

try: missionList[n]
except: n=0
while True:
    hub.display.char(missionList[n])

    # Wait for any button.
    pressed = ()
    while not pressed:
        pressed = hub.buttons.pressed()
        wait(10)
    
    # Wait for the button to be released.
    while hub.buttons.pressed():
        wait(10)
    
    if Button.RIGHT in pressed:
        n = (0 if (n==len(missionList)-1) else n+1)
        buttonPressed = True;
    elif Button.LEFT in pressed:
        n = (len(missionList)-1 if (n==0) else n-1)
        buttonPressed = True
    elif Button.CENTER in pressed:
        buttonPressed = True
        break

hub.light.on(Color.GREEN)
wait(50)
hub.system.set_stop_button(Button.CENTER) # Now we want to use the Center button as the stop button again.
runBytes = n.to_bytes(1, 'big')
hub.system.storage(offset=0,write=runBytes)
runProgram(missionList[n])