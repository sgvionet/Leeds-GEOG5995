#Importing libraries for visualiation and GUI
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.animation 
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
#Using this command we are running the animation
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
#Using this command, we can stop the aniation at any time
def quit():
    global root
    root.destroy()  

#Using tkinter, python creates a window 'root' entitled Agent-based modelling, where it plots and runs the animation
#The window will also hav a drop down menu bar which will have two commands: run and quit the model
root = tkinter.Tk()
root.wm_title("Agent-based Modelling")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="Quit model", command=quit)


tkinter.mainloop()

