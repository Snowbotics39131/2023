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
        return self.angular_velocity
    def update(self):
        self.angle = self.gyro.heading()
        self.angular_velocity = self.gyro.angular_velocity(Axis.Z)
gyro = Gyro()
class GyroKalmanFilter(Subsystem):
    def __init__(self):
        # Initialize the state vector and covariance matrix
        self.x0 = Matrix([[0], [0]])  # [angle, angular_velocity]
        self.P0 = Matrix([[1, 0], [0, 1]])

        # Define the state transition matrix, measurement matrix, process noise covariance matrix, and measurement noise covariance matrix
        self.F = Matrix([[1, dt], [0, 1]])
        self.H = Matrix([[1], [0]])
        self.Q = Matrix([[0.0001], [0]])
        self.R = Matrix([[0.01]])
        # Sampling time
        self.dt = 0.0
    def getStateEstimate():
        return self.x0
    def update(self):
        gyro_reading = gyro.getAngularVelocity()
        # Prediction step
        x_pred = self.F * self.x0
        P_pred = self.F * self.P0 * self.F.T + self.Q

        # Update step
        z = Matrix([[gyro_reading]])
        y = z - self.H * x_pred
        S = self.H * P_pred * self.H.T + self.R
        K = P_pred * self.H.T * S.inverse()
        x = x_pred + K * y
        P = (I - K * self.H) * P_pred * (I - K * self.H).T + K * self.R * K.T

        # Update state estimate and covariance matrix
        self.x0 = x
        self.P0 = P
kalmanFilter = GyroKalmanFilter()

class DataRecorder(Subsystem):
    def __init__(self):
        self.time = StopWatch()
        self.data = []
    def update(self):
        print("running recorder")
        self.data.append({time.time(),gyro.getAngle(), driveBase.angle(), kalmanFilter.getStateEstimate() })
    def done(self):
        print(self.data)

dataRecorder = DataRecorder()

SubsystemsList = [gyro,kalmanFilter,dataRecorder]
for x in range(10):
    for subsystem in SubsystemsList:
        subsystem.update()
    wait(100)
for subsystem in SubsystemsList:
    subsystem.done()

