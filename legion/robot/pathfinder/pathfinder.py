from legion.model.omnidirectional import Omnidirectional
from legion.control.pid import PID
from board.arietta.pin.digital import Digital
from board.arietta.pin.pwm import PWM
from math import fabs


class Pathfinder(Omnidirectional):

    def __init__(self, arm=10,
                 pid_x=PID(), pid_y=PID(), pid_w=PID(),
                 pid_0=PID(), pid_1=PID(), pid_2=PID()):
        self.motor_0_direction = Digital(33)
        self.motor_0_speed = PWM(0)
        self.motor_1_direction = Digital(35)
        self.motor_1_speed = PWM(1)
        self.motor_2_direction = Digital(37)
        self.motor_2_speed = PWM(2)
        super(Pathfinder, self).__init__(arm,
                                         pid_x, pid_y, pid_w,
                                         pid_0, pid_1, pid_2)

    def open_move(self, x, y, z):
        super(Pathfinder, self).open_move(x, y, z)
        _motor_0 = self._speed.motor0_out
        _motor_1 = self._speed.motor1_out
        _motor_2 = self._speed.motor2_out
        _max = max([fabs(self._speed.motor0_out),
                    fabs(self._speed.motor1_out),
                    fabs(self._speed.motor2_out)])
        if _max > 1:
            _motor_0 /= _max
            _motor_1 /= _max
            _motor_2 /= _max
        _d, _spd = self._parse_speed(_motor_0)
        self.motor_0_direction = _d
        self.motor_0_speed.duty_cycle = self.motor_0_direction.period * _spd

        _d, _spd = self._parse_speed(_motor_1)
        self.motor_1_direction = _d
        self.motor_1_speed.duty_cycle = self.motor_0_direction.period * _spd

        _d, _spd = self._parse_speed(_motor_2)
        self.motor_2_direction = _d
        self.motor_2_speed.duty_cycle = self.motor_0_direction.period * _spd

    def _parse_speed(self, speed):
        if speed == 0:
            return 0, 0
        elif speed > 0:
            return 1, speed
        elif speed < 0:
            return 1, 1-speed
