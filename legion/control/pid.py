import time


class PID(object):

    def __init__(self, kp, ki, kd, out_min, out_max):
        self._kp = kp
        self._ki = ki
        self._kd = kd
        self._out_min = out_min
        self._out_max = out_max
        self._inAuto = True

    def initialize(self):
        self._last_input = self._input
        self._I_term = self._output
        if self._I_term > self._out_max:
            self._I_term = self._out_max
        elif self._I_term < self._out_min:
            self._I_term = self._out_min

    def compute(self, setpoint, sensor_input):
        self._setpoint = setpoint
        self._input = sensor_input
        if not self._inAuto:
            return 0
        now = time.time() * 1000
        time_change = now - self._last_time

        error = self._setpoint - self._input
        self._I_term += (self._ki * error * time_change)

        if self._I_term > self._out_max:
            self._I_term = self._out_max
        elif self._I_term < self._out_min:
            self._I_term = self._out_min
        dErr = (error - self._last_err) / time_change

        self._output = self._kp * (error + self._I_term + self._kd * dErr)

#       if self._output > self._out_max:
#           self._output = self._out_max
#       else if self._output < self._out_min:
#           self._output = self._out_min

        if self._output > self._out_max:
            self._I_term = self._I_term - self._output - self._out_max

        elif self._output < self._out_min:
            self._I_term += self._out_min - self._output

        self._output = self._kp * error + self._I_term + self._kd * dErr

        self._last_err = error
        self._last_time = now
        return self._output

    def set_tunings(self, kp, ki, kd):
        self._kp = kp
        self._ki = ki
        self._kd = kd

    def set_output_limits(self, min_out, max_out):
        if min_out > max_out:
            return
        self._out_min = min_out
        self._out_max = max_out

        if self._output > self._out_max:
            self._output = self._out_max
        elif self._output < self._out_min:
            self._output = self._out_min

        if self._I_term > self._out_max:
            self._I_term = self._out_max
        elif self._I_term < self._out_min:
            self._I_term = self._out_min

    def auto(self, mode):
        if (mode and not self._inAuto):
            self.intialize()
        self._inAuto = mode
