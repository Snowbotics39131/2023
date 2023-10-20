---
title: Framework 
layout: default
---
# Snowbotics Framework Documentation

## What is Snowbotics Framework?

Snowbotics Framework is a Python programing system created by the members of FLL team 39131 Snowbotics that makes it easier for students to code FLL robots. It is built on top of the Pybricks software, which is a Python library for Lego robots.

https://github.com/Snowbotics39131/FLL-Pre-Season-Code

## Why use Snowbotics Framework?

Snowbotics Framework utilizes the object-oriented nature of Python to make it easier to code an FLL robot and puts more advanced robotics control concepts in the hands of novice programmers. There are several advantages to using Python in FLL. Python allows teams to write more complex code, use cooperation and version control software like GitHub, and is more applicable to their future endeavors. However, there is a steep learning curve associated with using Python, which makes it difficult for some teams to use. Pybricks is a micropython for FLL system that is powerful and well designed, but it lacks some of the features and ease of use of the Lego Word Block programming language.

Snowbotics Framework is a good choice for teams that want to use Python in FLL, but don't have the time or resources to learn Python from scratch. It is also a good choice for teams that are looking for a more powerful and flexible coding system than Pybricks.

## Features

**Modular File System**: Snowbotics Framework provides a modular file system that separates missions, components, and infrastructure code into different files. This makes it easier to read, understand, and maintain code. It also makes it easier for teams to collaborate on projects. Some files are designed to be more accessible for novices, moving the supporting complicated code to other files for experienced coders.

**Start Menu**: Snowbotics Framework includes a start menu that makes it easy to choose which code to run without a computer. This is a critical feature for FLL competitions, and it is something that Pybricks does not have.

**Parallelization**: Snowbotics Framework includes an action system that makes it easy to run steps in parallel. This is not possible in micropython, but the action system replicates this functionality as far as FLL is concerned.

**Port Map/Cross Platform Compatibility**: The port map feature of Snowbotics Framework is a powerful tool that can help teams to configure their robots quickly and easily. It also provides a safety net by automatically detecting errors and allowing the robot to continue running in multiple configurations. The port map file lists the physical parameters of the robot, such as the number of motors and sensors, and their respective ports. The framework uses this information to automatically determine which sensors and motors are enabled and to configure the robot accordingly. If the robot is not configured correctly, the framework will generate a detailed error message. This can help teams to identify and fix problems before they start coding. The port map file also allows teams to run the same code on different robots with different dimensions or configurations. This is because the framework can automatically determine which robot is running and correct the code accordingly. And while this code is generally designed to work with the LEGO Spike Prime, it can also work with other robot systems allowing team members to practice with other robots at home.

## How does it work?
