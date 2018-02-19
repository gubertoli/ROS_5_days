Exercice 4.13: Create Package with Action Server that moves the Ardrone in the air, making a square

a) Create a package with an action server that makes the drone move in a square when called. 

b) Call the action server through the topics and observe the result and feedback.

- The size of the side of the square should be specified in the goal message as an integer.
- The feedback should publish the current side (as a number) the robot is at while doing the square.
- The result should publish the total number of seconds it took the drone to do the square
- Use the Test.action message for that action server. Use the shell command locate Test.action to find where that message is defined. Then, analyze the different fields of the msg in order to learn how to use it in your action server.