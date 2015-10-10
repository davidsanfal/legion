import unittest
from legion.legionary.omnidirectional import Omnidirectional
from legion.legionary.legionary import Legionary


class OmnidirectionalTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def simple_test(self):
        testbot = Omnidirectional()
        self.assertTrue(isinstance(testbot, Legionary))
        testbot.speeds = [1, 0, 0]
        self.assertEqual(testbot.real_speed, [1, 0, 0])
        testbot.speeds = [0, 1, 0]
        self.assertEqual(testbot.real_speed, [0, 1, 0])
        testbot.speeds = [0, 0, 1]
        self.assertEqual(testbot.real_speed, [0, 0, 1])
