"""
Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O( n ) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
import unittest


def max_subarray_sum(arr):
    n = len(arr)
    sum_sofar = arr[0]
    max_global = 0
    for i in range(1, n):
        sum_sofar = max(arr[i], sum_sofar + arr[i])
        max_global = max(sum_sofar, max_global)
    return max_global

##Test

class TestOcurrence(unittest.TestCase):
    def test_ocurrence_1(self):
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_sum(arr), 6)

    def test_ocurrence_2(self):
        arr = [4,-1,2,1]
        self.assertEqual(max_subarray_sum(arr), 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)

