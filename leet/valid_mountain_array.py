"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true



Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 104


"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_ind = arr.index(max(arr))

        if max_ind == 0 or max_ind == len(arr) - 1:
            return False

        for i in range(max_ind, -1, -1):
            if i == max_ind:
                prev = arr[i]
                continue

            if prev > arr[i]:
                prev = arr[i]
                continue
            else:
                return False

        for i in range(max_ind, len(arr)):
            if i == max_ind:
                prev = arr[i]
                continue

            if prev > arr[i]:
                prev = arr[i]
                continue
            else:
                return False

        return True
