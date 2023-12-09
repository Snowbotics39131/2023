from PortMap import * #PortMap has all the import
import newscenechange
import move_camera
import GoToBlueHome
import GoToBlueHomeOneWay
import Crane_Mission
import pushcamera
import finish_omni
from autotime2 import *

# Normally, the center button stops the program. But we want to use the
# center button for our menu. So we can disable the stop button.
hub.system.set_stop_button(None)

#missionList = ["1","2","3", '4'] #add here for new mission
MIN_MISSION=0
MAX_MISSION=8
missionList=[str(i) for i in range(MIN_MISSION, MAX_MISSION+1)]

def runProgram(mission):
    if mission=='0':
        newscenechange.SceneChange(2).run() #yellow
    if mission == "1":
        newscenechange.SceneChange().run()  #pink
    elif mission == "2":
        move_camera.MoveCamera().run()
    elif mission == "3":
        move_camera.GoToBlueHome().run()
    elif mission=='4':
        GoToBlueHome.Chicken().run()
    elif mission=='5':
        Crane_Mission.CraneMission().run()
    elif mission=='6':
        pushcamera.PushCamera().run()
    elif mission=='7':
        pushcamera.CraftCreator().run()
    elif mission=='8':
        finish_omni.Finish().run()
    else:
        print("There is no mission:{mission}")
    #if mission=='1':
    #    newscenechange.SceneChange().run()
    #elif mission=='2':
    #    move_camera.MoveCamera().run()
    #elif mission=='3':
    #    move_camera.GoToBlueHome().run()
    #elif mission=='4':
    #    Crane_Mission.CraneMission().run()
    #elif mission=='5':
    #    pushcamera.PushCamera().run()
    #elif mission=='6':
    #    pushcamera.CraftCreator().run()
    #elif mission=='7':
    #    GoToBlueHome.Chicken().run()

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
timer = Event("Mission Time")
timer.start()
runProgram(missionList[n])
timer.stop()
print(str(timer))