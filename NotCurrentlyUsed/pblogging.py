try:
    from pybricks.tools import StopWatch
except: #for testing in CPython
    from time import perf_counter
    class StopWatch:
        def time(*args, **kwargs):
            return perf_counter()
timer=StopWatch()
def debug(msg):
    if loglevel<=10:
        print(timer.time(), 'DEBUG', msg)
def info(msg):
    if loglevel<=20:
        print(timer.time(), 'INFO', msg)
def warning(msg):
    if loglevel<=30:
        print(timer.time(), 'WARNING', msg)
def error(msg):
    if loglevel<=40:
        print(timer.time(), 'ERROR', msg)
def critical(msg):
    if loglevel<=50:
        print(timer.time(), 'CRITICAL', msg)
DEBUG=10
INFO=20
WARNING=30
ERROR=40
CRITICAL=50
loglevel=30
def basicConfig(level=None):
    global loglevel
    if level!=None:
        loglevel=level