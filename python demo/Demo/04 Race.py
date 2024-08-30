import event, time, cyberpi, mbot2, mbuild
import time
# initialize variables
base_power = 0
kp = 0
left_power = 0
right_power = 0

@event.start
def on_start():
  global base_power, kp, left_power, right_power
  cyberpi.console.println("A：stop line-following")
  cyberpi.console.println("B：start line-following")
  cyberpi.console.println("Press joystick：check the color recognition results")

@event.is_press('a')
def is_btn_press():
  global base_power, kp, left_power, right_power
  cyberpi.stop_other()
  mbot2.drive_power(0, 0)

@event.is_press('b')
def is_btn_press1():
  global base_power, kp, left_power, right_power
  cyberpi.stop_other()
  base_power = 45
  kp = 0.7
  while True:
    left_power = -1 * ((base_power + kp * mbuild.quad_rgb_sensor.get_offset_track(1)))
    right_power = (base_power - kp * mbuild.quad_rgb_sensor.get_offset_track(1))
    mbot2.drive_power(right_power, left_power)
    if mbuild.quad_rgb_sensor.is_color("white","R1",1):
      cyberpi.led.show('white white white white white')

    if mbuild.quad_rgb_sensor.is_color("red","R1",1):
      cyberpi.led.show('red red red red red')

    if mbuild.quad_rgb_sensor.is_color("yellow","R1",1):
      cyberpi.led.show('yellow yellow yellow yellow yellow')

    if mbuild.quad_rgb_sensor.is_color("green","R1",1):
      cyberpi.led.show('green green green green green')

    if mbuild.quad_rgb_sensor.is_color("cyan","R1",1):
      cyberpi.led.show('cyan cyan cyan cyan cyan')

    if mbuild.quad_rgb_sensor.is_color("blue","R1",1):
      cyberpi.led.show('blue blue blue blue blue')

    if mbuild.quad_rgb_sensor.is_color("purple","R1",1):
      cyberpi.led.show('purple purple purple purple purple')

    if mbuild.quad_rgb_sensor.is_color("black","R1",1):
      cyberpi.led.show('black black black black black')

@event.is_press('middle')
def is_joy_press():
  global base_power, kp, left_power, right_power
  # The recognition color is set to appear after the key because it
  # takes a certain amount of time to print the text, which will block
  # the current thread and cause the patrolling effect to decline.
  cyberpi.stop_other()
  mbot2.drive_power(0, 0)
  while True:
    # There may be some error in color recognition, because the color card material based on factory calibration does not cover all materials.
    #
    # If you need custom color determination, you can consider based on the returned "object R/G/B value" parameter implementation.
    cyberpi.console.println(mbuild.quad_rgb_sensor.get_color_sta("R2",1))
    time.sleep(0.1)
