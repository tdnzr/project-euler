# Solution to Project Euler problem 26 by tdnzr.

# I struggled a lot with this problem and had to look up some stuff.
# Solution: Do long division until we end up dividing by the same number again.
# Note that my solution also returns the correct result of the division as a string
# (including the recurring part).
# While kind of neat - I certainly learned something by implementing it -,
# it's not actually required in the exercise.


def long_division(dividend, divisor):
    """Divides the dividend by the divisor via long division.
    Returns the result as a string, plus the length of the recurring part of the remainder."""
    
    remainderString = ""
    dividends_list = []
    recurringLength = 0

    # Compute the part to the left of the period first,
    # e.g. 10 / 4 = 2.5, so we compute the "2." part first:
    quotient, remainder = divmod(dividend, divisor)  # in case of integers, divmod(a, b) = (a // b, a % b)
    remainderString += str(quotient)
    if remainder == 0:
        return remainderString, 0
    # Then if there's a remainder, we add a period in preparation for long division
    # before we head into the while-loop:
    else:
        remainderString += "."
        dividend = remainder * 10
    
    # Now that dividend < divisor, we can deal with long division without worrying about the period:
    while dividend not in dividends_list:
        dividends_list.append(dividend)
        # Compute quotient and remainder, and append the quotient to the remainderString.
        # Then if the remainder is zero, we're done; otherwise, just like in division on paper,
        # we multiply the remainder by ten and begin the process anew.
        quotient, remainder = divmod(dividend, divisor)
        remainderString += str(quotient)
        if remainder == 0:
            return remainderString, 0
        else:
            dividend = remainder * 10

    recurringLength = len(dividends_list) - dividends_list.index(dividend)
    # Put the recurring part of the remainder in parentheses,
    # for no other reason than because we can:
    remainderString = remainderString[:-recurringLength] + "(" + remainderString[-recurringLength:] + ")"
    return remainderString, recurringLength


def run():
    maxDigit = 0
    maxRecurring = 0
    for i in range(1, 1000):  # 1 / d with d < 1000
        remainderString, recurring = long_division(1, i)
        # Optional, for debugging:
        # print(f"1 / {i:4} = {remainderString} --- {recurring}")
        if maxRecurring < recurring:
            maxRecurring = recurring
            maxDigit = i
    return maxDigit


if __name__ == "__main__":
    print(f"The value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part is: {run()}.")
