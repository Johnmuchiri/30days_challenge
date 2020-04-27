import unittest

"""

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Approach 1 time complexity O(loggn) and space complexity of O(logn)
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        result = True
        happy_number = n
        while happy_number != 1:
            if happy_number in visited:
                ##cycle detected
                result = False
                break
            visited.append(happy_number)
            happy_number = self.get_next(happy_number)
        return result

    def get_next(self, n):
        total_sum = 0
        while n > 0:
            n, j = divmod(n, 10)
            total_sum += j ** 2
        return total_sum


##Test

class TestOcurrence(unittest.TestCase):

    def test_ocurrence_1(self):
        solution = Solution()
        self.assertEqual(solution.isHappy(19), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
