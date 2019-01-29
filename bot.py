import curses
from gpiozero import CamJamKitRobot
from time import sleep
from pprint import pprint
import unicornhat as unicorn

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height = unicorn.get_shape()

robot = CamJamKitRobot()

debug = False

execfile("unicorn.py")

actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.right,
    curses.KEY_RIGHT: robot.left,
    49: dosmile,
    50: dowink,
    51: dofight,
    121: doyes,
    110: dono,
    32: doblank,
    111: dowhoa,
    47: dowhat,
    104: dohi,
    92: gocrazy,
    114: rainbow,
    116: thinking
}

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY DOWN
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY UP
            robot.stop()

curses.wrapper(main)
