import unittest

from pyassert import *
from calcul import calcul

class CalculTest(unittest.TestCase):

    def test_should_returnSquare_5(self):
    	assert_that(calcul(5)).equals(25)