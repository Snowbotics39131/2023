import sys
import pygame
from pygame.locals import *
import asyncio
from bleak import BleakScanner, BleakClient
import time

# nRF UART Service UUID. 
UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

# Replace this with the name of your hub if you changed
# it when installing the Pybricks firmware.
HUB_NAME = "Pybricks Hub"

MTU = 20
SEP = chr(183)

def hub_filter(device, ad):
    return device.name and device.name.lower() == HUB_NAME.lower()


def handle_disconnect(_):
    print("Hub was disconnected.")


def handle_rx(_, data: bytearray):
    print("Received:", data)


class Bluetooth: 
    
    buffer = []
    busy = False
    async def setup(self):
        self.device = await BleakScanner.find_device_by_filter(hub_filter)
        self.client = BleakClient( self.device, disconnected_callback=handle_disconnect)
        try:
            # Connect and get services.
            await self.client.connect()
            await self.client.start_notify(UART_TX_CHAR_UUID, handle_rx)
            nus = self.client.services.get_service(UART_SERVICE_UUID)
            self.rx_char = nus.get_characteristic(UART_RX_CHAR_UUID)
            
                    # Tell user to start program on the hub.
            print("Start the program on the hub now with the button.")
        except Exception as e:
            # Handle exceptions.
            print(e)
            
    async def sendBuffer(self):
        global MTU
        self.busy = True
        chunk = self.buffer[:MTU]
        self.buffer = self.buffer[MTU:]
        data = bytes(chunk)
        await self.client.write_gatt_char(self.rx_char, data)
        if self.buffer:
            self.sendBuffer()
        else:
            self.busy = False
        
       
        
    async def pushString(self,s):
        if not self.busy:
            print ("push: " + s)
            for c in s:
                self.buffer.append(ord(c))
            await self.sendBuffer()
    
        
    async def update():
        pass
        
class Joystick_handler(object):
    def __init__(self, id):
        self.id = id
        self.joy = pygame.joystick.Joystick(id)
        self.name = self.joy.get_name()
        self.joy.init()
        self.numaxes    = self.joy.get_numaxes()
        self.numballs   = self.joy.get_numballs()
        self.numbuttons = self.joy.get_numbuttons()
        self.numhats    = self.joy.get_numhats()

        self.axis = []
        for i in range(self.numaxes):
            self.axis.append(self.joy.get_axis(i))

        self.ball = []
        for i in range(self.numballs):
            self.ball.append(self.joy.get_ball(i))

        self.button = []
        for i in range(self.numbuttons):
            self.button.append(self.joy.get_button(i))

        self.hat = []
        for i in range(self.numhats):
            self.hat.append(self.joy.get_hat(i))

class Joystick():
    class program:
        "Program metadata"
        name    = "Pygame Joystick Test"
        version = "0.1"
        author  = "Johnathan Pollard"
        nameversion = name + " " + version
        
    def setup(self):
        pygame.init()
        pygame.event.set_blocked((MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN))
        
        joycount = pygame.joystick.get_count()
        if joycount == 0:
            print("This program only works with at least one joystick plugged in. No joysticks were detected.")
            quit(1)
        joy = []
        for i in range(joycount):
            joy.append(Joystick_handler(i))
        self.joystick=joy[0]
        
        self.resolution = (100, 100)
        self.screen = pygame.display.set_mode(self.resolution, RESIZABLE)
        pygame.display.set_caption(self.program.nameversion)
    
    def update(self):
        for event in [pygame.event.wait(), ] + pygame.event.get():
            # QUIT             none
            # ACTIVEEVENT      gain, state
            # KEYDOWN          unicode, key, mod
            # KEYUP            key, mod
            # MOUSEMOTION      pos, rel, buttons
            # MOUSEBUTTONUP    pos, button
            # MOUSEBUTTONDOWN  pos, button
            # JOYAXISMOTION    joy, axis, value
            # JOYBALLMOTION    joy, ball, rel
            # JOYHATMOTION     joy, hat, value
            # JOYBUTTONUP      joy, button
            # JOYBUTTONDOWN    joy, button
            # VIDEORESIZE      size, w, h
            # VIDEOEXPOSE      none
            # USEREVENT        code
            if event.type == QUIT:
                self.quit()
            elif event.type == KEYDOWN and event.key in [K_ESCAPE, K_q]:
                self.quit()
            elif event.type == VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.size, RESIZABLE)
            elif event.type == JOYAXISMOTION:
                self.joystick.axis[event.axis] = event.value
            elif event.type == JOYBALLMOTION:
                self.joystick.ball[event.ball] = event.rel
            elif event.type == JOYHATMOTION:
                self.joystick.hat[event.hat] = event.value
            elif event.type == JOYBUTTONUP:
                self.joystick.button[event.button] = 0
            elif event.type == JOYBUTTONDOWN:
                self.joystick.button[event.button] = 1
    def quit(self, status=0):
        pygame.quit()
        sys.exit(status)
        
    def getData(self):
        '''joyDict ={
            "name" :self.joystick.name,
            "LX" :  self.joystick.axis[0],
            "LY" :  self.joystick.axis[1],
            "RX" :  self.joystick.axis[2],
            "RY" :  self.joystick.axis[3],
            "L" :  self.joystick.axis[4],
            "R" :  self.joystick.axis[5],
            "HATX" :self.joystick.hat[0],
            "HATY" :self.joystick.hat[0],
            "Button0":self.joystick.button[0],
            "Button1":self.joystick.button[1],
            "Button2":self.joystick.button[2],
            "Button3":self.joystick.button[3],
            "Button4":self.joystick.button[4],
            "Button5":self.joystick.button[5],
            "Button6":self.joystick.button[6],
            "Button7":self.joystick.button[7],
            "Button8":self.joystick.button[8],
            "Button9":self.joystick.button[9],
        }'''
        buttonHolder = 0
        for i in range(0,len(self.joystick.button)):
            buttonHolder += self.joystick.button[i]*pow(2,i)            
            # map buttons to binary in an int 
        buttonHolder += (self.joystick.axis[4]>0)*pow(2,len(self.joystick.button)-1)
        buttonHolder += (self.joystick.axis[5]>0)*pow(2,len(self.joystick.button))
        hatHolder = 0
        hatHolder += self.joystick.hat[0][0]+1
        hatHolder += (self.joystick.hat[0][1]+1)*3
        clampLYAxis = int((-self.joystick.axis[1]+1)*100)
        clampLXAxis = int((-self.joystick.axis[0]+1)*100)
        clampRYAxis = int((-self.joystick.axis[3]+1)*100)
        clampRXAxis = int((-self.joystick.axis[2]+1)*100)
        
        joyDict = [clampLYAxis,clampLXAxis,clampRYAxis,clampRXAxis,buttonHolder,hatHolder]
        return ",".join(map(lambda n :f'{n:x}', joyDict))
    
        
        
class Main():
    
    def __init__(self):
        self.joystick = Joystick()
        self.bluetooth = Bluetooth()
    async def setup(self):
        self.joystick.setup()
        await self.bluetooth.setup() 
    
    async def sendMessage(self,command,value):
        global SEP
        print("sendMessage")
        await self.bluetooth.pushString(command + SEP + value + '\n')
        
    async def update(self):
        self.joystick.update()
        await self.sendMessage("c",self.joystick.getData())
    
    async def run(self):
        await self.setup()
        while True:
            await self.update()
            await asyncio.sleep(.02)

if __name__ == "__main__":
    main = Main()
    asyncio.run(main.run())