import event, time, cyberpi, mbuild, mbot2, random
import time

@event.start
def on_start():
    cyberpi.console.set_font(12)
    cyberpi.console.println("Press “B” to start obstacle avoidance")
    cyberpi.console.println("Press “A” to restart")
    while not cyberpi.controller.is_press('b'):
      pass

    while True:
      if mbuild.ultrasonic2.get(1) > 8:
        mbot2.forward(60)

      else:
        if random.randint(1, 2) == 1:
          mbot2.turn_left(35)
          time.sleep(1)

        else:
          mbot2.turn_right(35)
          time.sleep(1)

@event.is_press('a')
def is_btn_press():
    cyberpi.restart()

