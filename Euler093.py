# Solution to Project Euler problem 93 by tdnzr.


# What does it mean to consider arithmetic operations plus brackets / parentheses?
# I'm not sure. Maybe the following?
# 0a) Generate all sets of four digits a < b < c < d.
# 0b) Generate all permutations of this set.
# 1) Pick two numbers from the set of four digits, A and B.
# (We don't need to care about the order here: e.g. 3+4 = 4+3 whereas 4-3 != 3-4,
# but there's no problem if I generate all permutations.)
# 2) Apply an operation to A and B: (+, -, *, /). Call the result AB. Order matters here.
# 3) Pick one of the remaining numbers as C.
# 4) Apply an operation to AB and C. Call the result ABC. Order matters again. (AB-C != C - AB)
# 5) Apply an operation to ABC and D.
# The algorithm above should cover all cases except for those where I put brackets
# around both (A, B) *and* around (C, D), e.g. (8/4) + (9/3) isn't covered by the algorithm above.
# For those, I need a separate algorithm after step 2:
# 3b) Apply an operation to the remaining numbers, C and D.
# 4b) Apply an operation to on AB and CD.


from itertools import permutations


def applyOperation(firstNumber, secondNumber, index):
	"""Return the result of applying one of the four basic arithmetic operations
	to the firstNumber and SecondNumber, based on the number given as index."""
	if index == 0:
		return firstNumber + secondNumber
	elif index == 1:
		return firstNumber - secondNumber
	elif index == 2:
		return firstNumber / secondNumber
	elif index == 3:
		return firstNumber * secondNumber


def run():
    # Create a list of all sets of four digits a < b < c < d.
    # Adjusting the ranges like I've done below is faster than doing a
    # construction with 4 ranges of 1...9+1 plus the condition "if a < b < c < d".
    setOfDigits = [(a, b, c, d) for a in range(1,   6+1)
                                for b in range(a+1, 7+1)
                                for c in range(b+1, 8+1)
                                for d in range(c+1, 9+1)]

    longestChain = 0
    answer_tuple = ()
    # Generate all permutations of each set of four digits, then apply
    # all combinations of the four basic arithmetic operations to them.
    for digitTuple in setOfDigits:
        setOfResults = set()
        for A, B, C, D in permutations(digitTuple):
            # i, j, k correspond to the first, second, and third operation.
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        # First, we just apply all the operations to A and B, then AB and C,
                        # then ABC and D.
                        # Because we loop through all permutations,
                        # we don't have to calculate results like BA or CAB separately.
                        AB = applyOperation(A, B, i)
                        ABC = applyOperation(AB, C, j)
                        ABCD = float(applyOperation(ABC, D, k))  # Workaround: otherwise some results are already int, and int doesn't have the method is_integer().
                        
                        # Results consisting of two separate brackets, like AB / CD,
                        # do however need to be calculated separately:
                        CD = applyOperation(C, D, j)
                        AB_CD = float(applyOperation(AB, CD, k))  # Workaround: otherwise some results are already int, and int doesn't have the method is_integer().

                        # Now that we've applied the four operations,
                        # we can add it to the set of results if it's in integer.
                        if ABCD.is_integer():
                            setOfResults.add(int(ABCD))
                        if AB_CD.is_integer():
                            setOfResults.add(int(AB_CD))

        # Now check how many consecutive integers 1 ... n we've been able to generate:
        for number in range(1, len(setOfResults)):
            if number not in setOfResults:
                if number - 1 > longestChain:
                    longestChain = number - 1
                    answer_tuple = digitTuple
                break
    
    return ''.join(str(n) for n in answer_tuple)

if __name__ == "__main__":
    print (f"The set {run()} yields the longest chain of consecutive positive integers 1 to n.")
