# generated by mBlock5 for CyberPi
# codes make you happy

import event, time, cyberpi, mbot2, mbuild
import time
# initialize variables
TL = 0
FW = 0
moving = 0

@event.receive("move")
def on_receive():
    global TL, FW, moving
    mbot2.forward(20, 1)
    moving = 0

@event.receive("edge")
def on_receive1():
    global TL, FW, moving
    while not moving == 0:
      # DO SOMETHING
      pass

    cyberpi.audio.play('angry')
    mbuild.ultrasonic2.set_bri(0, "all", 1)
    cyberpi.led.on(208, 2, 27, "all")
    time.sleep(0.5)
    cyberpi.led.on(0, 0, 0, "all")
    cyberpi.led.off("all")
    if TL == 0:
      mbot2.turn(-180)
      TL = 1

    else:
      mbot2.turn(180)
      TL = 0

    mbot2.forward(40, 1)
    time.sleep(0.3)
    mbuild.ultrasonic2.add_bri(100, "all", 1)
    cyberpi.led.on(208, 2, 27, "all")
    time.sleep(0.5)
    cyberpi.led.on(0, 0, 0, "all")
    cyberpi.led.off("all")

