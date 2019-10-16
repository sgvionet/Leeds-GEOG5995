# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importing random library
import random
#Importing matplotlib.pyplot for visualisation
import matplotlib.pyplot
#Import time library to check out how long operations are
import time

#Defining distance_betwen as a function in order to test distance between agents
def distance_between(agents_row_a, agents_row_b): 
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

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
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] =  (agents[i][0] + 1)%100
        else:
            agents[i][0] =  (agents[i][0] - 1)%100
        if random.random() < 0.5:
            agents[i][1] =  (agents[i][1] + 1)%100
        else:
            agents[i][1] = (agents[i][1] - 1)%100
    
#Starts timer
start = time.clock()

#Using for-loop to test agent against each agent
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)       
        print(distance)    

#Stops timer
end = time.clock()
#print duration of operation
print("time = " + str(end - start))
     
#Plotting coordinates 
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()


