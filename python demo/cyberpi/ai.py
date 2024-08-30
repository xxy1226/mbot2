from time import sleep
import cyberpi

# for upload mode
cyberpi.speech.set_recognition_address(url = "http://msapi.passport3.makeblock.com/ms/bing_speech/interactive")
# for online mode
# cyberpi.set_recognition_url()

cyberpi.cloud.setkey("34d54aef8ede48379c5bf22c19aea159")

cyberpi.wifi.connect("RRC-XXIA", "13588720")

while not cyberpi.wifi.is_connected():
    pass
cyberpi.console.clear()
cyberpi.led.on(100, 0, 0)
cyberpi.cloud.listen("english", 2)
cyberpi.console.print(cyberpi.cloud.listen_result())
cyberpi.led.on(0, 0, 0)

