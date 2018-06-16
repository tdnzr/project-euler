# Solution to Project Euler problem 36.


def dec_to_bin(x):  # The command bin(10) returns e.g. '0b1010', so we cut off the first two characters.
    """Converts a decimal number to binary, then returns it as a string."""
    return bin(x)[2:]


def run():
    palindrome_sum = 0

    for i in range(1, 1_000_000):  # Numbers *less than* one million
        decimal_string = str(i)
        if decimal_string == decimal_string[::-1]:  # Palindrome test: compare string with reversed string.
            binary_string = dec_to_bin(i)
            if binary_string == binary_string[::-1]:  # No need to check for leading zeroes imo.
                palindrome_sum += i

    return palindrome_sum


if __name__ == "__main__":
    print(f"The sum of all numbers, less than one million, which are palindromic in base 10 and base 2 is: {run()}")
