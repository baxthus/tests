from turtle import *
import time
speed(15) # Change the execution velocity
color('cyan')
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
time.sleep(2.5)