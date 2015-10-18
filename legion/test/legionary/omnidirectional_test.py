import unittest
from legion.legionary.omnidirectional import Omnidirectional
from legion.legionary.legionary import Legionary


class OmnidirectionalTest(unittest.TestCase):

    def setUp(self):
        self.testbot = Omnidirectional()

    def tearDown(self):
        pass

    def simple_test(self):
        self.assertTrue(isinstance(self.testbot, Legionary))

    def position_test(self):
        self._set_speed(1, 0, 0)
        self._set_speed(0, 1, 0)
        self._set_speed(1, 1, 0)
        self._set_speed(1, 1, 1)
        self._set_speed(17, 23, 12)
        self._set_speed(17, -23, 12)
        self._set_speed(-17, 23, 12)
        self._set_speed(17, 23, -12)
        self._set_speed(0.01, 0.01, 0.01)

    def _set_speed(self, x, y, w):
        self.testbot.speed.x_in = x
        self.testbot.speed.y_in = y
        self.testbot.speed.w_in = w
        self.testbot.read_robot_speeds()

        self.assertEqual(round(self.testbot.speed.x, 12), x)
        self.assertEqual(round(self.testbot.speed.y, 12), y)
        self.assertEqual(round(self.testbot.speed.w, 12), w)
