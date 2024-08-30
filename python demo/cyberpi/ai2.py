from time import sleep
import cyberpi, event

cyberpi.speech.set_recognition_address(url = "http://msapi.passport3.makeblock.com/ms/bing_speech/interactive")

cyberpi.cloud.setkey("34d54aef8ede48379c5bf22c19aea159")

cyberpi.wifi.connect("RRC-XXIA", "13588720")

while not cyberpi.wifi.is_connected():
    pass
cyberpi.led.on(100, 100, 0)

@event.is_press('a')
def is_btn_press():
  cyberpi.console.clear()
  cyberpi.led.on(100, 0, 0)
  cyberpi.cloud.listen("english", 2)
  cyberpi.console.print(cyberpi.cloud.listen_result())
  cyberpi.led.on(0, 0, 0)