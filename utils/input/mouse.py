from typing import NoReturn
from easing_functions import QuadEaseInOut
from pynput.mouse import Button, Controller
from time import sleep

class SmoothMouse:
    def __init__(self):
        self.controller = Controller()

    def move_to(self, targetX: int, targetY: int, duration: float = 300.0):
        actualX, actualY = self.controller.position
        easeX = QuadEaseInOut(actualX, targetX, 1.0)
        easeY = QuadEaseInOut(actualY, targetY, 1.0)

        if duration == 0:
            self.controller.position = targetX, targetY
        elif duration > 0:
            time = 0
            interval = 1 / duration
            while time < 1.0:
                time += interval
                self.controller.position = (int(easeX.ease(time)), int(easeY.ease(time)))
                sleep(0.001)