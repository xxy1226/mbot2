# generated by mBlock5 for CyberPi
# codes make you happy

import event, time, cyberpi

@event.start
def on_start():
    cyberpi.display.set_brush(0, 255, 203)
    cyberpi.display.show_label("Hello World!", 16, "top_mid", index= 0)
    cyberpi.display.show_label("Hello World!", 16, "center", index= 1)
    cyberpi.display.show_label("Hello World!", 16, "bottom_mid", index= 2)

