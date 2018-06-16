# Solution to Project Euler problem 4.
# Initial, obviously highly inefficient solution.
# A solution that began by multiplying the highest factors first (like 999*999),
# would be much faster at finding the highest palindrome.


def run():
    product = 0
    setOfPalindromes = set()
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i*j
            palindromeTest = str(product)
            reversedString = palindromeTest[::-1]  # This reverses the string.
            if palindromeTest == reversedString:
                setOfPalindromes.add(product)
    return(max(setOfPalindromes))


if __name__ == "__main__":
    print(run())
