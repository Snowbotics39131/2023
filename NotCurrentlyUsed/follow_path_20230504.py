from PortMap import *
#kP=0.8 #Porportional constant
#kD=50 #Differential constant
#kI=0 #intergral constant
#olderror=0 #
#Ierror=0 # Intergral error
#speed=200 #forward speed
#distance=1300 #how far to go
#derrorlessthan0=0 #derror = differential error
#derrormorethan0=0 
#derrorequals0=0
timer=StopWatch() # timer used only for analysis
class myPID: #PID is already a PyBricks class, so that name can't be used.
    def __init__(self, getfunc, setfunc, target, kP=1, kI=0.01, kD=0.1, checkfeedback=False):
        self.getfunc=getfunc
        self.setfunc=setfunc
        self.target=target
        self.kP=kP
        self.kI=kI
        self.kD=kD
        #self.checkfeedback=checkfeedback
        self.olderror=(self.target-self.getfunc())/self.target
        self.ierror=self.olderror
        #if checkfeedback:
        #    self.oldderror=0
        #    self.negative=False
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
        #tick=timer.time()
        error=(self.target-self.getfunc())/self.target
        self.ierror+=error
        derror=error-self.olderror
        #if self.checkfeedback:
        #    if abs(derror)>abs(self.oldderror*7) and self.oldderror!=0:
        #        if self.negative:
        #            self.negative=False
        #            print('Normal', derror, self.oldderror)
        #        else:
        #            self.negative=True
        #            print('Negative', derror, self.oldderror)
        #if self.checkfeedback and self.negative:
        #    self.setfunc(-(self.kP*error+self.kI*self.ierror+self.kD*derror))
        #else:
        #    self.setfunc(self.kP*error+self.kI*self.ierror+self.kD*derror)
        self.setfunc(self.kP*error+self.kI*self.ierror+self.kD*derror)
        self.olderror=error
        #if self.checkfeedback:
        #    self.oldderror=derror
        #tock=timer.time()
        #print(tick-tock)
class LineFollow2:
    def __init__(self, kP=1, kI=0, kD=0.1, reflecttarget=35): # 35 is the ideal color reflection combination of black and white divided to reduce number size between 1 and 0
        self.followleftpid=myPID(colorSensorLeft.reflection, self.followleftfunc, reflecttarget, kP, kI, kD) #checkfeedback does not work at all
        self.followrightpid=myPID(colorSensorRight.reflection, self.followrightfunc, reflecttarget, kP, kI, kD)
    def followrightfunc(self, turn):
        motorLeft.run(200*(1-turn))
        motorRight.run(200*(1+turn))
    def followleftfunc(self, turn):
        motorLeft.run(200*(1+turn))
        motorRight.run(200*(1-turn))
    def follow_left(self, distance):
        while driveBase.distance()<distance:
            self.followleftpid.cycle()
    def follow_right(self, distance):
        #oldtime=0
        while driveBase.distance()<distance:
            #nowtime=timer.time()
            #if nowtime>oldtime: #run this every 1 millisecond
            #if nowtime%50<oldtime%50:
            #    self.followrightpid.cycle()
            #    #print(nowtime%100-oldtime%100)
            #oldtime=nowtime
            self.followrightpid.cycle()
testfollow=LineFollow2()
testfollow.follow_right(1200)
class LineFollow:
    def __init__(self, kP=0.8, kD=1, kI=0.01, reflecttarget=35): # 35 is the ideal color reflection combination of black and white divided to reduce number size between 1 and 0
        self.kP=kP
        self.kD=kD
        self.kI=kI
        self.reflecttarget=reflecttarget
    def config(self, kP=None, kD=None, kI=None, reflecttarget=None):
        if kP!=None:
            self.kP=kP
        if kD!=None:
            self.kD=kD
        if kI!=None:
            self.kI=kI
        if reflecttarget!=None:
            self.reflecttarget=reflecttarget
    def follow(self, distance, speed=200):
        ierror=0
        olderror=0
        while driveBase.distance()<distance: # go until distance
            error=(colorSensorRight.reflection()-self.reflecttarget)/self.reflecttarget #Calculate error based on reflection target
            if error==olderror: #if the sensor hasn't updated yet, don't reset derror
                continue
            derror=error-olderror # takes the difference of current error from old error
            ierror+=error # adds error to I error 
            if abs(error)<0.1: # resets Ierror if its close to 0
                ierror=0
            #print('error '+str(error))
            #print('Derror '+str(Derror))
            #if Derror<0: # counts how many times derror is below 0
            #    derrorlessthan0+=1 
            #elif Derror: # counts how many times derror is equal to 1
            #    derrorequals0+=1
            #elif Derror>0: # counts how many times derror is greater than 1
            #    derrormorethan0+=1
            #print(str(derrorlessthan0)+' '+str(derrorequals0)+' '+str(derrormorethan0))
            print(self.kP, self.kI, self.kD, 'constants pid')
            print(error, ierror, derror, 'errors pid')
            turn=self.kP*error+self.kD*derror+self.kI*ierror # creates a correction based on the pid controller constants and their error
            try:
                print(self.kP*error/turn, self.kD*derror/turn, self.kI*ierror/turn, 'percents pdi')
            except ZeroDivisionError:
                print('turn is 0 percents pdi')
            #print(turn,error,Derror)
            motorLeft.run(speed*(1-turn*2)) # 1- turn ensures that corrections are porportional to the speed.
            motorRight.run(speed*(1+turn))
            olderror=error # out with the old data in with the new.
            print(timer.time(), 'timer') # prints the current timer
            # remember when doing something sequentially after this not stopping the motors would affect the program
            hub.display.number(colorSensorRight.reflection())
    def follow_left(self, distance, speed=200):
        ierror=0
        olderror=0
        while driveBase.distance()<distance: # go until distance
            error=(colorSensorLeft.reflection()-self.reflecttarget)/self.reflecttarget #Calculate error based on reflection target
            if error==olderror: #if the sensor hasn't updated yet, don't reset derror
                continue
            derror=error-olderror # takes the difference of current error from old error
            ierror+=error # adds error to I error 
            if abs(error)<0.1: # resets Ierror if its close to 0
                ierror=0
            #print('error '+str(error))
            #print('Derror '+str(Derror))
            #if Derror<0: # counts how many times derror is below 0
            #    derrorlessthan0+=1 
            #elif Derror: # counts how many times derror is equal to 1
            #    derrorequals0+=1
            #elif Derror>0: # counts how many times derror is greater than 1
            #    derrormorethan0+=1
            #print(str(derrorlessthan0)+' '+str(derrorequals0)+' '+str(derrormorethan0))
            print(self.kP, self.kI, self.kD, 'constants pid')
            print(error, ierror, derror, 'errors pid')
            turn=self.kP*error+self.kD*derror+self.kI*ierror # creates a correction based on the pid controller constants and their error
            try:
                print(self.kP*error/turn, self.kD*derror/turn, self.kI*ierror/turn, 'percents pdi')
            except ZeroDivisionError:
                print('turn is 0 percents pdi')
            #print(turn,error,Derror)
            motorLeft.run(speed*(1+turn*2)) # 1- turn ensures that corrections are porportional to the speed.
            motorRight.run(speed*(1-turn))
            olderror=error # out with the old data in with the new.
            print(timer.time(), 'timer') # prints the current timer
            # remember when doing something sequentially after this not stopping the motors would affect the program
            hub.display.number(colorSensorRight.reflection())
    def find_line(self):
        while colorSensorRight.reflection()<70:
            hub.display.number(colorSensorRight.reflection())
            driveBase.straight(5)
        while colorSensorRight.reflection()>20:
            hub.display.number(colorSensorRight.reflection())
            driveBase.straight(5)
        while colorSensorRight.reflection()<70:
            hub.display.number(colorSensorRight.reflection())
            driveBase.straight(5)
        driveBase.straight(-10)
        driveBase.turn(90)
    def find_line_2(self):
        state='start'
        driveBase.drive(150, 0)
        while True:
            if state=='start':
                if colorSensorLeft.reflection()>70 or colorSensorRight.reflection()>70:
                    state='seen white'
            if state=='seen white':
                if colorSensorLeft.reflection()<20 or colorSensorRight.reflection()<20:
                    state='seen black'
            if state=='seen black':
                if colorSensorLeft.reflection()>70 or colorSensorRight.reflection()>70:
                    state='found'
            if state=='found':
                driveBase.straight(50)
                driveBase.turn(90)
                driveBase.stop()
                break
    def pid_left(self):
        plerror=(colorSensorLeft.reflection()-self.reflecttarget)/self.reflecttarget
        plkP=1
        plkD=0.1
        plolderror=0
        plDerror=0
        while abs(plerror)>0:
            plerror=(colorSensorLeft.reflection()-self.reflecttarget)/self.reflecttarget
            plDerror=plerror-plolderror
            motorLeft.run_angle(50, plkP*plerror+plkD*plDerror)
            plolderror=plerror
    def find_line_3(self):
        state_left='start'
        state_right='start'
        motorLeft.run(100)
        motorRight.run(100)
        i=0
        while True:
            i+=1
            if i>2:
                i=0
            if i==0:
                print(colorSensorLeft.reflection(), colorSensorRight.reflection())
            if state_left=='start':
                if colorSensorLeft.reflection()>50:
                    state_left='seen white'
                    print('left seen white')
            if state_left=='seen white':
                if colorSensorLeft.reflection()<30:
                    state_left='seen black'
                    print('lfet seen black')
            if state_left=='seen black':
                if colorSensorLeft.reflection()>50:
                    state_left='found'
                    print('left found')
            if state_left=='found':
                self.pid_left()
                motorLeft.stop()
                #print('left stopped')
            if state_right=='start':
                if colorSensorRight.reflection()>70:
                    state_right='seen white'
                    print('right seen white')
            if state_right=='seen white':
                if colorSensorRight.reflection()<20:
                    state_right='seen black'
                    print('right seen black')
            if state_right=='seen black':
                if colorSensorRight.reflection()>70:
                    state_right='found'
                    print('right found')
            if state_right=='found':
                motorRight.stop()
                #print('right stopped')
            if state_left=='found' and state_right=='found':
                break
            wait(50)
#testfollow=LineFollow()
#testfollow.find_line_3()
#wait(3000)
#testfollow.follow(1300)
#testfollow.follow_left(1300)
#while True:
#    hub.display.number(colorSensorRight.reflection())