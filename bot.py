import curses
from gpiozero import CamJamKitRobot
from time import sleep
from pprint import pprint
import unicornhat as unicorn

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
u_width,u_height = unicorn.get_shape()

robot = CamJamKitRobot()

debug = False

execfile("unicorn.py")


actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.right,
    curses.KEY_RIGHT: robot.left,
    49: dosmile, #1
    50: dowink,  #2
    51: dofight, #3
    52: gocrazy, #4
    53: rainbow, #5
    54: doswirl, #6
    55: dochecker, #7
    56: doblues_and_twos, #8
    57: dorainbow_search, #9
    48: dotunnel, #0
    121: doyes, #y
    110: dono, #n
    32: doblank, #[space bar]
    111: dowhoa, #o
    47: dowhat, #/
    104: dohi #h
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
