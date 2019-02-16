from brightpi import *
brightPi = BrightPi()
brightPi.reset()
i = 0
WHITE = (1, 2, 3, 4)
IR = (5, 6, 7, 8)

def switch(bank, state): # This could help for example in a loop.
  brightPi.reset()
  brightPi.set_led_on_off(bank, state)

def cycle():
  global i
  if i % 3 == 0: switch(WHITE, 1)
  if i % 3 == 1: switch(IR, 1)
  if i % 3 == 2: brightPi.reset()
  i += 1

from subprocess import check_call
def shutdown(): check_call(['sudo','poweroff'])

from gpiozero import Button
button = Button(21, hold_time=2)
button.when_pressed = cycle
button.when_held = shutdown
