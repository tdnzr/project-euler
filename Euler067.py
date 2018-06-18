# Solution to Project Euler problem 67.

# This problem is identical to problem 18, it just uses a larger data set.
# So I copied the code from there.


def run():
    with open('Euler067_triangle.txt') as inputFile:
        # Turn the given triangle string into a matrix / list of lists of integers.
        # Example result: triangle = [[75], [95, 64], [17, 47, 82]]
        triangle = []
        for line in inputFile.read().splitlines():
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
