"""
Sort Array By Parity

Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.



Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.



Note:

    1 <= nums.length <= 5000
    0 <= nums[i] <= 5000


"""
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []

        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])

        return [*even, *odd]
