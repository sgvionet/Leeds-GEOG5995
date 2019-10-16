# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importing random library
#import random
#Importing matplotlib.pyplot for visualisation
import matplotlib.pyplot
#Importing class Agent from agentframework.py
import agentframework

#Defining distance_betwen as a function in order to test distance between agents,
#imported from the recently created class
def distance_between(agents_row_a, agents_row_b): 
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

#Create a list for agents
agents = []
#Generating the number of agents
num_of_agents = 10
#Generating number of iterations(movements)
num_of_iterations = 100


#Using the for-loop, we are creating as many agents as we want, 
#imported from the recently created class
for i in range(num_of_agents):
    agents.append(agentframework.Agent())


#Using for-loops, we are generating a number of iterations(movements - 100) for each agent
#imported from the class
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        
    

#Using for-loop to test each agent against each agent
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)       
        print(distance)    

     
#Plotting coordinates 
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

#Printing agents within the class imported from agentframework
#in order to test them
a = agentframework.Agent()
print(a.y, a.x)
a.move()
print(a.y, a.x)


