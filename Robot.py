#from Mission1 import mission1 
from Mission2 import mission2
from PortMap import * #PortMap has all the import

# Normally, the center button stops the program. But we want to use the
# center button for our menu. So we can disable the stop button.
hub.system.set_stop_button(None)

missionList = ["1","2","3","B"] #add here for new mission

def runProgram(mission):
    if mission == "1":
        import Tim_autbalance_
    elif mission == "2":
        mission2()
    elif mission == "B":
        import autobalancePID
    else:
        print("There is no mission:{mission}")

pressed={}
runBytes = hub.system.storage(offset=0,read=1,)
n=int.from_bytes(runBytes, 'big')
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