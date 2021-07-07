"""
Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.


"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands_counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == '1':
                    islands_counter += 1
                    self.reverse_island(grid, i, j)

        return islands_counter

    def reverse_island(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
            return

        grid[i][j] = '0'
        self.reverse_island(grid, i + 1, j)
        self.reverse_island(grid, i - 1, j)
        self.reverse_island(grid, i, j + 1)
        self.reverse_island(grid, i, j - 1)
