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
#nav_graph.add_vertex(100, 100)
#nav_graph.add_vertex(600, 150)
#nav_graph.add_vertex(100, 450)
#nav_graph.add_vertex(350, 750)
#nav_graph.add_vertex(450, 500)
nav_graph.add_vertex(100, 100)
nav_graph.add_vertex(150, 600)
nav_graph.add_vertex(450, 100)
nav_graph.add_vertex(750, 350)
nav_graph.add_vertex(500, 450)
nav_graph.add_edge(nav_graph.get_id_from_coordinates(100, 100), nav_graph.get_id_from_coordinates(600, 150))
nav_graph.add_edge(nav_graph.get_id_from_coordinates(100, 100), nav_graph.get_id_from_coordinates(100, 450))
def shortest_path(start, end):
    output=dijkstra(nav_graph, nav_graph.closest_vertex(start.x, start.y), nav_graph.closest_vertex(end.x, end.y))
    output=[nav_graph.get_coordinates_from_id(i) for i in output]
    #FIXME: angle shouldn't always be 0
    output=[Pose(i[0], i[1], 0) for i in output]
    return [start]+output+[end]