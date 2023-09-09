---
title: Actions
layout: default
---

# `Action`
The parent class of all actions.
## `done`
Run when the action is complete. Used for clean up.
## `isFinished`
Test if the action is complete.
## `start`
Run before starting the `update` loop. Used for setup.
## `update`
Run repeatedly until `isFinished` returns `True`.
# `ParallelAction`
|Argument  |Type    |Default|Description        |
|----------|--------|-------|-------------------|
|`*actions`|iterable|N/A    |Iterable of actions|

Run actions simultaneously.
## `done`
Clean up for all actions.
## `isFinished`
Check if all actions are complete.
## `start`
Start all actions.
## `update`
Update all actions.
# `SeriesAction`
|Argument  |Type    |Default|Description        |
|----------|--------|-------|-------------------|
|`*actions`|iterable|N/A    |Iterable of actions|

Run actions sequentially.
## `isFinished`
Check if all actions are complete.
## `update`
Update current action, or switch to next action.
# `SpinMotor`
|Argument        |Type    |Default    |Description                                      |
|----------------|--------|-----------|-------------------------------------------------|
|`speed`         |`Number`|N/A        |The speed of the motor.                          |
|`rotation_angle`|`Number`|N/A        |How far to rotate the motor in degrees.          |
|`then`          |`Stop`  |`Stop.HOLD`|How to stop the motor at the end of the rotation.|

Spin the attachment motor a certain angle.
## `done`
Remove the action from `Estimation.simpleEstimate`.
## `isFinished`
Check if the motor has finished its rotation.
## `start`
Start the rotation.
