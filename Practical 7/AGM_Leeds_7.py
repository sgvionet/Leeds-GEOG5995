#Importing matplotlib.pyplot for visualisation
import matplotlib.pyplot
#Importing class Agent from agentframework.py
import agentframework
#Importing csv library to read the in.txt file
import csv
#Importing random library 
import random


#Using reading command("r") and csv library, we are now reading the text file 
#as a csv file
f = open("in.txt", "r")
reader = csv.reader(f)
#Create a list for environment
environment=[]


#Using a for-loop, we are making each row a list in the environment,
#with each row being filled with values
for line in f:
    rowlist = [] #Creating an empty rowlist
    line_split = line.split(',') #Splitting the numbers(values) in the csv file
    for value in line_split: #Using for-loop, we are appending values to the created rowlist
        rowlist.append(int(value))
    environment.append(rowlist) #Appending the rowlist to the environment (data) list


#Create a list for agents
agents = []
#Generating the number of agents
num_of_agents = 10
#Generating number of iterations(movements)
num_of_iterations = 100
#Adding variable neighbourhood
neighbourhood=20

#Using the random library, we are shuffling the order in which agents are processed each movement
random.shuffle(agents)

#Using the for-loop, we are getting agents to interact with the environment, 
#imported from the recently created class
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    


#Using for-loops, we are generating a number of iterations(movements - 100) for each agent
#imported from the class
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
     
#Plotting coordinates and environment
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()