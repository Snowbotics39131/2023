try: #PyBricks
    from umath import e, pi
except ModuleNotFoundError: #CPython
    from math import e, pi
class Kalman1D:
    def __init__(self, mean_funcs, variances):
        self.mean_funcs=mean_funcs
        self.variances=variances
    def estimate(self):
        means=list(i() for i in self.mean_funcs)
        means=list(i[1]*(1/self.variances[i[0]]) for i in enumerate(means))
        return sum(means)/sum(1/i for i in self.variances)
class Kalman2D:
    def __init__(self, mean_funcs, xvars, yvars):
        self.xfilter=Kalman1D(list(lambda: i()[0] for i in mean_funcs), xvars)
        self.yfilter=Kalman1D(list(lambda: i()[1] for i in mean_funcs), yvars)
    def estimate(self):
        return [self.xfilter.estimate(), self.yfilter.estimate()]
def gaussian(o, u, x):
    return (1/(o*(2*pi)**0.5))*(e**(((-0.5*(x-u)**2))/o**2))
if __name__=='__main__':
    testfilter=Kalman1D([lambda: 0, lambda :1], [0.8, 0.5])
    o=[0.8, 0.5]
    u=[0, 1]
    print(testfilter.estimate())
    from matplotlib import pyplot as plt
    plt.plot(list(range(-5, 5)), list(gaussian(o[0], u[0], i) for i in range(-5, 5)))
    plt.plot(list(range(-5, 5)), list(gaussian(o[1], u[1], i) for i in range(-5, 5)))
    plt.plot([testfilter.estimate(), testfilter.estimate()], [0, 1])
    plt.show()
