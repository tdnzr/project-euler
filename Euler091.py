# Solution to Project Euler problem 91.

# Pythagoras: The length of a line from (x1, y1) to (x2, y2) is equal to: sqrt((x2 - x1)**2 + (y2 - y1)**2)

# The algorithm I've used still has some remaining inefficiences due to symmetries:
# Firstly, the program currently doesn't distinguish between P=(0,1) and Q=(1,0) vs. P=(1,0) and Q=(0,1),
# so it's slower than necessary by a factor of 2, and I need to divide the final counter by 2.
# Secondly, the program calculates symmetrical cases multiple times (P=(0,1), Q=(2,0) vs. P=(2,0), Q=(0,1)).

from time import time
# from itertools import combinations
start = time()

def run():
    maxSideLength = 50
    pointsList = [(x, y) for x in range(maxSideLength+1)
                  for y in range(maxSideLength+1) if (x, y) != (0, 0)]
    rightTriangleCounter = 0

    for px, py in pointsList:
        for qx, qy in pointsList:
            if (px, py) == (qx, qy):  # If pointP = pointQ, we don't have a triangle.
                continue
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
    rightTriangleCounter //= 2  # See the comment at the top - this is necessary due to a symmetry problem.
    return rightTriangleCounter


if __name__ == "__main__":
    print(f"Given that 0 <= x1, y1, x2, y2 <= 50, {run()} right triangles can be formed.")
    print(time()-start)
