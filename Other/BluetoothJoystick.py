from PortMap import *
import jmath
from usys import stdin
from uselect import poll
import ujson

SEP = chr(183)
EOF = '\n'

class BlutoothBase:
    """Base class for AiBrick communication."""
    frames = {}

    def __init__(self):
        self.buffer = ''
        self.nuart = poll()
        self.nuart.register(stdin)
        self._flush()

    def _send(self, cmd: str, message: str):
        """Sends the frame with given command's name and message."""
        print(cmd, SEP, message, '\n', sep='')
    
    def _flush(self):
        while self.nuart.poll(0):
            stdin.read(1)

    def receive(self):
        """
        Listens to Blueooth transmission and pushes the received bytes into 
        buffer until and of frame (EOF) byte is received. Then calls _process()
        to interpret contents of the frame and returns frame's name (command).
        If EOF was not yet received, None is returned.
        """
        while self.nuart.poll(0):
            char = stdin.read(1)  
            if char == EOF:
                received, self.buffer = self.buffer, ''
                if SEP in received:
                    cmd, message = received.split(SEP, 1)
                else:
                    cmd, message = '', received
                self._process(cmd, message)
                return self.frames.get(cmd, cmd)
            else: 
                self.buffer += char
        return None

class BluetoothTest(BlutoothBase):
    """
    Implements communication with Python PC application.
    """
    frames = {"c": "commands"}

    def __init__(self, name='', commands = True):
        super().__init__()
        self.config = {
            "name": name,
            "commands": commands
        }
        self.commands = {}
        self.labels = ["LY","LX","RY","RX","Buttons","Hat"]

    def _process(self, cmd: str, message: str):
        """
        Processes the frame content to respond with setup configuration
        or read command properties 
        """
        if cmd == 'setup':
            self._send('setup', ujson.dumps(self.config))
        if cmd == 'c' and self.config['commands']:
            commandsList = message.split(',')
            self.commands = {label: self.toInt(p) 
                                for label, p in zip(self.labels, commandsList)}
        else:
            # for debug purposes
            print("cmd", cmd, len(cmd), "message", message)
    
    def toInt(self,h):
        try:
            return int(h,16)
        except:
            return 0

class Joystick:
    joyDict ={
            "LX" :      0,
            "LY" :      0,
            "RX" :      0,
            "RY" :      0,
            "HatX":     0,
            "HatY":     0,
            "Buttons":  0,
        }
    debounceList = {
            "HatX":     0,
            "HatY":     0,
            "Buttons":  0,    
        }
    def __init__(self):
        self.bluetoothTest = BluetoothTest("PrimeHub")

    def update(self):
        received = self.bluetoothTest.receive()
        if received == 'setup':
            # aiBrick app requested for setup
            hub.light.on(Color.ORANGE)
        elif received in ['commands']:
            #print("'%s' commands detected!" % bluetoothTest.commands)
            pass
        
        for class_label, class_commands in self.bluetoothTest.commands.items():
            if class_label == "Buttons":
                self.joyDict["Buttons"] = class_commands
            if class_label == "LY":
                self.joyDict["LY"] = class_commands - 100
            if class_label == "LX":
                self.joyDict["LX"] = class_commands - 100
            if class_label == "RY":
                self.joyDict["RY"] = class_commands - 100
            if class_label == "RX":
                self.joyDict["RX"] = class_commands - 100            
            if class_label == "Hat":
                self.joyDict["HatX"] = class_commands%3 - 1
                self.joyDict["HatY"] = int(class_commands/3)%3 - 1 
        
    def getAxis(self,axis,threshold = 10):
        return self.joyDict[axis] if abs(self.joyDict[axis])>threshold else 0
    def getHatX(self,debounce = True):
        if debounce:
            if self.debounceList["HatX"] != self.joyDict["HatX"]: 
                self.debounceList["HatX"] = self.joyDict["HatX"]
                return self.joyDict["HatX"]
            else: return 0 
        else: return self.joyDict["HatX"]
    def getHatY(self,debounce = True):
        if debounce:
            if self.debounceList["HatY"] != self.joyDict["HatY"]: 
                self.debounceList["HatY"] = self.joyDict["HatY"]
                return self.joyDict["HatY"]
            else: return 0 
        else: return self.joyDict["HatY"]

    def getButton(self,buttonNumber,debounce = True):
        buttonVal = (self.joyDict["Buttons"]>>buttonNumber)&1
        if debounce:
            buttonDebounce=self.debounceList["Buttons"]>>buttonNumber&1
            if buttonDebounce != buttonVal:
                self.debounceList["Buttons"] = jmath.modifyBit(self.debounceList["Buttons"],buttonNumber,buttonVal)
                return buttonVal
            else: return 0 
        else: return buttonVal

joystick = Joystick()
speedMult = 2
centerSpeedMult = 1
count = 0
turnStick = "LX"
controlMode = "Linear"
print(motorLeft.control.limits())
while True:
    joystick.update()
    '''angle = hub.imu.heading()
    stickAngle = jmath.atan2(joystick.getAxis("RX"),joystick.getAxis("RY"))
    turn = jmath.shortestDirectionBetweenBearings(stickAngle,angle)'''
    
    speedMult += joystick.getHatY()
    centerSpeedMult += joystick.getHatX()
    if joystick.getButton(3):
        if turnStick == "LX": turnStick = "RX"
        elif turnStick == "RX": turnStick = "LX"
    hub.display.number(speedMult)
    if controlMode ==  "Linear":
        speed = joystick.getAxis("LY") * pow(2,speedMult)
        turn = joystick.getAxis(turnStick) * pow(2,speedMult)
    if controlMode == "Squared":
        speed = joystick.getAxis("LY") * speedMult
        turn = joystick.getAxis(turnStick) * speedMult
    if controlMode == "Cubed":
        speed = joystick.getAxis("LY") * pow(2,speedMult)
        turn = joystick.getAxis(turnStick) * pow(2,speedMult)
    motorLeft.run(speed-turn)
    motorRight.run(speed+turn)
    if joystick.getButton(10,debounce=False): centerSpeed = 100 
    elif joystick.getButton(11,debounce=False): centerSpeed = -100
    else: centerSpeed = 0

    motorCenter.run(centerSpeed*pow(2,centerSpeedMult))