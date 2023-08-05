from PortMap import *
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
        self.labels = ["Speed","Turn","Buttons"]

    def _process(self, cmd: str, message: str):
        """
        Processes the frame content to respond with setup configuration
        or read command properties 
        """
        if cmd == 'setup':
            self._send('setup', ujson.dumps(self.config))
        if cmd == 'c' and self.config['commands']:
            commandsList = message.split(',')
            self.commands = {label: int(p) if p.isdigit() else 0 
                                for label, p in zip(self.labels, commandsList)}
        else:
            # for debug purposes
            print("cmd", cmd, len(cmd), "message", message)


hub = PrimeHub()
bluetoothTest = BluetoothTest("PrimeHub")
mode = 0
speed = 0
turn = 0
buttons = 0
speedMultiplier = 0
while True:
    received = bluetoothTest.receive()
    if received == 'setup':
        # aiBrick app requested for setup
        hub.light.on(Color.ORANGE)
    elif received in ['commands']:
        #print("'%s' commands detected!" % bluetoothTest.commands)
        pass
    for class_label, class_commands in bluetoothTest.commands.items():
            if class_label == "Buttons":
                buttons == class_commands
            if class_label == "Speed":
                speed = class_commands - 50
            if class_label == "Turn":
                turn = class_commands - 50
            
    hub.display.number(speedMultiplier)
    motorRight.run((speed+turn)*100)
    motorLeft.run((speed-turn)*100)