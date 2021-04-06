"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1



Constraints:

    1 <= nums.length <= 104
    -9999 <= nums[i], target <= 9999
    All the integers in nums are unique.
    nums is sorted in an ascending order.


"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        found = False
        _max = len(nums)
        _min = 0
        _mid = _max // 2

        while not found:
            # print(_min, _mid, _max)
            if _max == 1:
                return 0 if nums[0] == target else -1

            if _mid > _max or _mid == _min:
                return -1

            if nums[_mid] == target:
                return _mid
            else:
                if nums[_mid] < target:
                    _min = _mid
                    _mid = (_min + _max) // 2
                else:
                    _max = _mid
                    _mid = (_min + _max) // 2


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert sol.search(nums, target) == 4

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    assert sol.search(nums, target) == -1