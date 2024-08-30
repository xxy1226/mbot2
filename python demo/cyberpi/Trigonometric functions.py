import os, sys, random, math, cyberpi
from time import sleep
print("Ready!")

count = 0
while True:
  val = int(math.sin(count / 2) * 50 + 50)
  cyberpi.display.set_brush(0, 255, 0)
  cyberpi.linechart.add(int(val))
  
  val = int(math.cos(count / 2) * 50 + 50)
  cyberpi.display.set_brush(255, 255, 255)
  cyberpi.linechart.add(int(val))
  
  count += 1