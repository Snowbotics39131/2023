try:
    import umath
except ImportError:
    import math as umath

def shortestDirectionBetweenBearings(target,current): # finds the shortest point from a to b between two points on a circle 
    return ((target-current+540)%360-180)
    #180 is always -180

def atan2(b,a): # arc tangent version 2 converts from degrees to radians
    return (umath.atan2(b,a)/umath.pi*180) #

def sin(a):
    return umath.sin(umath.radians(a))

def cos(a):
    return umath.cos(umath.radians(a))