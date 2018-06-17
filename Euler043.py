# Solution to Project Euler problem 43.

# Pandigital numbers also appeared in problem 41, so I originally borrowed and adapted the solution from there.

from itertools import permutations


def is_substring_divisible(string):
    primeList = [2, 3, 5, 7, 11, 13, 17]
    # Create substrings à 3 digits from positions 2-4 to 8-10,
    # and check if they are divisible by a certain prime:
    for i in range(6+1):
        substring = string[i+1:i+4]
        if int(substring) % primeList[i] != 0:
            return False
    else:
        return True


def run():
    total_sum = 0
    # Construct all pandigital numbers via itertools.permutations.
    # permutations returns a tuple, so we have to join it into a string.
    for pandigitalTuple in permutations("0123456789"):
        if pandigitalTuple[0] == "0":  # Skip cases with a leading 0.
            continue
        numberString = "".join(pandigitalTuple)
        if is_substring_divisible(numberString):
            total_sum += int(numberString)

    return total_sum


if __name__ == "__main__":
    print(f"The sum of all 0 to 9 pandigital numbers with [the weird property] is: {run()}")
