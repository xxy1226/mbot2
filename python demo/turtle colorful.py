from turtle import *

colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
length = len(colors)
speed(20)
# print(360 // length if 360 % length != 0 else 360 // length -1)
for x in range(360):
    pencolor(colors[x % len(colors)])
    width(x / 100 + 1)
    forward(x)
    left(360 // length if 360 % length != 0 else 360 // length -1)
hideturtle()
done()