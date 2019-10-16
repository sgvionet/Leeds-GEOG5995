# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importing random library
import random

#Assigning values to y0 and x0
#idem for y1 and x1

y0 = 0
y1 = 4
x0 = 0
x1 = 3

#Using random function to alter y0 and then x0 randomly 
#We assign the command separately as python cannot work so that 
#one increases and the other decreases simultaneously 
#idem for y1, x1

if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    
if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
    
if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1

#Calculate distance between ste of two coordinates using Pythagora's formula
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer) 
    
#Print values to check if code works
print(y0, x0)
print(y1, x1)