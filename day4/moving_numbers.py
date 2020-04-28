"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.


hint 1 : In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.

hint 2 :  A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.
"""
import unittest

"""
O(n) time complexity and 0(1) space complexity
"""


def move_numbers(arr):
    n = len(arr)

    j = 0  ##runner pointer
    i = 0  ##last non zero index pointer
    ##case when the first inded is a non zero digt
    if arr[j] != 0:
        arr[i] = arr[j]
        j += 1
        i += 1

    ## case when the first index is a  zero digit
    while j < n:
        if arr[j] == 0:
            j += 1
        else:
            arr[i], arr[j] = arr[j], 0
            i += 1
            j += 1

    return arr


arr = [1, 0, 2, 0, 3, 12]
print(move_numbers(arr))


class TestOcurrence(unittest.TestCase):
    def test_ocurrence_1(self):
        arr = [0, 1, 0, 3, 12]
        self.assertEqual(move_numbers(arr), [1, 3, 12, 0, 0])

    def test_ocurrence_2(self):
        arr = [1, 0, 1, 0, 3, 12]
        self.assertEqual(move_numbers(arr), [1, 1, 3, 12, 0, 0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
