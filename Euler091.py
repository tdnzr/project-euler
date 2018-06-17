# Solution to Project Euler problem 91.

# Pythagoras: The length of a line from (x1, y1) to (x2, y2) is equal to: sqrt((x2 - x1)**2 + (y2 - y1)**2)

# I suspect the algorithm I've used could still be somewhat improved if I could consider
# some more cases of symmetry, but it's already pretty good due to itertools.combinations.

from itertools import combinations

def run():
    maxSideLength = 50
    points = ((x, y) for x in range(maxSideLength + 1)
                     for y in range(maxSideLength + 1)
                     if (x, y) != (0, 0))
    rightTriangleCounter = 0

    # By using itertools.combinations, we don't double-count symmetrical cases where P and Q 
    # have just switched places (triangles OPQ = OQP). Otherwise we'd have twice as many calculations.
    for (px, py), (qx, qy) in combinations(points, 2):
        squareLengthOP = px**2 + py**2
        squareLengthOQ = qx**2 + qy**2
        squareLengthPQ = (px - qx)**2 + (py - qy)**2

        # By only comparing square lengths, we save ourselves the effort of having to take square roots anywhere in the program.
        squareLengths = [squareLengthOP, squareLengthOQ, squareLengthPQ]
        squareLengths.sort()  # Now the maximum of the list is at position three (index 2) of the list.
        # Use Pythagoras to check whether OPQ is a right triangle.
        # a**2 + b**2 must equal c**2, so obviously c is maximal and at index 2 of the sorted list.
        if (squareLengths[0] + squareLengths[1]) == squareLengths[2]:
            rightTriangleCounter += 1
    return rightTriangleCounter


if __name__ == "__main__":
    print(f"Given that 0 <= x1, y1, x2, y2 <= 50, {run()} right triangles can be formed.")
