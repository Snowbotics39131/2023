from pybricks.tools import StopWatch
STATES={
    0: 'ready',
    1: 'running',
    2: 'stopped',
    3: 'stopped by parent'
}
def indent(string):
    string=string.split('\n')
    string=(f'    {i}' for i in string)
    string='\n'.join(string)
    return string
class EventError(Exception):
    pass
class Event:
    def __init__(self, name):
        self.name=name
        self.stopwatch=StopWatch()
        self.stopwatch.pause()
        self.stopwatch.reset()
        self.state=0 #0 ready; 1 running; 2 stopped manually; 3 stopped by parent
        self.subevents=[]
    def start(self):
        if self.state==0:
            print(f'starting {self.name}')
            self.state=1
            self.stopwatch.resume()
        else:
            raise EventError('Event must be in ready state to start')
    def stop(self):
        if self.state==1:
            self.stopwatch.pause()
            for i in self.subevents:
                if i.state==1:
                    i.stop()
                    i.state=3
            self.state=2
            print(f'stopped {self.name} ({self.stopwatch.time()}ms)')
        else:
            raise EventError('Event must be in running state to stop')
    def add_subevent(self, subevent):
        self.subevents.append(subevent)
    def __str__(self):
        substrs=[str(i) for i in self.subevents]
        mystr=f'{self.name} ({STATES[self.state]}, took {self.stopwatch.time()}ms)' if self.state in (2, 3) else f'{self.name} ({STATES[self.state]})'
        substrs='\n'.join(substrs)
        substrs=indent(substrs)
        output=mystr+'\n'+substrs
        return output
