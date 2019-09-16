# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:08:08 2019

@author: gyvi
"""
#Import relevant libraries
import random
#Set up variables
y0 = random.randint(0,99)
x0 = random.randint(0,99)

#Move y0 randomly
if random.random() < 0.5: 
    y0 = y0 + 1 
else:
    y0 = y0 - 1
#Move x0 randomly
if random.random() <0.5:
    x0 = x0 + 1
else: 
    x0 = x0 - 1
#Move y0 randomly
if random.random() < 0.5: 
    y0 = y0 + 1 
else:
    y0 = y0 - 1
#Move x0 randomly
if random.random() <0.5:
    x0 = x0 + 1
else: 
    x0 = x0 - 1
    





#Set up variables
y1 = random.randint(0,99)
x1 = random.randint(0,99)

#Move y1 randomly
if random.random() < 0.5: 
    y1 = y1 + 1 
else:
    y1 = y1 - 1
#Move x1 randomly
if random.random() <0.5:
    x1 = x1 + 1
else: 
    x1 = x1 - 1
#Move y1 randomly  
if random.random() < 0.5: 
    y1 = y1 + 1 
else:
    y1 = y1 - 1
#Move x1 randomnly 
if random.random() <0.5:
    x1 = x1 + 1
else: 
    x1 = x1 - 1

print(x0, y0)
print(x1, y1)

#Pythagorean distance between y0,x0 and y1,x1
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
#print the answer
print (answer)
    
    
    
    