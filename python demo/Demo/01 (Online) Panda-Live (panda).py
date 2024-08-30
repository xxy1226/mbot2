from mblock import event
import time
# initialize variables
TL,FW,moving

@event.greenflag
def on_greenflag():
  sprite.glide(0, -40, 1)

@event.keypressed('space')
def on_keypressed():
  while not sprite.get_variable('moving') == 0:
    # DO SOMETHING
    pass

  sprite.set_variable('moving', 1)
  sprite.broadcast(str('move'))

@event.received('move')
def on_received():
  if sprite.get_variable('FW') == 0:
    sprite.forward(50)
    sprite.set_costume('costume2')
    time.sleep(0.2)
    sprite.forward(50)
    sprite.set_costume('costume1')

  else:
    sprite.forward(-50)
    sprite.set_costume('costume4')
    time.sleep(0.2)
    sprite.forward(-50)
    sprite.set_costume('costume3')

  while True:
    if sprite.touching('edge'):
      sprite.broadcast(str('edge'))
      if sprite.get_variable('FW') == 0:
        sprite.set_costume('costume3')
        sprite.set_variable('FW', 1)

      else:
        sprite.set_costume('costume1')
        sprite.set_variable('FW', 0)

      sprite.glide(0, -40, 1)

    time.sleep(3)

