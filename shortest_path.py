#!/usr/bin/env python3
try:
    from Estimation import Pose
except:
    #can't import Estimation in CPython, need this for testing
    class Pose:  # pose is the postion of a robot at an x y angle
        x = 0  # is from the left wall of the field are negative
        y = 0  # is from the orgin to the non orgin
        a = 0  # angle
    
        def __init__(self, x, y, a):  # constructor defines intial position
            self.x = x
            self.y = y
            self.a = a
        
        def appendPose(self,pose):
            self.x += pose.x
            self.y += pose.y
            self.a = (self.a + pose.a)%360 #not sure this is right
from graph import *
nav_graph=Graph()
#TODO: build a graph used for navigation
def shortest_path(start, end):
    output=dijkstra(nav_graph, nav_graph.closest_vertex(start.x, start.y), nav_graph.closest_vertex(end.x, end.y))
    #FIXME: angle shouldn't always be 0
    output=[Pose(i[0], i[1], 0) for i in output]
    return [start]+output+[end]