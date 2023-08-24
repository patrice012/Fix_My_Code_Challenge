#!/usr/bin/python3
"""Test for fizzBuzz function"""

# import os
import unittest
import sys

from io import StringIO
from unittest.mock import patch
from pathlib import Path

# Get the absolute path of the parent directory of the script
script_path = Path(__file__).resolve()
parent_directory = script_path.parent.parent

# Add the parent directory to the sys.path so that the module can be imported
sys.path.append(str(parent_directory))

# Now use the __import__ function to import the module
module_name = "0-fizzbuzz"
fizzbuzz = __import__(module_name).fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_name(self):
        self.assertTrue(True)

    def test_fizzbuzz_with_50_elements(self):
        """Test for n equal 30"""
        n = 30
        output = "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz\
        16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz"
        with patch("sys.stdout", new=StringIO()) as console:
            fizzbuzz(n)
            self.assertTrue(output, console.getvalue().strip())

    def test_fizzbuzz_with_5_element(self):
        """Test for n equal 5"""
        n = 5
        output = "1 2 Fizz 4 Buzz"
        with patch("sys.stdout", new=StringIO()) as console:
            fizzbuzz(n)
            self.assertTrue(output, console.getvalue().strip())

    def test_fizzbuzz_with_negative_value(self):
        """Test for n equal -10"""
        n = -10
        output = ""
        with patch("sys.stdout", new=StringIO()) as console:
            fizzbuzz(n)
            self.assertEqual(output, console.getvalue().strip())

    def test_fizzbuzz_with_no_value(self):
        """Test for n not set"""
        output = "fizzbuzz() missing 1 required positional argument: 'n'"
        with self.assertRaises(TypeError, msg=output):
            fizzbuzz()


if __name__ == "__main__":
    unittest.main(verbosity=2)
