import PortMap as pm
import pblogging as logging
logging.basicConfig(logging.INFO)
timer=pm.StopWatch() #timer used only for analysis
class PID_: #PID is already a PyBricks class, so that name can't be used.
    def __init__(self, getfunc, setfunc, target, kP=1, kI=0.01, kD=0.1):
        self.getfunc=getfunc
        self.setfunc=setfunc
        self.target=target
        self.kP=kP
        self.kI=kI
        self.kD=kD
        self.olderror=(self.target-self.getfunc())/self.target
        self.ierror=self.olderror
    def config(self, target=None, kP=None, kI=None, kD=None, getfunc=None, setfunc=None):
        if target!=None:
            self.target=target
        if kP!=None:
            self.kP=kP
        if kI!=None:
            self.kI=kI
        if kD!=None:
            self.kD=kD
        if getfunc!=None:
            self.getfunc=getfunc
        if setfunc!=None:
            self.setfunc=setfunc
    def cycle(self):
        error=(self.target-self.getfunc())/self.target
        self.ierror+=error
        derror=error-self.olderror
        self.setfunc(self.kP*error+self.kI*self.ierror+self.kD*derror)
        self.olderror=error
class LineFollow:
    def __init__(self, kP=1, kI=0, kD=0.1, reflecttarget=35):
        #35 is the ideal color reflection combination of black and
        #white divided to reduce number size between 1 and 0
        self.followleftpid=PID_(pm.colorSensorLeft.reflection, self.followleftfunc, reflecttarget, kP, kI, kD)
        self.followrightpid=PID_(pm.colorSensorRight.reflection, self.followrightfunc, reflecttarget, kP, kI, kD)
        self.findleftpid=PID_(pm.colorSensorLeft.reflection, self.findleftfunc, reflecttarget, kP, kI, kD)
        self.findrightpid=PID_(pm.colorSensorRight.reflection, self.findrightfunc, reflecttarget, kP, kI, kD)
    def followrightfunc(self, turn):
        pm.motorLeft.run(200*(1-turn))
        pm.motorRight.run(200*(1+turn))
    def followleftfunc(self, turn):
        pm.motorLeft.run(200*(1+turn))
        pm.motorRight.run(200*(1-turn))
    def findleftfunc(self, speed):
        pm.motorLeft.run(50*speed)
    def findrightfunc(self, speed):
        pm.motorRight.run(50*speed)
    def follow_left(self, distance):
        while pm.driveBase.distance()<distance:
            self.followleftpid.cycle()
    def follow_right(self, distance):
        while pm.driveBase.distance()<distance:
            self.followrightpid.cycle()
    def find_line(self):
        white=60
        black=30
        state_left='start'
        logging.info('left start')
        state_right='start'
        logging.info('right start')
        pm.motorLeft.run(100)
        pm.motorRight.run(100)
        while state_left!='done' or state_right!='done':
            logging.debug(str(pm.colorSensorLeft.reflection())+' '+str(pm.colorSensorRight.reflection())+' '+str(timer.time()))
            if state_left=='start':
                if pm.colorSensorLeft.reflection()>=white:
                    state_left='white'
                    logging.info('left white')
            if state_left=='white':
                if pm.colorSensorLeft.reflection()<=black:
                    state_left='black'
                    logging.info('left black')
            if state_left=='black':
                if pm.colorSensorLeft.reflection()>=white:
                    pm.motorLeft.brake()
                    state_left='pid'
                    logging.info('left pid')
            if state_left=='pid':
                self.findleftpid.cycle()
                if abs(self.findleftpid.target-self.findleftpid.getfunc())<=2:
                    pm.motorLeft.hold()
                    state_left='done'
                    logging.info('left done')
            if state_right=='start':
                if pm.colorSensorRight.reflection()>=white:
                    state_right='white'
                    logging.info('right white')
            if state_right=='white':
                if pm.colorSensorRight.reflection()<=black:
                    state_right='black'
                    logging.info('right black')
            if state_right=='black':
                if pm.colorSensorRight.reflection()>=white:
                    pm.motorRight.brake()
                    state_right='pid'
                    logging.info('right pid')
            if state_right=='pid':
                self.findrightpid.cycle()
                if abs(self.findrightpid.target-self.findrightpid.getfunc())<=1:
                    pm.motorRight.hold()
                    state_right='done'
                    logging.info('right done')
if __name__=='__main__':
    testfollow=LineFollow()
    testfollow.find_line()
    #testfollow.follow_right(1200)