# Solution to Project Euler problem 62 by tdnzr.

# I originally tried a solution based on going through all permutations of a cube,
# and testing if these permutations were also cubes. But this was impossibly slow.
# In contrast, this solution is based on the insight that there was no need to compute all permutations.
# In contrast to the original attempt, this solution yields the correct result in just 0.2s.


from collections import Counter


def run():
    # Make a list of cubes, then sort all cubes by their digits, in ascending order.
    # This makes the later permutation tests trivial.
    listOfCubes = [i**3 for i in range(1, 10000)]
    sortedCubes = ["".join(sorted(str(cube))) for cube in listOfCubes]

    # Count how often each cube appears, then find five-fold duplicates:
    counter = Counter(sortedCubes)
    sortedCandidates = [number for (number, amount) in counter.items()
                        if amount == 5]

    # Find the corresponding sorted numbers in sortedCubes. Because their indices haven't changed,
    # I can re-compute the corresponding un-sorted number by taking the cube of their positions in the list.
    actualCandidates = [(sortedCubes.index(i) + 1) ** 3
                        for i in sortedCandidates if i in sortedCubes]

    return min(actualCandidates)


if __name__ == "__main__":
    print(f"{run()} is the smallest cube for which exactly five permutations of its digits are cube.")
