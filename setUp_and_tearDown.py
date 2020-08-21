# setUp and tearDown
# for larger apps you may want similiar app states before running tets
# setUp runs before each test method
# tearDown runs after eact test method
# common use cases: adding/removing data from a test database, creating instances of a class
import unittest
from robot import Robot

# class SomeTests(unittest.TestCase):

#   def setUp(self):
#     #do setu phere
#     pass

#   def test_first(self):
#     #setUp runs before
#     #teardown runs after
#     pass

#   def test_second(self):
#     #setUp runs before
#     #teardown runs after
#     pass

#   def tearDown(self):
#     #do teardown here
#     pass

class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()