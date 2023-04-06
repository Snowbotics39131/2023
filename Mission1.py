from PortMap import *

def mission1():
    hub.light.on(Color.RED)
    print ("mission1")
    while True:
        wait(200)
        if Button.RIGHT in hub.buttons.pressed():
            hub.light.on(Color.GREEN)

if __name__ == "__main__": #run on file run but not import
    mission1()