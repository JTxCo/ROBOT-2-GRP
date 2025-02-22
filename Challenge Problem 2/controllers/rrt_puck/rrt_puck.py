"""rrt_puck controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor

def monte_carlo_propagate():
    # Initialize success to True
    #Set both the motors to velocity control mode
    #Set the desired duration of random motion (in seconds)
    #Enable the proximity sensors on the e-puck
    #Assign a random velocity to the left motor
    #Assign a random velocity to the right motor
    #Sample a random time duration and while the duration is not reached, execute the randomly sampled velocities on the robt
    #Perform collision checking at each iteration. Return False if collision occurs.
    #If no collision occurs, stop the robot, return success and return the velocities.
    


#main
#Initialize the robot, obtain variables for the emitter and receiver on the robot.
#Set emitter and receiver channels
#In a while loop:
	#Check if receiver has received data
	#If data asks for monte carlo propagation:
		#perform monte carlo propagation from the robot's current state until 5 successful propagations are obtained.
		#Use the emmiter to send the following after each propagation attempt: success of propagation (boolean), left motor velocity and right motor velocity.
        #If data indicates that the goal has been reached, then write code to find the final path and replay the final set of actions on the robot all the way from its initial state to the goal state
