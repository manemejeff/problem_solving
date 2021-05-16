"""
1002. Find Common Characters
Easy

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]



Note:

    1 <= A.length <= 100
    1 <= A[i].length <= 100
    A[i][j] is a lowercase letter


"""
from typing import List


def commonChars(words: List[str]) -> List[str]:
    list_of_sets = []
    res = []
    min_num = None

    # getting intersections
    for word in words:
        list_of_sets.append(set(word))
    inters = set.intersection(*list_of_sets)

    # counting min occur in words
    for char in inters:
        min_num = None
        counter = 0
        for word in words:
            counter = word.count(char)
            if min_num is None or min_num > counter:
                min_num = counter
        # appending char to final list
        if counter != 0:
            for i in range(min_num):
                res.append(char)

    return (res)


if __name__ == '__main__':
    print(commonChars(["bella", "label", "roller"]))
    print(commonChars(["cool", "lock", "cook"]))
    """
    Runtime: 40 ms, faster than 92.69% of Python3 online submissions for Find Common Characters.
    Memory Usage: 14.6 MB, less than 9.15% of Python3 online submissions for Find Common Characters.
    """
