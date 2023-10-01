# only tested in CPython
try:
    from pybricks.tools import StopWatch
except:
    from time import perf_counter

    class StopWatch:
        def time(self):
            return perf_counter()*1000
stopwatch = StopWatch()
times = [(stopwatch.time(), 'start', True)]
deltas = [(0, 'start', True)]


def checkpoint(message, automatic):
    time = stopwatch.time()
    delta = time-times[len(times)-1][0]
    times.append((time, automatic, message))
    deltas.append((delta, automatic, message))
    print(f'{delta}ms\t{"auto" if automatic else "manl"}\t{message}')


def print_all_deltas():
    total_automatic = 0
    total_manual = 0
    for i in deltas[1:]:
        print(f'{i[0]}ms\t{"auto" if i[1] else "manl"}\t{i[2]}')
        if i[1]:
            total_automatic += i[0]
        else:
            total_manual += i[0]
    total_grand = total_automatic+total_manual
    allowed_time = 150000
    print(f'Automatic Total:\t{total_automatic}ms\t{total_automatic/total_grand*100}%')
    print(f'Manual Total:\t{total_manual}ms\t{total_manual/total_grand*100}%')
    print(f'Grand Total:\t{total_grand}/{allowed_time}ms')
    print('Time OK' if total_grand <= allowed_time else f'{total_grand-allowed_time}ms too long')


if __name__ == '__main__':
    try:
        from pybricks.tools import wait
    except ImportError:
        from time import sleep

        def wait(ms):
            sleep(ms/1000)
    wait(1000)
    checkpoint('manl cp 1', False)
    wait(2000)
    checkpoint('auto cp 2', True)
    wait(3000)
    checkpoint('manl cp 3', False)
    wait(4000)
    checkpoint('auto cp 4', True)
    print_all_deltas()
