# Solution to Project Euler problem 31 by tdnzr.

# Realisation: The problem just consists of finding all valid tuples (a, b, c, d, e, f, g, h),
# where a ... h correspond to the coins for 1p, 2p, 5p, 10p, 20p, £1, and £2,
# which fulfill the equation a + 2b + 5c + 10d + 20e + 50f + 100g + 200h == 200.
# Separate realisation: But a simple nested loop for a...h is too inefficient to be brute-forced.

# Hence, we still do a nested for-loop, but compute the ranges for each loop.

# Amazingly, the following worked without any debugging...


def run():
    # Special case for the £2 coin, so I can ignore it in the remaining exercise.
    counter = 1

    # Loop through the coins in descending order (g = £1 ... a = 1p),
    # then compute the remainder each time.
    for g in range(200 // 100 + 1):  # £1 coin
        remainderG = 200 - 100*g
        for f in range(remainderG // 50 + 1):
            remainderF = remainderG - 50*f
            for e in range(remainderF // 20 + 1):
                remainderE = remainderF - 20*e
                for d in range(remainderE // 10 + 1):
                    remainderD = remainderE - 10*d
                    for c in range(remainderD // 5 + 1):
                        remainderC = remainderD - 5*c
                        for b in range(remainderC // 2 + 1):
                            # Once we've reached this point, we're done; we've found a valid combination.
                            # So there's no need for a separate loop for the single pence.

                            # remainderB = remainderC - 2*b
                            # a = remainderB
                            counter += 1
    return counter


if __name__ == "__main__":
    print(run())
