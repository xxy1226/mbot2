import event, time, cyberpi, mbot2, mbuild
import time

cyberpi.driver.cloud_translate.TTS_URL = "{TTSURL}"
cyberpi.driver.cloud_translate.set_token("{ACCESSTOKEN}")

@event.start
def on_start():
    cyberpi.audio.set_vol(8)
    cyberpi.audio.set_tempo(150)
    cyberpi.audio.play_until('start')
    cyberpi.console.clear()
    cyberpi.console.set_font(12)
    # !!!!!!!!! Attention:
    #
    # This project needs to be connected to the Internet before it
    # run. Please use the parameters of this row of blocks as the
    # account and password of the WiFi router in your environment.
    cyberpi.wifi.connect("RRC-XXIA", "13588720")
    cyberpi.console.println("Connecting the network...")
    while not cyberpi.wifi.is_connect():
      # DO SOMETHING
      pass

    cyberpi.console.println("Connected network successfully!")
    time.sleep(0.5)
    cyberpi.console.clear()
    cyberpi.console.println("Hello, I'm mBot2 from Makeblock. ")
    # At present, TTS uses the service of Baidu, and its
    # execution speed will be greatly affected by the
    # network environment, presenting great fluctuations.
    cyberpi.cloud.tts("en", "Hello, I'm m Bot two from Make block. ")
    cyberpi.console.println("Now let me introduce myself!")
    cyberpi.cloud.tts("en", "Now let me introduce myself!")
    cyberpi.console.println("Firstly, My main controller is integrated with many advanced functions.")
    time.sleep(1.5)
    # cyberpi.cloud.tts("en", "Firstly, My main controller is integrated with many advanced functions.")
    cyberpi.console.println("It includes a full-color display, speakers and WiFi, Bluetooth, motion sensors, microphone and light sensors")
    time.sleep(1.5)
    # cyberpi.cloud.tts("en", "It includes a full-color display, speakers and WiFi, Bluetooth, motion sensors, microphone and light sensors")
    cyberpi.console.println("This makes me omnipotent in AIOT teaching")
    time.sleep(1.5)
    # cyberpi.cloud.tts("en", "This makes me omnipotent in AIOT teaching")
    cyberpi.console.println("The second is my powertrain, the new coded motor that allows me to move accurately.")
    time.sleep(1.5)
    # cyberpi.cloud.tts("en", "The second is my powertrain, the new coded motor that allows me to move accurately.")
    precision_move_demo()
    cyberpi.console.println("And finally, the new generation of electronics module, m Build, gives me super functionality")
    time.sleep(1.5)
    # cyberpi.cloud.tts("en", "And finally, the new generation of electronics module, m Build, gives me super functionality")
    cyberpi.broadcast("message 1")
    cyberpi.console.println("Find out more about me by downloading mblock!")
    time.sleep(1.5)
    # cyberpi.cloud.tts("en", "Find out more about me by downloading m block!")
    cyberpi.console.clear()
    cyberpi.console.println("Joystick down to switch read values")

@event.receive("message 1")
def on_receive():
    mBuild_modules_demo()

def precision_move_demo():
    mbot2.straight(3)
    mbot2.straight(-3)
    mbot2.turn(-90)
    mbot2.turn(90)

def sensor_values_display():
    while True:
      while not cyberpi.controller.is_press('down'):
        cyberpi.display.show_label(str('Distance:') + str(str(mbuild.ultrasonic2.get(1)) + str('cm')), 16, "center")
        time.sleep(0.1)

      time.sleep(0.5)
      while not cyberpi.controller.is_press('down'):
        cyberpi.display.show_label(str("Color's RGB value:") + str(mbuild.quad_rgb_sensor.get_color_sta("R2",1)), 16, "center")
        time.sleep(0.1)

      time.sleep(0.5)
      while not cyberpi.controller.is_press('down'):
        cyberpi.display.show_label(str('Line offset position:') + str(mbuild.quad_rgb_sensor.get_offset_track(1)), 16, "center")
        time.sleep(0.1)

      time.sleep(0.5)
      while not cyberpi.controller.is_press('down'):
        cyberpi.display.show_label(str('Light intensity:') + str(cyberpi.get_bri()), 16, "center")
        time.sleep(0.1)

      time.sleep(0.5)
      while not cyberpi.controller.is_press('down'):
        cyberpi.display.show_label(str('Loudness:') + str(cyberpi.get_loudness("maximum")), 16, "center")
        time.sleep(0.1)

      time.sleep(0.5)
      while not cyberpi.controller.is_press('down'):
        cyberpi.display.show_label(str('Battery:') + str(cyberpi.get_battery()), 16, "center")
        time.sleep(0.1)

      time.sleep(0.5)
      while not cyberpi.controller.is_press('down'):
        cyberpi.display.show_label(str('Shaking strength:') + str(cyberpi.get_shakeval()), 16, "center")
        time.sleep(0.1)
        
      time.sleep(0.5)

def mBuild_modules_demo():
    cyberpi.led.show('red red red red red')
    mbuild.quad_rgb_sensor.set_led("red", 1)
    time.sleep(0.2)
    cyberpi.led.show('green green green green green')
    mbuild.quad_rgb_sensor.set_led("green", 1)
    time.sleep(0.2)
    cyberpi.led.show('yellow yellow yellow yellow yellow')
    mbuild.quad_rgb_sensor.set_led("yellow", 1)
    time.sleep(0.2)
    cyberpi.led.show('cyan cyan cyan cyan cyan')
    mbuild.quad_rgb_sensor.set_led("cyan", 1)
    time.sleep(0.2)
    cyberpi.led.show('purple purple purple purple purple')
    mbuild.quad_rgb_sensor.set_led("purple", 1)
    time.sleep(0.2)
    cyberpi.led.show('white white white white white')
    mbuild.quad_rgb_sensor.set_led("white", 1)
    time.sleep(0.2)
    cyberpi.led.show('blue blue blue blue blue')
    mbuild.quad_rgb_sensor.set_led("blue", 1)
    time.sleep(0.2)
    cyberpi.console.clear()
    sensor_values_display()

