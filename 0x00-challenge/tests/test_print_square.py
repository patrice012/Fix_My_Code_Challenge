#!/usr/env/python3
"""Test print_squre function"""

import subprocess
import unittest


class Test_print_squre(unittest.TestCase):
    """Test print_square function using python subprocess"""

    def test_print_square_0(self):
        """Test print square with n = 0"""
        args = ["0"]
        program = ["node", "1-print_square.js"]
        res = subprocess.run(program + args,\
            capture_output=True, text=True, check=True)
        output = ""
        self.assertEqual(res.stdout, output)

    def test_print_square_2(self):
        """Test print square with n = 2"""
        args = ["2"]
        program = ["node", "1-print_square.js"]
        res = subprocess.run(program + args,\
            capture_output=True, text=True, check=True)
        _format = "##\n"
        output = ""
        for i in range(int(args[0])):
            output += _format
        self.assertEqual(res.stdout, output)

    def test_print_square_10(self):
        """Test print square with n = 10"""
        args = ["10"]
        program = ["node", "1-print_square.js"]
        res = subprocess.run(program + args,\
            capture_output=True, text=True, check=True)
        _format = "##########\n"
        output = ""
        for i in range(int(args[0])):
            output += _format
        self.assertEqual(res.stdout, output)

    def test_print_square_negative_value(self):
        """Test print square with n = -2"""
        args = ["-2"]
        program = ["node", "1-print_square.js"]
        output = ""
        res = subprocess.run(program + args,\
            capture_output=True, text=True, check=True)
        self.assertEqual(output, res.stdout)

    def test_print_square_no_value(self):
        """Test print square with n not set"""
        args = []
        program = ["node", "1-print_square.js"]
        example = "Example: ./1-print_square.js 8\n"
        usage = "Usage: ./1-print_square.js <size>\n"
        output = f"Missing argument\n{usage}{example}"
        try:
            res = subprocess.run(
                program + args, capture_output=True, text=True, check=True
            )
        except subprocess.CalledProcessError as e:
            self.assertEqual(output, e.stderr)
