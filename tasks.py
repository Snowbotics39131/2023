class Task:
    def __init__(self):
        self.subtask = 0
        self.subtasks = []
        self.stopped = False
        self.terminated = False
    def cycle(self):
        raise NotImplementedError
    def tick(self):
        if self.terminated or self.stopped:
            return
        self.subtask += 1
        if len(self.subtasks) == 0:
            self.subtask = 0
        else:
            self.subtask %= len(self.subtasks) + 1
        if self.subtask == 0:
            self.cycle()
        else:
            self.subtasks[self.subtask-1].tick()
    def __call__(self):
        while not self.terminated or self.stopped:
            self.tick()
if __name__=='__main__':
    class GetMotorEncoderTask(Task):
        def cycle(self):
            print('getting motor encoders')
    class GetColorSensorTask(Task):
        def cycle(self):
            print('getting color sensors')
    class GetUltrasonicTask(Task):
        def cycle(self):
            print('getting ultrasonic')
    class UpdateSensorTask(Task):
        def __init__(self):
            super().__init__()
            self.subtasks = [
                GetMotorEncoderTask(),
                GetColorSensorTask(),
                GetUltrasonicTask(),
            ]
        def cycle(self):
            pass
    class EstimatePoseTask(Task):
        def cycle(self):
            print('estimating pose')
    class PIDTask(Task):
        def cycle(self):
            print('updating PID')
    class ControlMotorTask(Task):
        def __init__(self):
            super().__init__()
            self.subtasks = [
                PIDTask(),
            ]
        def cycle(self):
            print('controlling motors')
    class SuperTask(Task):
        def __init__(self):
            super().__init__()
            self.subtasks = [
                UpdateSensorTask(),
                EstimatePoseTask(),
                ControlMotorTask(),
            ]
        def cycle(self):
            pass
    SuperTask()()
