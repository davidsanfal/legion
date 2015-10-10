from math import sin, cos, pi
from legion.legionary.legionary import Legionary


class Omnidirectional(Legionary):

    def __init__(self):
        self.arm = 10
        self.speed_0 = 0
        self.speed_1 = 0
        self.speed_2 = 0
        super(Omnidirectional, self).__init__()

    def _engines_speed(self):
        self.speed_0 = -self._speed_x*sin(pi/3) + (self._speed_y*cos(pi/3)) + self.arm*self._speed_w
        self.speed_1 = -self._speed_y + self.arm*self._speed_w
        self.speed_2 = self._speed_x*sin(pi/3) + (self._speed_y*cos(pi/3)) + self.arm*self._speed_w

    @property
    def real_speed_0(self):
        return self.speed_0  # read encoder

    @property
    def real_speed_1(self):
        return self.speed_1  # read encoder

    @property
    def real_speed_2(self):
        return self.speed_2  # read encoder

    @property
    def real_speed_x(self):
        return ((self.real_speed_2 - self.real_speed_0)/sin(pi/3))/2

    @property
    def real_speed_y(self):
        return ((self.real_speed_2 + self.real_speed_0)/2 - self.real_speed_1)/(1 + cos(pi/3))

    @property
    def real_speed_w(self):
        return (self.real_speed_1 + self.real_speed_y)/self.arm

    @property
    def real_speed(self):
        return [self.real_speed_x, self.real_speed_y, self.real_speed_w]
