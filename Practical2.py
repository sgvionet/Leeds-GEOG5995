# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:08:08 2019

@author: gyvi
"""
#Import relevant libraries
import random
import operator
import matplotlib.pyplot


agents = []
#Set up variables
y0 = random.randint(0,99)
x0 = random.randint(0,99)
#Append variables
agents.append([random.randint(0,99),random.randint(0,99)])

#Move y0 randomly
if random.random() < 0.5: 
    y0 = y0 + 1 
else:
    y0 = y0 - 1
#Move agents randomly (x0)
if random.random() <0.5:
    agents [0][1] = agents [0][1] + 1
else: 
    agents [0][1] = agents [0][1] - 1
#Move agents randomly
if random.random() < 0.5: 
    agents [0][0] = agents [0][0] + 1 
else:
    agents [0][0] = agents [0][0] - 1
#Move agents randomly
if random.random() <0.5:
    agents [0][1] = agents [0][1] + 1
else: 
    agents [0][1] = agents [0][1] - 1
    





#Set up variables
y1 = random.randint(0,99)
x1 = random.randint(0,99)

#Appending agents
agents.append ([random.randint(0,99), random.randint(0,99)])

#Move y1 randomly
if random.random() < 0.5: 
    y1 = y1 + 1 
else:
    y1 = y1 - 1
#Move agents randomly (x1)
if random.random() <0.5:
    agents [0][1] = agents [0][1] + 1
else: 
    agents [0][1] = agents [0][1] - 1
#Move agents randomly
if random.random() < 0.5: 
    agents [0][0] = agents [0][0] + 1 
else:
    agents [0][0] = agents [0][0] - 1
#Move agents randomly
if random.random() <0.5:
    agents [0][1] = agents [0][1] + 1
else: 
    agents [0][1] = agents [0][1] - 1



#Pythagorean distance between y0,x0 and y1,x1
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
#print the answer

print(agents)
#Printing the maximum value for x
print(max(agents, key=operator.itemgetter(1)))

#Plotting the values onto figure
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.show()
    
    
    