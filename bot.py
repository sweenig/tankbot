import curses
from time import sleep
debug = False
import unicorn
unicorn.showface(unicorn.faces["hi"])
from gpiozero import CamJamKitRobot
robot = CamJamKitRobot()
motoractions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.right,
    curses.KEY_RIGHT: robot.left
}
actions = {}
actions.update(motoractions)
actions.update(unicorn.actions)
unicorn.showface(unicorn.faces["smile"])
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
