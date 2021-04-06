"""
1523. Count Odd Numbers in an Interval Range
Easy

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).



Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].



Constraints:

    0 <= low <= high <= 10^9

"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:

        if high == low:
            return 1 if low % 2 != 0 else 0

        dif = high - low
        odds = 0
        low_ones = low % 10
        high_ones = high % 10
        print(f'{dif=}, {odds=}, {low_ones=}, {high_ones=}')
        if high_ones < low_ones:
            high_ones += 10
            dif -= 10
        print(f'{dif=}, {odds=}, {low_ones=}, {high_ones=}')
        for i in range(low_ones, high_ones + 1):
            if i % 2 != 0:
                odds += 1
        print(f'{dif=}, {odds=}, {low_ones=}, {high_ones=}')
        if dif // 10 > 0:
            odds += (dif // 10) * 5
        print(f'{dif=}, {odds=}, {low_ones=}, {high_ones=}')
        return odds


if __name__ == '__main__':
    s = Solution()
    print(s.countOdds(586, 2891))
    print('Expected 1153')