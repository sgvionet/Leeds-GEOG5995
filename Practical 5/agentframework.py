# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:35:11 2019

@author: sgvionet
"""
#Importing random library
import random 

#Creating a class called Agent
class Agent():
    #Generating agents inside the class using __init__ method and label self
    def __init__(self):
        self.y = random.randint(0,100)
        self.x = random.randint(0,100)
    #Generating movement for agents using the label self
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1)%100
        else:
            self.y = (self.y - 1)%100
        if random.random() < 0.5:
            self.x = (self.x + 1)%100
        else:
            self.x = (self.y - 1)%100