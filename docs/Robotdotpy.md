---
title: robot.py
layout: default
---
## Robot.py

The file `robot.py` is a simple mission selector for a LEGO Mindstorms Hub and the first program run when the robot starts. 

It works by first disabling the stop button, since the center button is going to be used for the menu. Then, it creates a list of mission names and a function to run each mission.

The main loop of the program works by displaying the current mission name on the Hub's display and waiting for a button press. If the right button is pressed, the next mission is selected. If the left button is pressed, the previous mission is selected. If the center button is pressed, the program exits.

Once a mission has been selected, the program sets the stop button back to the center button and then runs the selected mission.

Here is a more detailed breakdown of the code:

`from PortMap import * #PortMap has all the import`

This line imports the `PortMap` module, which contains all of the necessary imports for programming the LEGO Mindstorms Hub.

```
# Normally, the center button stops the program. But we want to use the
# center button for our menu. So we can disable the stop button.
hub.system.set_stop_button(None)
```

This line disables the stop button on the Hub.

`missionList = ["1","2","3"] #add here for new mission`

This line creates a list of mission names.

```
def runProgram(mission):
   if mission == "1":
       import SampleMission1
   elif mission == "2":
       import mission2
   else:
       print("There is no mission:{mission}")
```

This function takes a mission name as input and runs the corresponding mission.

```
pressed={}
runBytes = hub.system.storage(offset=0,read=1,)
n=int.from_bytes(runBytes, 'big')
try: missionList[n]
except: n=0
```

This section of code gets the current mission index from the Hub's storage. If the saved index is out of bounds, the index is set to 0.

```
while True:
   hub.display.char(missionList[n])
```

This loop displays the current mission name on the Hub's display.

```
   # Wait for any button.
   pressed = ()
   while not pressed:
       pressed = hub.buttons.pressed()
       wait(10)

   # Wait for the button to be released.
   while hub.buttons.pressed():
       wait(10)
```

This section of code waits for any button to be pressed and then released.

```
   if Button.RIGHT in pressed:
       n = (0 if (n==len(missionList)-1) else n+1)
       buttonPressed = True;
   elif Button.LEFT in pressed:
       n = (len(missionList)-1 if (n==0) else n-1)
       buttonPressed = True
   elif Button.CENTER in pressed:
       buttonPressed = True
       break
```

This section of code handles button presses. If the right button is pressed, the next mission is selected. If the left button is pressed, the previous mission is selected. If the center button is pressed, the program exits.

```
hub.light.on(Color.GREEN)
wait(50)
hub.system.set_stop_button(Button.CENTER) # Now we want to use the Center button as the stop button again.
```
This section of code sets the stop button back to the center button.

```
runBytes = n.to_bytes(1, 'big')
hub.system.storage(offset=0,write=runBytes)
```

This section of code saves the current mission index to the Hub's storage.

`runProgram(missionList[n])`

This line runs the selected mission.

Overall, the code is a simple but effective way to create a mission selector for a LEGO Mindstorms Hub. It is easy to understand and maintain, and it can be easily extended to support more missions.
