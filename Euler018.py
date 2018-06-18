# Solution to Project Euler problem 18.

# Algorithm: To calculate the maximum path, I can decimate the row at the very bottom, then work my way upwards.
# Example:
#    3
#   7 4
#  2 4 6
# 8 5 9 3
# I can decimate this triangle by adding max(8, 5) to the 2, max(5, 9) to the 4,
# max(9, 3) to the 6, and then eliminate or ignore row four.


def run():
    inputFile = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

    # Turn the given triangle string into a matrix / list of lists of integers.
    # Example result: triangle = [[75], [95, 64], [17, 47, 82]]
    triangle = []
    for line in inputFile.splitlines():
        triangle_line = [int(s) for s in line.split()]
        triangle.append(triangle_line)

    # Now we decimate the triangle, row for row, beginning at the bottom.
    # The outer loop begins at the second-to-last row and goes upwards;
    # the inner loop iterates through all columns of the row.
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    # After we've decimated the triangle, the element at the top contains the sum of the longest path.
    return triangle[0][0]


if __name__ == "__main__":
    print(f"The sum of the largest path is: {run()}")
