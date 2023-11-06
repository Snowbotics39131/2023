from PortMap import * #PortMap has all the import
from move_camera import *
from pushcamera import *
from Crane_Mission import *

# Normally, the center button stops the program. But we want to use the
# center button for our menu. So we can disable the stop button.
hub.system.set_stop_button(None)
#Prime Mode works by assigning each attachment a prime number. This number is
#raised to the power of the number of times the attachment is run.
#2, 4, 8, 3, 9, 27, 5, 25, 125
#2 Digit Mode works by having the first digit as the attachment and the second
#digit as the number of the run.
#11, 12, 13, 21, 22, 23, 31, 32, 33
#Order Mode is works by increasing the number each subsequent mission.
#1, 2, 3, 4, 5, 6, 7, 8, 9
MODE='order'
if MODE=='prime':
    mission_numbers=['2', '3', '5', '25']
elif MODE=='2digit':
    mission_numbers=['11', '21', '31', '32']
elif MODE=='order':
    mission_numbers=['1', '2', '3', '4']
mission_funcs=[
    CombinedMission().run,
    CraneMission().run,
    PushCamera().run,
    CraftCreator().run
]
missionList=mission_numbers

def runProgram(mission):
    try:
        mission_funcs[mission_numbers.index(mission)]()
    except KeyError:
        print(f'There is no mission: {mission}')

pressed={}

runBytes = hub.system.storage(offset=0,read=1,)
print(int.from_bytes(runBytes, 'big'))
try:
    n=mission_numbers.index(int.from_bytes(runBytes, 'big'))
except ValueError:
    n=0

try: missionList[n]
except: n=0
while True:
    hub.display.number(int(missionList[n]))

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