from shortest_path import *
from MissionBase import *
from Estimation import Pose
class DoNothingMission(MissionBase):
    startPose=Pose(100, 400, 45)
class DoNothingMission2(MissionBase):
    startPose=Pose(300, 200, 270)
Sequence(DoNothingMission(), DoNothingMission2()).run()