#Importing random library
import random 

#Creating a class called Agent
#Generating agents and environment inside the class 
class Agent():
    def __init__(self, environment):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.environment = environment
        self.store = 0
#Generating movement for agents
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
    
#Making agents eat units of the environment
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10