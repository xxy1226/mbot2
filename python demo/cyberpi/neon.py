import math, random, cyberpi
from time import sleep

cyberpi.led.show("r g b y c")
count = 0
while True:
  cyberpi.led.set_bri(math.sin(count / 4) * 50 + 52)
  cyberpi.led.move(1)
  count += 1
  sleep(0.1)