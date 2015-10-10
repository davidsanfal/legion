from legion.errors import LegionaryException


class Legionary(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self._speed_x = 0
        self._speed_y = 0
        self._speed_w = 0

    @property
    def speed_x(self):
        return self._speed_x

    @property
    def speed_y(self):
        return self._speed_y

    @property
    def speed_w(self):
        return self._speed_w

    @speed_x.setter
    def speed_x(self, speed):
        self._speed_x = speed
        self._engines_speed()

    @speed_y.setter
    def speed_y(self, speed):
        self._speed_y = speed
        self._engines_speed()

    @speed_w.setter
    def speed_w(self, speed):
        self._speed_w = speed
        self._engines_speed()

    @property
    def speeds(self):
        return [self.speed_x,
                self.speed_y,
                self.speed_w]

    @speeds.setter
    def speeds(self, speeds):
        if len(speeds) == 3:
            self._speed_x = speeds[0]
            self._speed_y = speeds[1]
            self._speed_w = speeds[2]
            self._engines_speed()

    def _engines_speed(self):
        raise LegionaryException()
