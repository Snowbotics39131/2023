# FLL-Pre-Season-Code
Hello! this is a readme file to describe the repository. This repository is code for the FLL team #39131 Snowbotics team from Colorado.

Documentaion here -> (https://snowbotics39131.github.io/FLL-Pre-Season-Code/Framework.html)

The code in this repository is mostly python, as we are currently running pybricks on our lego mindstorms robots.

# Code Stucture

This structure was inspired by FRC Team 254s [auto code](https://github.com/Team254/FRC-2022-Public/tree/main/src/main/java/com/team254/frc2022/auto)

Here are the rules to the code structure 
1. Robot.py runs missions
2. Missions are made of Actions
3. Actions can access subsystems
4. Actions can be made of other Actions
5. Subsystems include the default driveBase and motors as well as custom subsystems like the Estimation

Here is some of the code structure in a fancy mermaid chart:

```mermaid
flowchart TD
    A[Robot.py] ---> B
    A ---> C
    A ---> D
    subgraph Missions
    B[Mission1.py] 
    C[Mission2.py]
    D[Mission3.py]
    end
    subgraph Actions
    H[PathActions]
    I[MechinismActions]
    J[HubActions]
    end
    subgraph Subsystems
    L[driveBase]
    M[Motors]
    N[SensorSubsystems]
	S[Kinematics/Estimation]
    end
    B & C & D -.- Q(are made of)
    Q -.- H & I & J
    H & I & J -.- P(access)
    P -.- L & M & N & S
    S -.-> Actions
    E[MissionBase.py] -.-> Missions  
    F[PortMap.py] --> A
    G[PortMapPlus.py] --> F
    K[Actions.py] -.-> Actions

```

-----------------------------------------------------------------------------------------------------------------------------------
#License 
This project is licensed under the Creative Commons Zero (CC0) license. You are free to use, modify, and distribute this project without any restrictions.

[![License: CC0 1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
