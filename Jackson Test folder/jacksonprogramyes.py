from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()
motorLeft = Motor(Port.E,Direction.COUNTERCLOCKWISE)
motorRight = Motor(Port.A)

hub.light.blink(Color.RED,[150,100])

motorLeft.run(5000)
motorRight.run(5000)
wait(5000)

hub.light.blink(Color.MAGENTA,[150,100])

motorLeft.run(-5000)
motorRight.run(5000)
wait(600)

hub.light.blink(Color.RED,[150,100])
motorLeft.run(3000)
motorRight.run(3000)
wait(5000)
