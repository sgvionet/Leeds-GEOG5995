#Importing random library
import random 

#Creating a class called Agent
#Generating agents and environment inside the class 
class Agent():
    def __init__(self, environment, agents):
        self.y = random.randint(0,300)
        self.x = random.randint(0,300)
        self.environment = environment
        self.store = 0
        self.agents = agents
        self.store = 0
#Generating movement for agents
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
    
#Making agents eat units of the environment
    def eat(self):
        if self.environment[self.y][self.x] > 100:
            self.environment[self.y][self.x] -= 100
            self.store += 100
#Moving the distance between agents calculation into the class
    def distance_between(self, agents_row_b):
        return (((self.x - agents_row_b.x)**2) +
                ((self.y - agents_row_b.y)**2))**0.5
#Creating a function sharing with neighbours inside the class,
#in order to make the agents communicate with each other
    def share_with_neighbours(self, neighbourhood):
        for i in range(len(self.agents)):
            distance = self.distance_between(self.agents[i])
            if distance <= neighbourhood:
                total = self.store + self.agents[i].store 
                average = total/2
                self.store = average
                self.agents[i].store = average
                