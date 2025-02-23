'''
    Joel Carlson and Saravana Prakash


'''


# You may need to import some classes of the controller module. Ex:
from controller import Robot, Motor, DistanceSensor, Emitter, Receiverr, Supervisor

#Create a class to represent a Node, which consists of position, parent Node and action(velocity of the motors)
class Node:
    def __init__(self, position, parent, action):
        self.position = position
        self.parent = parent
        self.action = action #Velocity of the motors




def randomly_sample_state():
    #Using 50% goal biasing, sample a state within the arena and return the state







def main():
    # Initialize the Webots Supervisor
    supervisor = Supervisor()
    
    #Initialize the supervisor node, the graph and create a node class object to represent the initial state of the robot, which is also the only node in the tree
    
    
    #Create variables for the e-puck robot, the emmiter and the receiver
    robot = supervisor.getFromDef("EPUCK")
    emitter = robot.getDevice("emitter")
    receiver = robot.getDevice("receiver")
    
    
    #Set channels for the emitter reciever pair
    emitter.setChannel(1)
    receiver.setChannel(2)
    # Time stop at intervals to check for new messages could be set here TBD
    # receiver.enable(TIME_STEP)
    
    #Set the robot's motors to velocity control mode
    left_motor = robot.getDevice("left wheel motor")
    right_motor = robot.getDevice("right wheel motor")
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
     
    
     
    # Run the simulation step by step in a while loop:
    	#Randomly sample a state
    	#Find the nearest node in the tree to the randomly sampled state
    	#Teleport the robot to this nearest node
    	#Use the emitter to request the puck's controller to perform monte carlo propagations
        #While 5 succcesfull propagations are yet to be executed:
            #Use the reciever to obtain the success and the velocity values
            #If success if false, collision has occured. Move on.
            #Else, obtain the final position of the robot and store it.
            #Teleport the puck back to the nearest node
        #Compare the final positions with the randomly sampled state and pick the nearest one.
        #Add it to the tree
        #Is the new state close enough to the goal:
        	#GOAL REACHED! 
        	#Write code to gather the final set of actions and use emitter to transmit data for replaying
            
if __name__ == "__main__":
    main()
