## MissionBase Class

The `MissionBase` class is a base class for all missions. It has the following methods:

* `setStart()`: This method is called once when the mission is started.
* `run()`: This method starts the mission.
* `done()`: This method is called once when the mission is finished.
* `stop()`: This method stops the mission.
* `isActive()`: This method returns `True` if the mission is active, and `False` otherwise.
* `isActiveWithRaise()`: This method returns `True` if the mission is active, and raises a `MissionEndedException` if it is not.
* `interrupt()`: This method interrupts the mission.
* `resume()`: This method resumes the mission.
* `runAction()`: This method runs an action.
* `getIsInterrupted()`: This method returns `True` if the mission is interrupted, and `False` otherwise.

