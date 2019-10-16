#Importing matplotlib.pyplot for visualisation
import matplotlib.pyplot
#Import animation library
import matplotlib.animation 
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
#Adding variable neighbourhood
neighbourhood=20


#Creating agents, imported from the agentframwork
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

#Creating a figure using matplotlib    
fig = matplotlib.pyplot.figure(figsize=(7, 7))

#Within the animation, we are plotting the environment and agent interacting 
carry_on = True

def update(frame_number):
    fig.clear()   
    global carry_on
    
    matplotlib.pyplot.xlim(0,300)
    matplotlib.pyplot.ylim(0,300)
    matplotlib.pyplot.imshow(environment)
 
#Shuffling the order in which agents are processed each movement
    random.shuffle(agents)
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    
#Colouring the agents(sheep)in black
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'black')
               
#Generate a random stopping condition   
    if random.random() < 0.001:
        carry_on = False
        print("random stopping condition")
          
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 100) & (carry_on):
        yield a			
        a = a + 1

#Plotting the animation
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
