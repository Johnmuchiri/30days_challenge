import unittest


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
