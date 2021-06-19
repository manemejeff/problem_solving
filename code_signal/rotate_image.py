"""
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.array.integer a

    Guaranteed constraints:
    1 ≤ a.length ≤ 100,
    a[i].length = a.length,
    1 ≤ a[i][j] ≤ 104.

    [output] array.array.integer

"""


def rotateImage(a):
    lng = len(a)
    for i in range(lng):
        for j in range(i, len(a[i])):
            a[i][j], a[j][i] = a[j][i], a[i][j]

    for i in range(lng):
        for j in range(lng // 2):
            a[i][j], a[i][lng - 1 - j] = a[i][lng - 1 - j], a[i][j]

    return a


if __name__ == '__main__':
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print(rotateImage(a))
