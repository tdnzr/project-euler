# Solution to Project Euler problem 26.

# I struggled a lot with this problem and had to look up some stuff.
# Solution: Do long division until we end up dividing by the same number again.
# Note that my implementation of long division here only works properly if dividend <= divisor.
# It also computes the string of the remainder, which is neat but not required in the exercise.

def long_division(dividend, divisor):
    """Divides the dividend by the divisor via long division. This implementation requires dividend <= divisor.
    Returns the result as a string, plus the length of the recurring part of the remainder."""
    
    assert dividend <= divisor, "This implementation of long division only works properly if dividend <= divisor."
    
    remainderString = ""
    dividends_list = []
    recurringLength = 0
    while dividend not in dividends_list:
        dividends_list.append(dividend)
        if dividend % divisor == 0:
            remainderString += (str(dividend // divisor))
            return remainderString[0] + "." + remainderString[1:], 0
        elif dividend > divisor:
            remainderString += (str(dividend // divisor))
            dividend = (dividend % divisor) * 10
        else:  # dividend < divisor
            remainderString += "0"
            dividend = (dividend % divisor) * 10
    recurringLength = len(dividends_list) - dividends_list.index(dividend)
    return remainderString[0] + "." + remainderString[1:], recurringLength


def run():
    maxDigit = 0
    maxRecurring = 0
    for i in range(1, 1000):  # 1/d with d < 1000
        remainderString, recurring = long_division(1, i)
        #if i < 200:
        #	print(f"1/{i:2} = {remainderString} --- {recurring}")
        if maxRecurring < recurring:
            maxRecurring = recurring
            maxDigit = i
    return maxDigit


if __name__ == "__main__":
    print(f"The value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part is: {run()}.")
