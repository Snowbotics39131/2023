from PortMap import *
from pybricks.geometry import *

class Subsystem():
    def update(self):
        pass
    def done(self):
        pass

class Gyro(Subsystem):
    angle = 0 
    angular_velocity =0
    def __init__(self):
        self.gyro = hub.imu
    def getAngularVelocity(self):
        return self.angular_velocity
    def getAngle(self):
        return self.angle
    def update(self):
        self.angle = self.gyro.heading()
        self.angular_velocity = self.gyro.angular_velocity(Axis.Z)
gyro = Gyro()
class GyroKalmanFilter(Subsystem):
    def __init__(self):
        print("using Kalman")
        # Sampling time
        self.dt = 0.005

        # Initialize the state vector and covariance matrix
        self.x0 = Matrix([[0], [0]])  # [angle, angular_velocity]
        self.P0 = Matrix([[1, 0], [0, 1]])

        # Define the state transition matrix, measurement matrix, process noise covariance matrix, and measurement noise covariance matrix
        self.F = Matrix([[1, self.dt], [0, 1]])
        self.H = Matrix([[0, 1]])
        self.Q = Matrix([[0.001, 0], [0, 0.001]]) #set to the (sd of the noise)^2 
        self.R = Matrix([[0.001]]) #set to the (sd of the noise)^2 

    def getStateEstimate(self):
        return self.x0

    def update(self):
        gyro_reading = -gyro.getAngularVelocity()
        # Prediction step
        x_pred = self.F * self.x0
        P_pred = (self.F * self.P0) * self.F.T  + self.Q
        # Update step
        z = Matrix([[gyro_reading]])
        y = z - (self.H * x_pred)
        S = (self.H * P_pred) * self.H.T + self.R
        K = P_pred * self.H.T * (1/S)
        x = x_pred + K * y
        # Identity Matrix
        I = Matrix([[1,0],[0,1]])
        P = (I - K * self.H) * P_pred * (I - K * self.H).T + K * self.R * K.T

        # Update state estimate and covariance matrix
        self.x0 = x
        self.P0 = P

kalmanFilter = GyroKalmanFilter()

class DataRecorder(Subsystem):
    def __init__(self):
        self.time = StopWatch()
        self.data = []
        self.rate = 20
        self.i = 0
        print("recording data")
    def update(self):
        self.i+=1
        if (not self.i%self.rate): 
            self.data.append({self.time.time(), gyro.getAngle(), driveBase.angle(), kalmanFilter.getStateEstimate()[0]})
            out = (str(kalmanFilter.getStateEstimate()[0]) + "  gyro   " + str(gyro.getAngle()))
            print(out)
        if len(self.data)>100:
            self.data.pop(0)
    def done(self):
        for datum in self.data:
            print(datum)

dataRecorder = DataRecorder()

SubsystemsList = [gyro,kalmanFilter,dataRecorder]
driveBase.reset()
while True:
    for subsystem in SubsystemsList:
        subsystem.update()
    wait(5)
for subsystem in SubsystemsList:
    subsystem.done()

