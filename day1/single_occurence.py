"""Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4"""
import sys

import unittest

def singleNumber(A):
    x = 0
    for n in A:
        x = x ^ n
    return x


##Test

class TestOcurrence(unittest.TestCase):
    def test_ocurrence_1(self):
        arr = [4, 1, 2, 1, 2]
        self.assertEqual(singleNumber(arr), 4)

    def test_ocurrence_2(self):
        arr = [2, 2, 1]
        self.assertEqual(singleNumber(arr), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
