from math import sin, cos, pi
from legion.model.legionary import Legionary
from legion.control.pid import PID
import time


class OmnidirectionalSpeed(object):
    def __init__(self):
        self.motor0_in = 0
        self.motor0 = 0
        self.motor0_out = 0
        self.motor1_in = 0
        self.motor1 = 0
        self.motor1_out = 0
        self.motor2_in = 0
        self.motor2 = 0
        self.motor2_out = 0


class Omnidirectional(Legionary):

    def __init__(self, arm=10,
                 pid_x=PID(), pid_y=PID(), pid_w=PID(),
                 pid_0=PID(), pid_1=PID(), pid_2=PID()):
        self.arm = arm
        self._speed = OmnidirectionalSpeed()
        self._pid_0 = pid_0
        self._pid_1 = pid_1
        self._pid_2 = pid_2
        super(Omnidirectional, self).__init__(pid_x, pid_y, pid_w)

    def calculate_motor_in_speeds(self):
        self._speed.motor0_in = -self.speed.x_out*sin(pi/3) + (self.speed.y_out*cos(pi/3)) + self.arm*self.speed.w_out
        self._speed.motor1_in = -self.speed.y_out + self.arm*self.speed.w_out
        self._speed.motor2_in = self.speed.x_out*sin(pi/3) + (self.speed.y_out*cos(pi/3)) + self.arm*self.speed.w_out

    def read_motor_speeds(self):
        self._speed.motor0 = -self.speed.x_in*sin(pi/3) + (self.speed.y_in*cos(pi/3)) + self.arm*self.speed.w_in
        self._speed.motor1 = -self.speed.y_in + self.arm*self.speed.w_in
        self._speed.motor2 = self.speed.x_in*sin(pi/3) + (self.speed.y_in*cos(pi/3)) + self.arm*self.speed.w_in

    def read_robot_speeds(self):
        self.read_motor_speeds()
        self.speed.x = ((self._speed.motor2 - self._speed.motor0)/sin(pi/3))/2
        self.speed.y = ((self._speed.motor2 + self._speed.motor0)/2 - self._speed.motor1)/(1 + cos(pi/3))
        self.speed.w = (self._speed.motor1 + self.speed.y)/self.arm

    def go_to(self, x, y, w):
        self.destiny.x = x
        self.destiny.y = y
        self.destiny.w = w

    def move(self):
        now = time.time() * 1000
        self.read_robot_speeds()
        self.position.x = self.speed.x * (now - self.last_time)
        self.position.y = self.speed.y * (now - self.last_time)
        self.position.w = self.speed.w * (now - self.last_time)
        self.speed.x_out = self._pid_x.compute(self.destiny.x, self.position.x)
        self.speed.y_out = self._pid_y.compute(self.destiny.y, self.position.y)
        self.speed.w_out = self._pid_w.compute(self.destiny.w, self.position.w)
        self.calculate_motor_in_speeds()
        self._speed.motor0_out = self._pid_x.compute(self._speed.motor0_in, self._speed.motor0)
        self._speed.motor1_out = self._pid_y.compute(self._speed.motor1_in, self._speed.motor1)
        self._speed.motor2_out = self._pid_w.compute(self._speed.motor2_in, self._speed.motor2)
        self.last_time = now

    def open_move(self, x, y, w):
        self.speed.x_out = x
        self.speed.y_out = y
        self.speed.w_out = x
        self.calculate_motor_in_speeds()
        self._speed.motor0_out = self._speed.motor0_in
        self._speed.motor1_out = self._speed.motor1_in
        self._speed.motor2_out = self._speed.motor2_in
