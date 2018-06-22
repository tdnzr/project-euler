# Solution to Project Euler problem 39 by tdnzr.

# This problem is tangentially related to problem 9, Special Pythagorean triplet.

# As an optimization, and because we don't want to double-count solutions, we require a <= b <= c.

def run():
    numOfSolutions = []

    for p in range(3, 1000+1):  # p <= 1000, and we won't have a valid triangle for p < 3.
        solutions = 0
        # The following loop must begin with a = 1, otherwise we'd get results like [a,b,c]=[0,100,100],
        # which would fulfill the criterion a**2 + b**2 == c**2 without yielding a valid triangle.
        # Also, because we require a <= b <= c, a can at most equal p/3.
        # b can at most equal p/2 for the same reason.
        for a in range(1, p // 3 + 1):
            for b in range(a, p // 2 + 1):
                c = p - a - b
                if a**2 + b**2 == c**2:
                    solutions += 1
        numOfSolutions.append(solutions)

    return numOfSolutions.index(max(numOfSolutions)) + 3  # p starts at 3


if __name__ == "__main__":
    print(f"The perimeter value which yields the most solutions for the problem is {run()}.")
