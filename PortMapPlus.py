from pybricks.hubs import *
#split to another file to make it easier for the inexperienced
def hubType():
    global hub
    try:
        hub = CityHub()
        return 'city'
    except: pass
    try:
        hub = MoveHub()
        return 'move'
    except: pass
    try:
        hub = EV3Brick()
        return 'EV3'
    except: pass
    try:
        hub = TechnicHub()
        return 'technic'
    except: pass
    try:
        hub = PrimeHub()
        print(f'{hub.battery.voltage()}mV')
        return 'prime'
    except: pass
    try:
        hub = EssentialHub()
        return 'essential'
    except: pass
    return 'virtual'

def hubDef(): return hub
class Device:
    devicesList=["motorLeft","motorRight","driveBase","colorSensorLeft","colorSensorRight", "ultrasonicSensor"] #offical name list
    output = "PortMap.Device("
    def __init__(self):
        "procedurally generates variables like has_{capability}  ex: device.has_motorLeft"
        for device in self.devicesList:
            try: exec(device)
            except: exec("self.has_"+device+"=False",{'self':self}) #check this out!
            else:
                exec("self.has_"+device+"=True",{'self':self})
                self.output += device + ', '
    def __str__(self):
        return self.output + '\b\b)'