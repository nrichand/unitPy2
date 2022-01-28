from mockito import mock, verify
import unittest

from calcul import calcul

class CalculTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()

        calcul(out)

        verify(out).write("Hello world of Python\n")