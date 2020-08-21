# unit Testing
# test smallest parts of an application in isolation
# good candidates for unit testing: individual classes, modules, or functinos
# bad candidates for unit testing: an entire app, dependicies acorss several classes or modules


# Python comes with a built in module called unittest
# you can write unit tests encapsulated as classes that inherit from unittest.TestCase
# this inheritance gives you accesss to many assertion helpers that let you test the behaviour of your functions
# you can run tests by calling unittest.main()

# example

# activites.py
# def eat(food, is_healthy):
#   pass
# def nap(num_hours):
#   pass

# tests.py
import unittest #test is its own file
from activities import eat, nap, is_funny #import these functions from this file to be tested
class ActivityTests(unittest.TestCase):
  def test_eat_healthy(self):
    """testing healthy"""
    self.assertEqual(eat("broccoli", is_healthy=True),
    "I'm eating broccoli, because my body is a temple")
  def test_eat_unhealthy(self):
    """testing un healthy"""
    self.assertEqual(eat("pizza", is_healthy=False),
    "I'm eating pizza, because YOLO!")
  def test_short_nap(self):
    """testing short nap"""
    self.assertEqual(
      nap(1),
      "I'm feeling refreshed after my 1 hour nap"
    )
  def test_long_nap(self):
    """testing long nap"""
    self.assertEqual(
      nap(3),
      "Ugh I overslept. I didn't mean to nap for 3 hours"
    )
  def test_is_funny_tim(self):
    """tim is never funny test"""
    self.assertFalse(is_funny("tim"), "tim should not be funny")
  def test_is_funny_anyone_else(self):
    """anybody but Tim should be funny"""
    self.assertTrue(is_funny("blue"), "blue should be funny")
    self.assertTrue(is_funny("tammy"), "tammy should be funny")
    self.assertTrue(is_funny("sven"), "sven should be funny")

if __name__ == "__main__":
  unittest.main()

# add docstrings and then run the file with the verbose flag -v to display the name of the test functions

# other types of assertions:

# self.assertEqual(x,y)
# self.assertNotEqual(x,y)
# self assertTrue(x)
# self.assertFalse(x)
# self.assertIsNone(x)
# self.assertIsNotNone(x)
# self.assertIn(x,y)
# self.assertNotIn(x,y)