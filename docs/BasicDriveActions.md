---
title: Actions
layout: default
---
# `DriveStraightAction`

|Argument  |Type    |Default|Description                          |
|----------|--------|-------|-------------------------------------|
|`distance`|`Number`|N/A    |The distance to drive in millimeters.|

Drive straight using `driveBase`.
## `done`
Update `simpleEstimate`.
## `isFinished`
Check if the drive is complete.
## `start`
Start driving.
# `DriveTurnAction`

|Argument|Type    |Default|Description                |
|--------|--------|-------|---------------------------|
|`angle` |`Number`|N/A    |How far to turn in degrees.|

Turn a given number of degrees using `driveBase`.
## `done`
Update `simpleEstimate`.
## `isFinished`
Check if turn is finished.
## `start`
Start the turn.
# `FindLine`

|Argument       |Type    |Default|Description                               |
|---------------|--------|-------|------------------------------------------|
|`kP`           |`Number`|`1`    |Proportional coefficient.                 |
|`kI`           |`Number`|`0`    |Integral coefficient.                     |
|`kD`           |`Number`|`0.1`  |Derivative coefficient.                   |
|`reflecttarget`|`Number`|`35`   |Reflectance target for the PID controller.|

Square on a white-black-white line.
## `isFinished`
Check if squaring is complete.
## `start`
Go forward slowly and start looking for the line.
## `update`
Update states using data from color sensors.
# `FollowLineLeft`

|Argument       |Type    |Default|Description                               |
|---------------|--------|-------|------------------------------------------|
|`distance`     |`Number`|N/A    |How far to follow the line in millimeters.|
|`kP`           |`Number`|`1`    |Proportional coefficient.                 |
|`kI`           |`Number`|`0`    |Integral coefficient.                     |
|`kD`           |`Number`|`0.1`  |Derivative coefficient.                   |
|`reflecttarget`|`Number`|`35`   |Reflectance target for the PID controller.|

Follow a line using the left color sensor.
## `done`
Stop driving.
## `isFinished`
Check if the robot has gone `distance`.
## `start`
Reset `driveBase`.
## `update`
Use the PID controller to update the motor speeds.
# `FollowLineRight`
*Identical to `FollowLineLeft`, but uses the right color sensor.*
# `GoToPoint(SeriesAction)`

|Argument     |Type  |Default|Description        |
|-------------|----- |-------|-------------------|
|`destination`|`Pose`|N/A    |The point to go to.|

# `PIDController`

|Argument |Type      |Default|Description                           |
|---------|----------|-------|--------------------------------------|
|`getfunc`|`Callable`|N/A    |Function to get the measured value.   |
|`setfunc`|`Callable`|N/A    |Function to set the manipulated value.|
|`target` |`Number`  |N/A    |Target for the measured value.        |
|`kP`     |`Number`  |`1`    |Proportional coefficient.             |
|`kI`     |`Number`  |`0.01` |Integral coefficient.                 |
|`kD`     |`Number`  |`0.1`  |Derivative coefficient.               |

## `config`
*Same args as \_\_init\_\_*

Configure each property of the controller.
## `cycle`
Update the controller.
