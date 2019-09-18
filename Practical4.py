# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:08:08 2019

@author: gyvi
"""
#Import relevant libraries
import random
import operator
import matplotlib.pyplot


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
#Setting the limit for number of agents
num_of_agents = 10
#Setting the number of iterations (movements)
num_of_iterations = 100
agents = []
#Set up variables
y0 = random.randint(0,99)
x0 = random.randint(0,99)
#Create a for-loop for number of agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
#Create a for-loop for number of iterations (movements) for each agent  
for j in range(num_of_iterations):
    for i in range(num_of_agents):     
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

#Pythagorean distance between y0,x0 and y1,x1
#answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
#print(answer)
#print the agents
print(agents)
#Printing the maximum value for x
print(max(agents, key=operator.itemgetter(1)))
#Plotting the values onto figure
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

# test distance function
distance = distance_between(agents[0],agents[1])
print(distance)

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

    