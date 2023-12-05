from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

connected_old=False
status_old=0
while True:
    connected=hub.charger.connected()
    status=hub.charger.status()
    voltage=hub.battery.voltage()
    hub.display.number(int(voltage/100))
    if connected!=connected_old:
        if connected:
            hub.speaker.play_notes(['C3/4', 'C5/4'])
        else:
            hub.speaker.play_notes(['C5/4', 'C3/4'])
        connected_old=connected
    if status!=status_old:
        if status_old!=0:
            if status==2:
                hub.speaker.play_notes(['C3/4', 'C4/4', 'C5/4'])
            elif status==3:
                hub.speaker.play_notes(['C5/4', 'C4/4', 'C3/4'])
        status_old=status