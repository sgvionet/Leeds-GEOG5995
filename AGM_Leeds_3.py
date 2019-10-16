# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importing random library
import random
#Importing matplotlib.pyplot for visualisation
import matplotlib.pyplot

#Create a list for agents
agents = []
#Generating the number of agents
num_of_agents = 10
#Generating number of iterations(movements)
num_of_iterations = 100


#Using the for-loop, we are creating as many agents as we want
for i in range(num_of_agents):
    agents.append([random.randint(0,100), random.randint(0,100)])


#Using for-loops, we are generating a number of iterations(movements - 100) for each agent (10)
#If the plotsize is smaller than the randint for agent creation (line 22), 
#we can create a torus by using the modulus operator(%)
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] =  (agents[i][0] + 1)%50
        else:
            agents[i][0] =  (agents[i][0] - 1)%50
        if random.random() < 0.5:
            agents[i][1] =  (agents[i][1] + 1)%50
        else:
            agents[i][1] = (agents[i][1] - 1)%50
    
        
#Plotting coordinates 
matplotlib.pyplot.ylim(0, 50)
matplotlib.pyplot.xlim(0, 50)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()
