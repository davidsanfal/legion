from legion.errors import LegionaryException
import time


class Point(object):
    def __init__(self, x=0, y=0, w=0):
        self.x = x
        self.y = y
        self.w = w


class Speed(object):
    def __init__(self):
        self.x_in = 0
        self.x = 0
        self.x_out = 0
        self.y_in = 0
        self.y = 0
        self.y_out = 0
        self.w_in = 0
        self.w = 0
        self.w_out = 0


class Legionary(object):

    def __init__(self, pid_x, pid_y, pid_w):
        self.speed = Speed
        self.position = Point(0, 0, 0)
        self.destiny = Point(0, 0, 0)
        self._pid_x = pid_x
        self._pid_y = pid_y
        self._pid_w = pid_w
        self.last_time = time.time() * 1000

    def go_to(self, x, y, w):
        raise LegionaryException()
