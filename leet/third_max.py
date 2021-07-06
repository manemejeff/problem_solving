"""
Third Maximum Number

Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.



Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

Example 2:

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.



Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1


Follow up: Can you find an O(n) solution?
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = None
        second_max = None
        third_max = None
        for item in nums:

            if item == first_max or item == second_max or item == third_max:
                continue

            if not first_max or item > first_max:
                third_max = second_max
                second_max = first_max
                first_max = item
            elif not second_max or item > second_max:
                third_max = second_max
                second_max = item
            elif not third_max or item > third_max:
                third_max = item

        # print(f'{first_max=}, {second_max=}, {third_max=}')

        if third_max is None:
            return first_max
        else:
            return third_max