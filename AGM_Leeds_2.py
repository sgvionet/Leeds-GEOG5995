# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importing random library
import random
#Import operator library to use for max() function
import operator
#Importing matplotlib.pyplot for visualisation
import matplotlib.pyplot


#Create a list for agents
agents = []

#Appending values to appended agents, remembering that y0 is the first and x0 the second
agents.append([random.randint(0,100), random.randint(0,100)])

#Appending values to appended agents, remembering that y1 is the first and x1 the second
agents.append([random.randint(0,100), random.randint(0,100)])

#Print values to check if code works
print(agents)



#We replace the y0 and x0 values with the appended agents (where each agent is appended agents[0]),
#and the second dimension represents the two coordinates ([0] = y; [1] = x) in order to generate one movement


if random.random() < 0.5:
    agents[0][0] =  agents[0][0] + 1
else:
    agents[0][0] =  agents[0][0] - 1
    
if random.random() < 0.5:
    agents[0][1] =  agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1
    

#We replace the y1 and x1 values with the appended agents (where each agent is appended agents[1]), 
#where the second dimension represents the two coordinates ([0] = y; [1] = x) in order to generate one movement
  
  
if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1
    
if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1

#Calculate distance between set of two coordinates using Pythagora's formula 
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
#print(answer) 

#Printing out the max value for the x direction using operator.itemgetter(1)
#where 1 is the second element as a result of indexing (see explanation line 40)
#We can print in the y direction by simply executing the following line:
#print(max(agents))
print(max(agents, key=operator.itemgetter(1)))

#Plotting coordinates so that the most easterly point is red
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()
