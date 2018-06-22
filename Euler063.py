# Solution to Project Euler problem 63 by tdnzr.

# About the only difficult thing here seems to be the question of what the upper bound is.
# 9**10 = 3486784401 and has 10 digits. After trying some numbers manually (I could've used another quick program for this),
# it turns out that 9**22 = 984770902183611232881 has only 21 digits,
# whereas 9**21 also has 21 digits. So there's no need to check powers above 21.


# I originally feared the following code would be double-counting stuff because the representations aren't unique,
# e.g. 9=3^2=9^1. But obviously a number cannot be simultaneously 3 or 1 digits long, # so while there are duplicates
# in listOfPowers, at most one of them fulfills the condition given in the problem, and we aren't double-counting anything.


def run():
    listOfPowers = [(number, exponent, number**exponent)
                    for number in range(1, 9+1)
                    for exponent in range(1, 21+1)]  # No need to consider an exponent of zero, since there are no zero-digit numbers.

    counter = 0
    for number, exponent, result in listOfPowers:
        if len(str(result)) == exponent:
            # print (f"Valid result: {number} ** {exponent:2} = {result}")
            counter += 1
    return counter


if __name__ == "__main__":
    print(f"Exactly {run()} n-digit positive integers exist which are also an nth power.")
