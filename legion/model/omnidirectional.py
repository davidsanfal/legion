from math import sin, cos, pi
import time


class Point():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0


class OmnidirectionalSpeed():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.m0 = 0
        self.m1 = 0
        self.m2 = 0


class Omnidirectional(object):

    def __init__(self, arm=10):
        self.arm = arm
        self.position = Point()
        self.speed = OmnidirectionalSpeed()

    @property
    def speeds(self):
        x = ((self.speed.m2 - self.speed.m0)/sin(pi/3))/2
        y = ((self.speed.m2 + self.speed.m0)/2 - self.speed.m1)/(1 + cos(pi/3))
        w = (self.speed.m1 + y)/self.arm

        return x, y, w

    @speeds.setter
    def speeds(self, spds):
        x, y, w = spds
        self.speed.m0 = -x*sin(pi/3) + (y*cos(pi/3)) + self.arm*w
        self.speed.m1 = -y + self.arm*w
        self.speed.m2 = x*sin(pi/3) + (y*cos(pi/3)) + self.arm*w
        self.speed.x, self.speed.y, self.speed.w = self.speeds

    def move(self):
        now = time.time() * 1000
        x, y, w = self.speeds
        self.position.x += x * (now - self.last_time)
        self.position.y += y * (now - self.last_time)
        self.position.w += w * (now - self.last_time)
        self.last_time = now
