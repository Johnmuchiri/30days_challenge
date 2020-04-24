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


# Dynamic programing approach

def find_ocurrencies(arr):
    memo = {}
    for i in arr:
        if i in memo.keys():
            memo[i] += 1
        else:
            memo[i] = 1
    for key in memo:
        if memo[key] == 1:
            return key


##Test

class TestOcurrence(unittest.TestCase):
    def test_ocurrence_1(self):
        arr = [4, 1, 2, 1, 2]
        self.assertEqual(find_ocurrencies(arr), 4)

    def test_ocurrence_2(self):
        arr = [2, 2, 1]
        self.assertEqual(find_ocurrencies(arr), 1)


if __name__ == '__main__':
    unittest.main()
