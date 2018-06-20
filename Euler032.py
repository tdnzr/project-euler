# Solution to Project Euler problem 32.

# Preliminary thoughts:
# I need terms that contain 9 digits spread across two factors plus their product.
# 100 * 1000 =  100000, i.e. 3 digits * 4 digits = 6 digits
# 999 * 9999 = 9989001, i.e. 3 digits * 4 digits = 7 digits
# So: A product of A digits times B digits yields between A + B - 1 and A + B digits.
# Total number of digits: A + B + A + B - 1 or A + B + A + B, i.e. 2(A+B)-1 or 2(A+B). This number must equal 9.
# So: 2(A+B)-1 = 9 or 2(A+B)=9. The latter cannot be fulfilled for integers: 2(A + B) = 9 -> A + B = 4.5.

# So I actually *only* have the condition 2(A + B) - 1 = 9 or 2(A + B) = 10 or A + B=5.
# So I *always* have 5 digits on the left of the equation, and the product always has exactly 4 digits!

# Which leads to the following algorithm:
# Loop through all products from 1000 to 9999 which contain distinct digits from 1 to 9.
# Concerning the factors, I can restrict myself to A < B,
# so I only have to consider the cases where A = 1 or A = 2, i.e. A in range(1, 99 + 1).
# Then I check if product can be divided by the first factor, and if so,
# whether both factors plus product concatenated together pandigital.
# And that's the complete algorithm.

# Note: The program I've implemented could still be improved, but the program is already fast enough.
# 1) The outer for-loop plus if-statement could be replaced by a more efficient 
# loop through itertools.combinations of the digits "1" ... "9".
# We wouldn't even need to convert to string any longer.
# 2) Also, it's weird that we generate a set of candidateString (and, below, of testString),
# but then look for the "0", not in the set (which provides efficient lookups), but rather in the string.


def run():
    uniqueProducts = set()

    for candidate in range(1000, 9999 + 1):  # 1000...9999
        candidateString = str(candidate)
        # set(string) counts the number of unique elements in a string.
        # So to check that a number only contains unique digits,
        # I can just check whether len(set(string)) == len(string).
        # But I separately have to ensure that the string contains no zero.
        if len(set(candidateString)) == len(candidateString) and "0" not in candidateString:
            for factor in range(1, 99 + 1):  # The first factor must have 1 or 2 digits.
                if candidate % factor == 0:  # Test if candidate is divisible by factor.
                    factor2 = candidate // factor
                    testString = candidateString + str(factor) + str(factor2)
                    # Test if the term is pandigital.
                    # And by adding it to a set, we ensure that we don't double-count it.
                    if len(set(testString)) == 9 and "0" not in testString:
                        uniqueProducts.add(candidate)

    total_sum = sum([product for product in uniqueProducts])
    return total_sum

if __name__ == "__main__":
    print (f"The sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital is: {run()}")
